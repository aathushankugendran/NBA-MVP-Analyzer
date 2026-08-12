"""
app.py

Small Flask API that serves the NBA / NFL / MLB award datasets as JSON,
so the static site's terminal (or any other frontend) can eventually
fetch this instead of using the embedded JS DATA objects.

Run:
    pip install -r requirements.txt
    python app.py

Then:
    GET  /api/<league>/awards            full dataset
    GET  /api/<league>/mvp                just the MVP section
                                           (MLB: /api/mlb/mvp?division=AL)
    GET  /api/<league>/search?q=<name>    search finalists by player name

league is one of: nba, nfl, mlb
"""

import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

LEAGUE_FILES = {
    "nba": "nba_2025_26.json",
    "nfl": "nfl_2025.json",
    "mlb": "mlb_2025.json",
}

app = Flask(__name__)
CORS(app)  # allows the static HTML site to fetch this API from a different origin


def load_league(league: str) -> dict:
    path = os.path.join(DATA_DIR, LEAGUE_FILES[league])
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def collect_finalists(data: dict) -> list:
    """Flatten every finalist / winner-with-a-name object found in the dataset."""
    found = []

    def walk(node):
        if isinstance(node, dict):
            if "name" in node:
                found.append(node)
            if "winner" in node and "name" not in node:
                # e.g. {"winner": "Joe Mazzulla", "team": "Boston Celtics"}
                found.append({"name": node["winner"], "team": node.get("team"), "note": node.get("note")})
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return found


@app.route("/api/<league>/awards", methods=["GET"])
def get_awards(league):
    if league not in LEAGUE_FILES:
        return jsonify({"error": f"unknown league '{league}'"}), 404
    return jsonify(load_league(league))


@app.route("/api/<league>/mvp", methods=["GET"])
def get_mvp(league):
    if league not in LEAGUE_FILES:
        return jsonify({"error": f"unknown league '{league}'"}), 404
    data = load_league(league)
    mvp = data.get("mvp")
    if league == "mlb":
        division = request.args.get("division", "AL").upper()
        mvp = mvp.get(division)
        if mvp is None:
            return jsonify({"error": f"unknown division '{division}'"}), 400
    return jsonify(mvp)


@app.route("/api/<league>/search", methods=["GET"])
def search_player(league):
    if league not in LEAGUE_FILES:
        return jsonify({"error": f"unknown league '{league}'"}), 404
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify({"error": "missing query param 'q'"}), 400

    data = load_league(league)
    matches = [p for p in collect_finalists(data) if p.get("name") and query in p["name"].lower()]
    return jsonify({"query": query, "results": matches})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "leagues": list(LEAGUE_FILES.keys())})


if __name__ == "__main__":
    app.run(debug=True, port=5001)