"""
Derives a multi-dimensional complexity profile from project context answers.
Each dimension is scored 0.0 – 1.0. The weighted average feeds the simulation.
"""


DIMENSIONS = [
    "Technical",
    "Requirements",
    "Integration",
    "Team Fit",
    "Feature Risk",
    "Organizational",
]

DIMENSION_WEIGHTS = {
    "Technical":      0.22,
    "Requirements":   0.20,
    "Integration":    0.18,
    "Team Fit":       0.18,
    "Feature Risk":   0.14,
    "Organizational": 0.08,
}


# ── Individual dimension scorers ─────────────────────────────────────────────

def score_technical(context: dict) -> float:
    score = 0.0

    perf = context.get("performance_req", "Standard")
    score += {"Standard": 0.0, "High Performance": 0.3, "Real-time / Ultra-low latency": 0.55}[perf]

    security = context.get("security_req", "Basic auth only")
    score += {
        "Basic auth only": 0.0,
        "Role-based access control": 0.15,
        "Compliance required (HIPAA / GDPR / PCI)": 0.40,
    }[security]

    stack_new = context.get("new_tech_involved", False)
    if stack_new:
        score += 0.25

    mobile_platforms = context.get("mobile_platforms", 0)
    score += min(mobile_platforms * 0.10, 0.20)

    offline = context.get("offline_support", False)
    if offline:
        score += 0.10

    return min(round(score, 3), 1.0)


def score_requirements(context: dict) -> float:
    score = 0.0

    clarity = context.get("req_clarity_overall", "Partially defined")
    score += {
        "Fully defined and frozen": 0.0,
        "Mostly defined":           0.20,
        "Partially defined":        0.40,
        "Still being discussed":    0.65,
        "Vague / exploratory":      0.85,
    }[clarity]

    stakeholders = context.get("num_stakeholders", 2)
    if stakeholders <= 2:
        score += 0.0
    elif stakeholders <= 5:
        score += 0.15
    else:
        score += 0.30

    domain_new = context.get("new_domain", False)
    if domain_new:
        score += 0.20

    change_risk = context.get("change_request_risk", "Medium")
    score += {"Low": 0.0, "Medium": 0.15, "High": 0.30}[change_risk]

    return min(round(score, 3), 1.0)


def score_integration(context: dict) -> float:
    score = 0.0

    num_apis = context.get("num_external_apis", 0)
    score += min(num_apis * 0.12, 0.45)

    data_migration = context.get("data_migration", False)
    if data_migration:
        score += 0.30

    db_type = context.get("database_complexity", "Simple relational")
    score += {
        "Simple relational":             0.0,
        "Multiple databases":            0.20,
        "NoSQL / unstructured":          0.15,
        "Data warehouse / analytics DB": 0.30,
    }[db_type]

    legacy = context.get("legacy_integration", False)
    if legacy:
        score += 0.25

    return min(round(score, 3), 1.0)


def score_team_fit(team_profile: dict, project_type: str, context: dict) -> float:
    score = 0.0

    senior = team_profile.get("senior", 0)
    mid    = team_profile.get("mid",    0)
    junior = team_profile.get("junior", 0)
    total  = max(senior + mid + junior, 1)
    junior_ratio = junior / total

    score += junior_ratio * 0.40

    if not team_profile.get("worked_together", True):
        score += 0.20

    if not team_profile.get("familiar_stack", True):
        score += 0.30

    # Large teams have more coordination overhead
    if total > 8:
        score += 0.15
    elif total > 5:
        score += 0.08

    remote = context.get("remote_team", False)
    if remote:
        score += 0.10

    return min(round(score, 3), 1.0)


def score_feature_risk(features: list) -> float:
    if not features:
        return 0.3

    scores = [f["score"] for f in features]
    avg    = sum(scores) / len(scores)
    max_s  = max(scores)
    high_risk_count = sum(1 for s in scores if s >= 0.70)
    high_risk_ratio = high_risk_count / len(scores)

    combined = (avg * 0.50) + (max_s * 0.30) + (high_risk_ratio * 0.20)
    return round(min(combined, 1.0), 3)


def score_organizational(context: dict, has_pm: bool) -> float:
    score = 0.0

    if not has_pm:
        score += 0.30

    approval_stages = context.get("approval_stages", 1)
    score += min((approval_stages - 1) * 0.12, 0.35)

    client_involvement = context.get("client_involvement", "Low")
    score += {"Low": 0.0, "Medium": 0.10, "High — client reviews every sprint": 0.25}[client_involvement]

    return min(round(score, 3), 1.0)


# ── Master function ──────────────────────────────────────────────────────────

def compute_full_complexity(
    features: list,
    project_type: str,
    team_profile: dict,
    context: dict,
    has_pm: bool = True,
) -> dict:
    tech  = score_technical(context)
    reqs  = score_requirements(context)
    integ = score_integration(context)
    tfit  = score_team_fit(team_profile, project_type, context)
    feat  = score_feature_risk(features)
    org   = score_organizational(context, has_pm)

    dimension_scores = {
        "Technical":      tech,
        "Requirements":   reqs,
        "Integration":    integ,
        "Team Fit":       tfit,
        "Feature Risk":   feat,
        "Organizational": org,
    }

    overall = sum(
        dimension_scores[d] * DIMENSION_WEIGHTS[d]
        for d in DIMENSION_WEIGHTS
    )
    overall = round(min(overall, 1.0), 3)

    return {
        "dimensions": dimension_scores,
        "overall":    overall,
        "label":      _label(overall),
        "drivers":    _top_drivers(dimension_scores),
    }


def _label(score: float) -> str:
    if score < 0.25:
        return "Low"
    elif score < 0.45:
        return "Medium"
    elif score < 0.65:
        return "High"
    else:
        return "Very High"


def _top_drivers(dimension_scores: dict) -> list:
    weighted = {
        d: round(dimension_scores[d] * DIMENSION_WEIGHTS[d], 4)
        for d in dimension_scores
    }
    sorted_dims = sorted(weighted.items(), key=lambda x: x[1], reverse=True)
    return [d for d, _ in sorted_dims[:3]]
