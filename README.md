# RiskPulse — Monte Carlo Project Risk Simulator

RiskPulse runs Monte Carlo simulations to estimate software project schedule and budget risk. Core code and examples are provided.

Key ideas
- Baseline risk by project type.
- Feature-level scoring (built-before, third-party API, requirements clarity).
- 16-question project context across Technical, Requirements, Integrations, Organizational.
- Monte Carlo engine runs N trials (default 10,000) to produce probability distributions for time and cost.

Included files (pushed)
- monte_carlo_risk/app.py
- monte_carlo_risk/pages/* (UI pages)
- monte_carlo_risk/simulator/* (core engine: monte_carlo.py, feature_scorer.py, distributions.py, complexity_analyzer.py)
- monte_carlo_risk/charts/* (plot helpers)
- monte_carlo_risk/utils/*
- monte_carlo_risk/requirements.txt

Quick start
1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r monte_carlo_risk\requirements.txt
4. python monte_carlo_risk\app.py  # or run specific scripts

Notes
- Do not commit results/ or virtual environments. Add to .gitignore if needed.
- For reproducible runs, set a random seed in configs.

Contributing
Open issues, create feature branches, and submit PRs. Add tests under monte_carlo_risk/tests/.
