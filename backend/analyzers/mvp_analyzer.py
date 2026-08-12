"""
mvp_analyzer.py

Loads the real MVP race for a given league/season from the JSON data files
in ../data and prints a breakdown, mirroring the original NBA-MVP-Analyzer
console output but now data-driven and multi-league.

Usage:
    python mvp_analyzer.py --league nba
    python mvp_analyzer.py --league nfl
    python mvp_analyzer.py --league mlb --division AL
    python mvp_analyzer.py --league mlb --division NL
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


def print_finalist(finalist: dict, indent: str = "  ") -> None:
    name = finalist.get("name", "Unknown")
    team = finalist.get("team", "")
    result = finalist.get("result", "")
    line = f"{indent}{name}"
    if team:
        line += f" ({team})"
    if result:
        line += f" — {result}"
    print(line)

    stats = finalist.get("stats")
    if stats:
        stat_str = ", ".join(f"{k.upper()}: {v}" for k, v in stats.items())
        print(f"{indent}  {stat_str}")

    note = finalist.get("note")
    if note:
        print(f"{indent}  note: {note}")


def run_nba_mvp(data: dict) -> None:
    mvp = data["mvp"]
    print(f"NBA {data['season']} MVP Race ({mvp['award_name']})")
    print("-" * 50)
    for finalist in mvp["finalists"]:
        print_finalist(finalist)
        print()
    print(f"Result: {mvp['winner']} wins MVP ({mvp['vote_summary']}).")


def run_nfl_mvp(data: dict) -> None:
    mvp = data["mvp"]
    print(f"NFL {data['season']} MVP Race")
    print("-" * 50)
    for finalist in mvp["finalists"]:
        print_finalist(finalist)
        print()
    print(f"Result: {mvp['winner']} wins MVP ({mvp['vote_summary']}).")


def run_mlb_mvp(data: dict, division: str) -> None:
    division = division.upper()
    mvp = data["mvp"][division]
    print(f"MLB {data['season']} {division} MVP Race")
    print("-" * 50)
    for finalist in mvp["finalists"]:
        print_finalist(finalist)
        print()
    print(f"Result: {mvp['winner']} wins {division} MVP ({mvp['vote_summary']}).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Print the real MVP race for a league/season.")
    parser.add_argument("--league", choices=["nba", "nfl", "mlb"], required=True)
    parser.add_argument("--division", choices=["AL", "NL"], default="AL", help="MLB only: AL or NL")
    args = parser.parse_args()

    data = load_league(args.league)

    if args.league == "nba":
        run_nba_mvp(data)
    elif args.league == "nfl":
        run_nfl_mvp(data)
    elif args.league == "mlb":
        run_mlb_mvp(data, args.division)


if __name__ == "__main__":
    main()