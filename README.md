# RiskPulse — Monte Carlo Project Risk Simulator

RiskPulse applies Monte Carlo simulation to software project risk assessment. It converts fuzzy single-point estimates into probability distributions for schedule and budget outcomes.

Overview
- Baseline risk by project type (e.g., web app vs cross-platform mobile).
- Feature-level scoring: each feature answers 3 questions (built-before, third-party API, requirements clarity).
- Project context: 16 questions across Technical, Requirements, Integrations, Organizational factors.
- Simulation engine runs default 10,000 trials, sampling from selected distributions to produce outcome distributions and summary metrics.

Included files (copied to repo root)
- app.py — UI entrypoint
- requirements.txt — Python dependencies
- pages/ — Streamlit pages (home, simulator, how_it_works, about)
- simulator/ — core engine modules (monte_carlo.py, feature_scorer.py, distributions.py, complexity_analyzer.py)
- charts/ — plotting helpers (radar, histogram, tornado, convergence)
- utils/ — styling and utilities

Quick start
1. Create a virtual environment and activate it:

   python -m venv .venv
   .venv\Scripts\activate  # Windows

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app (Streamlit):

   streamlit run app.py

Running simulations
- Use `simulator/monte_carlo.py` or the app's simulator page.
- For quick iteration, reduce trials (e.g., --trials 10000).
- Save outputs to a `results/` folder (add to .gitignore).

Reproducibility
- Set explicit random seeds in the config or call `numpy.random.seed()` before runs.
- Save `metadata.json` with parameter settings for each experiment.

Contributing
- Open issues and submit PRs.
- Add tests under `simulator/tests/` and document new modules.

License
- Add a LICENSE file (e.g., MIT) if open-sourcing.

Contact
- Update maintainers and contact information as needed.
