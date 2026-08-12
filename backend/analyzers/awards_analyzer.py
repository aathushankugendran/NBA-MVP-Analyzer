"""
awards_analyzer.py

Prints every award winner for a league/season, mirroring the "awards"
command in the site's built-in terminal.

Usage:
    python awards_analyzer.py --league nba
    python awards_analyzer.py --league nfl
    python awards_analyzer.py --league mlb
"""

import argparse
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

LEAGUE_FILES = {
    "nba": "nba_2025_26.json",
    "nfl": "nfl_2025.json",
    "mlb": "mlb_2025.json",
}


def load_league(league: str) -> dict:
    path = os.path.join(DATA_DIR, LEAGUE_FILES[league])
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def walk_awards(data: dict, prefix: str = "") -> None:
    """Recursively print award_name/winner pairs found anywhere in the dataset."""
    if isinstance(data, dict):
        if "winner" in data:
            label = prefix.strip(" >") or "Award"
            team = f" ({data['team']})" if "team" in data else ""
            print(f"{label}: {data['winner']}{team}")
        for key, value in data.items():
            if key in ("winner", "team", "finalists", "stats", "note", "vote_summary", "result",
                       "position", "award_name", "source_note", "announced_at", "league", "season"):
                continue
            walk_awards(value, f"{prefix} > {key.replace('_', ' ').title()}" if prefix else key.replace('_', ' ').title())


def main() -> None:
    parser = argparse.ArgumentParser(description="Print every award winner for a league/season.")
    parser.add_argument("--league", choices=["nba", "nfl", "mlb"], required=True)
    args = parser.parse_args()

    data = load_league(args.league)
    print(f"{data['league']} {data['season']} Awards")
    print("=" * 50)
    walk_awards(data)


if __name__ == "__main__":
    main()