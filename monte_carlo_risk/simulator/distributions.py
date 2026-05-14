def get_distribution_params(complexity_score, team_profile):
    senior = team_profile.get("senior", 0)
    mid = team_profile.get("mid", 0)
    junior = team_profile.get("junior", 0)
    total_devs = max(senior + mid + junior, 1)

    # Weighted daily productivity (story-point tasks/day per dev)
    # Senior ~ 2.5, Mid ~ 1.5, Junior ~ 0.7 story points per day
    weighted_productivity = (
        (senior * 2.5) + (mid * 1.5) + (junior * 0.7)
    ) / total_devs

    # Complexity reduces effective productivity
    base_productivity = weighted_productivity * (1 - complexity_score * 0.40)

    # Unfamiliar stack penalty
    familiar_stack = team_profile.get("familiar_stack", True)
    if not familiar_stack:
        base_productivity *= 0.72

    # New team coordination penalty
    worked_together = team_profile.get("worked_together", True)
    if not worked_together:
        base_productivity *= 0.85

    base_productivity = max(base_productivity, 0.3)

    # Bug rate: bugs per task batch (Poisson lambda)
    bug_lambda = 0.5 + (complexity_score * 3.5)
    if not familiar_stack:
        bug_lambda *= 1.35

    # Bug fix time (hours) — lognormal distribution
    bug_fix_mean = 2.0 + (complexity_score * 6.0)
    bug_fix_std = 1.5 + (complexity_score * 3.0)

    # Scope creep daily probability
    scope_creep_prob = 0.08 + (complexity_score * 0.35)

    # Team availability (triangular distribution)
    avail_min = 0.60
    avail_peak = 0.85 if not worked_together else 0.92
    avail_max = 1.0

    # Daily cost per developer ($)
    avg_daily_cost = (
        (senior * 600) + (mid * 400) + (junior * 250)
    ) / total_devs

    return {
        "productivity_mean": round(base_productivity, 3),
        "productivity_std": round(base_productivity * 0.30, 3),
        "bug_lambda": round(bug_lambda, 3),
        "bug_fix_mean": round(bug_fix_mean, 3),
        "bug_fix_std": round(bug_fix_std, 3),
        "scope_creep_prob": round(scope_creep_prob, 3),
        "avail_min": avail_min,
        "avail_peak": avail_peak,
        "avail_max": avail_max,
        "avg_daily_cost": round(avg_daily_cost, 2),
        "total_devs": total_devs,
    }
