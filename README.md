# NBA-MVP-Analyzer

**A retro, arcade-styled site that tracks real NBA, NFL, and MLB season awards — MVP races, Defensive/Offensive Player of the Year, Rookies of the Year, and more — with a built-in terminal you can query directly.**

🔗 **Live Demo:** _add your Amplify URL here once deployed_
📦 **Repo:** [github.com/aathushankugendran/NBA-MVP-Analyzer](https://github.com/aathushankugendran/NBA-MVP-Analyzer)

---

## What This Project Is

This started as a small interview case study: `a1.py`, a command-line script that took five hardcoded NBA MVP candidates, compared their points/rebounds/assists, and printed a winner using a simple tie-break rule.

I kept building on it because the underlying idea — turning a real awards race into something explorable, not just a static list — was worth taking further. It grew into three things:

1. **A retro front-end site** (`index.html`) with a league toggle (NBA / NFL / MLB), real 2025-26 season award data, winner highlighting, and a built-in retro terminal you can type commands into to query the data live.
2. **A backend** (`backend/`) with the same data as structured JSON, Python CLI analyzers that mirror the original `a1.py` idea (now data-driven and multi-league instead of hardcoded), and a small Flask API for anyone who wants to extend this beyond a static site.
3. **The original script** (`a1.py`), kept as-is — the seed the rest of this grew from.

## How It's Architected

The site is a **plain static HTML/JS page** — no build step, no framework, no server required to run it. It fetches its data directly from the JSON files in `backend/data/` using relative paths, which is what makes it deployable as-is on GitHub Pages, AWS Amplify Hosting, or any static host with zero configuration.

The **Flask API and CLI analyzers in `backend/`** aren't required for the site to work — they exist as a separate, optional layer: a real backend you can run locally, hit with `curl`, or build on top of if this ever needs to pull live stats instead of a point-in-time dataset. The site is intentionally decoupled from it so a recruiter (or anyone) can open the live link and have it just work, without a server running somewhere to keep alive.

```
NBA-MVP-Analyzer/
├── a1.py                        original 5-player NBA MVP script
├── index.html                   the retro site (NBA/NFL/MLB, no build step)
├── README.md
└── backend/
    ├── data/
    │   ├── nba_2025_26.json     MVP, DPOY, 6MOY, MIP, ROY, COY, All-NBA
    │   ├── nfl_2025.json        MVP, OPOY, DPOY, both ROYs, Comeback POY
    │   └── mlb_2025.json        AL + NL MVP, Cy Young, ROY, Manager, Comeback POY
    ├── analyzers/
    │   ├── mvp_analyzer.py      CLI: real MVP race breakdown, per league
    │   └── awards_analyzer.py   CLI: every award winner, per league
    ├── app.py                   Flask API serving the same JSON as endpoints
    ├── requirements.txt
    └── README.md                 backend-specific docs
```

## Running the Site

No install, no build:

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000/index.html`. (Opening the file directly via double-click won't work — browsers block `fetch()` of local files over `file://`, so it needs to be served, even locally.)

## Running the Backend (optional)

```bash
cd backend
pip install -r requirements.txt

# CLI
cd analyzers
python mvp_analyzer.py --league nba
python mvp_analyzer.py --league mlb --division NL

# or the API
cd ..
python app.py
```

See `backend/README.md` for full endpoint docs.

## Data

All figures are real, pulled from official league sources and major outlets (NBA.com, NFL.com, MLB.com/BBWAA, ESPN, CBS Sports) as of each award's announcement date — NBA: May 2026, NFL: Feb 2026, MLB: Nov 2025. This is a point-in-time snapshot, not a live feed; each JSON file notes its source and date.

## What's Next

- Wire the site to the Flask API for live-updating data instead of a static snapshot
- Add historical seasons instead of just the current one per league
- Expand the terminal's command set (career stat lookups, head-to-head comparisons)

---

*Built by [Aathushan Kugendran](https://github.com/aathushankugendran)*