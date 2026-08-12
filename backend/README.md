# MVP Analyzer — Backend

Real 2025-26 NBA, 2025 NFL, and 2025 MLB awards data, plus the Python scripts
and a small API that serve it. This is the backend counterpart to the retro
front-end site — the `python mvp_analyzer.py` commands in the site's built-in
terminal are modeled directly on the CLI scripts here.

## Structure

```
backend/
├── data/
│   ├── nba_2025_26.json     MVP, DPOY, 6MOY, MIP, ROY, COY, All-NBA First Team
│   ├── nfl_2025.json        MVP, OPOY, DPOY, both ROYs, Comeback POY, coaching awards
│   └── mlb_2025.json        AL + NL MVP, Cy Young, ROY, Manager, Comeback POY
├── analyzers/
│   ├── mvp_analyzer.py      CLI: prints the MVP race breakdown for a league
│   └── awards_analyzer.py   CLI: prints every award winner for a league
├── app.py                   Flask API serving the datasets as JSON
├── requirements.txt
└── README.md
```

## Running the CLI scripts

```bash
cd analyzers
python mvp_analyzer.py --league nba
python mvp_analyzer.py --league nfl
python mvp_analyzer.py --league mlb --division AL
python mvp_analyzer.py --league mlb --division NL

python awards_analyzer.py --league nba
python awards_analyzer.py --league nfl
python awards_analyzer.py --league mlb
```

## Running the API

```bash
pip install -r requirements.txt
python app.py
```

Then, with the server running on `http://localhost:5000`:

| Endpoint | Description |
|---|---|
| `GET /api/health` | Confirms the API is up and lists available leagues |
| `GET /api/<league>/awards` | Full dataset for `nba`, `nfl`, or `mlb` |
| `GET /api/<league>/mvp` | Just the MVP section (MLB: add `?division=AL` or `?division=NL`) |
| `GET /api/<league>/search?q=<name>` | Searches every finalist/winner by (partial) name |

Example:
```bash
curl http://localhost:5000/api/nba/mvp
curl "http://localhost:5000/api/mlb/mvp?division=NL"
curl "http://localhost:5000/api/nfl/search?q=mccaffrey"
```

## Connecting this to the front-end site

Right now the site's terminal answers questions from a JS object embedded
directly in `index.html` — it doesn't call this API. To wire them together:

1. Run `python app.py` (or deploy it — e.g. Railway, Render, AWS App Runner's
   successor ECS Express Mode).
2. In `index.html`, replace the hardcoded `NBA_DATA` / `NFL_DATA` JS objects
   with a `fetch('http://localhost:5000/api/nba/awards')` call (swap the URL
   for your deployed API once it's live), and enable CORS on the frontend's
   domain if it's hosted separately (already enabled here via `flask-cors`).
3. Everything downstream — the terminal commands, the winner-highlight
   cards — keeps working unchanged, since they already read from a `DATA`
   object with this same shape.

## Data provenance

All figures were pulled from NBA.com, NFL.com, MLB.com/BBWAA, ESPN, CBS
Sports, and Yahoo Sports award coverage as of the dates on each award
announcement (NBA: May 2026, NFL: Feb 2026, MLB: Nov 2025). This is a
point-in-time snapshot, not a live feed — see each `source_note` field in
the JSON files.