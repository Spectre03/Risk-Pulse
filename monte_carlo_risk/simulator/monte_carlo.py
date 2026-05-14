import numpy as np
import pandas as pd


def run_simulation(
    total_tasks,
    deadline_days,
    budget,
    params,
    n_simulations=10000,
    has_qa=True,
    has_pm=True,
):
    rng = np.random.default_rng(seed=42)
    total_devs = params["total_devs"]
    hours_per_day = 8

    records = []

    for _ in range(n_simulations):
        tasks_left = float(total_tasks)
        day = 0
        total_cost = 0.0
        bugs_pending = 0
        max_days = int(deadline_days * 3.5)

        while tasks_left > 0 and day < max_days:
            # How many devs are available today
            # Clamp peak so it always stays within [min, max] — prevents
            # ValueError when sensitivity analysis inflates avail_peak > avail_max
            _amin  = params["avail_min"]
            _amax  = params["avail_max"]
            _apeak = float(np.clip(params["avail_peak"], _amin + 0.001, _amax - 0.001))
            availability = float(np.clip(
                rng.triangular(_amin, _apeak, _amax),
                0.40, 1.0
            ))
            active_devs = max(1, round(total_devs * availability))

            # Productivity of each dev today
            productivity = max(0.2, float(rng.normal(
                params["productivity_mean"],
                params["productivity_std"]
            )))

            # Raw tasks completed
            tasks_done = active_devs * productivity

            # New bugs introduced proportional to tasks done
            new_bugs = int(rng.poisson(
                params["bug_lambda"] * (tasks_done / max(total_tasks, 1)) * 2
            ))
            bugs_pending += new_bugs

            # Fix some bugs today (takes time away from features)
            if bugs_pending > 0:
                bugs_fixed = min(bugs_pending, int(rng.poisson(1.8)) + 1)
                fix_hours = 0.0
                for _ in range(bugs_fixed):
                    h = float(rng.lognormal(
                        mean=np.log(max(0.5, params["bug_fix_mean"])),
                        sigma=0.55
                    ))
                    fix_hours += max(0.25, h)
                task_loss = fix_hours / hours_per_day
                tasks_done = max(0.0, tasks_done - task_loss)
                bugs_pending -= bugs_fixed

            # Random scope creep
            if rng.random() < (params["scope_creep_prob"] / 20.0):
                tasks_left += float(rng.integers(1, 5))

            tasks_left = max(0.0, tasks_left - tasks_done)

            # Daily cost
            daily_cost = active_devs * params["avg_daily_cost"]
            if has_pm:
                daily_cost *= 1.12
            total_cost += daily_cost

            day += 1

        # QA phase
        if has_qa:
            qa_days = int(rng.integers(2, max(3, round(day * 0.12) + 1)))
            day += qa_days
            total_cost += qa_days * total_devs * params["avg_daily_cost"] * 0.40

        records.append({
            "days": day,
            "cost": round(total_cost, 2),
            "on_time": day <= deadline_days,
            "on_budget": total_cost <= budget,
        })

    return pd.DataFrame(records)


def sensitivity_analysis(base_params, total_tasks, deadline_days, budget,
                         n_simulations=3000, has_qa=True, has_pm=True):
    base_df = run_simulation(
        total_tasks, deadline_days, budget, base_params,
        n_simulations, has_qa, has_pm
    )
    base_mean = base_df["days"].mean()

    factors = {
        "Developer Productivity": "productivity_mean",
        "Bug Discovery Rate": "bug_lambda",
        "Bug Fix Time": "bug_fix_mean",
        "Scope Creep Probability": "scope_creep_prob",
        "Team Availability": "avail_peak",
        "Daily Team Cost": "avg_daily_cost",
    }

    impacts = {}
    for label, key in factors.items():
        worse_params = dict(base_params)
        worse_params[key] = base_params[key] * 1.30

        worse_df = run_simulation(
            total_tasks, deadline_days, budget, worse_params,
            n_simulations, has_qa, has_pm
        )
        impact = worse_df["days"].mean() - base_mean
        impacts[label] = round(impact, 2)

    sorted_impacts = dict(
        sorted(impacts.items(), key=lambda x: abs(x[1]), reverse=True)
    )
    return sorted_impacts
