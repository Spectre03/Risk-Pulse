# RiskPulse — Monte Carlo Project Risk Simulator

RiskPulse runs Monte Carlo simulations to estimate project schedule and budget risk. The core implementation is in the `monte_carlo_risk/` folder.

Quick summary:
- Baseline risk by project type
- Feature scoring (built-before, third-party API, requirements clarity)
- 16-context questionnaire (Technical, Requirements, Integrations, Organizational)
- Default engine runs 10,000 trials and outputs probability distributions

Quick start:
1. python -m venv .venv && .venv\Scripts\activate
2. pip install -r requirements.txt  (if present)
3. python monte_carlo_risk\src\run_simulation.py --config monte_carlo_risk\config\example.yaml --trials 10000

Repository contents:
- monte_carlo_risk/  (code, notebooks, configs)
- data/  (optional input datasets)
- results/  (outputs; add to .gitignore)

Contributing: open issues and PRs; add tests under monte_carlo_risk/tests/.
