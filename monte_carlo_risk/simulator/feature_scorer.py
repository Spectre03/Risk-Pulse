PROJECT_TYPE_BASE_RISK = {
    "Web App": 0.30,
    "Mobile App (Android only)": 0.40,
    "Mobile App (iOS only)": 0.40,
    "Mobile App (Both iOS & Android)": 0.65,
    "API / Backend Service": 0.35,
    "Desktop App": 0.45,
    "Data Pipeline / ML System": 0.60,
}

FEATURE_TYPE_BASE_COMPLEXITY = {
    "User Authentication & Registration": 0.30,
    "Payment Gateway Integration": 0.70,
    "Real-time Features (Chat / Live Updates)": 0.85,
    "Admin Dashboard": 0.35,
    "Search & Filters": 0.45,
    "File Upload & Management": 0.40,
    "Third-party API Integration": 0.60,
    "Data Analytics & Reporting": 0.55,
    "Email / SMS Notifications": 0.35,
    "Maps & Geolocation": 0.60,
    "Social Media Integration": 0.50,
    "Push Notifications": 0.40,
    "Multi-language / Localization": 0.50,
    "Role-based Access Control": 0.45,
    "Custom Feature (Unique to this project)": 0.75,
}


def score_feature(feature_type, built_before, third_party, requirements_clear):
    base = FEATURE_TYPE_BASE_COMPLEXITY.get(feature_type, 0.50)

    modifier = 0.0
    if not built_before:
        modifier += 0.20
    if third_party:
        modifier += 0.15
    if requirements_clear == "No":
        modifier += 0.25
    elif requirements_clear == "Partially":
        modifier += 0.12

    return round(min(base + modifier, 1.0), 2)


def estimate_tasks_from_features(features):
    """
    Each 'task' = one story-point-sized unit of work.
    Low-risk features are simpler; high-risk ones are large and uncertain.
    Calibrated so a medium 3-feature project fills ~60 days for a team of 5.
    """
    total = 0
    for f in features:
        score = f["score"]
        if score < 0.40:
            total += 20
        elif score < 0.70:
            total += 50
        else:
            total += 100
    return max(total, 15)


def calculate_project_complexity(project_type, features):
    base_risk = PROJECT_TYPE_BASE_RISK.get(project_type, 0.40)

    if not features:
        return round(base_risk, 2)

    scores = [f["score"] for f in features]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)

    complexity = (base_risk * 0.30) + (avg_score * 0.50) + (max_score * 0.20)
    return round(min(complexity, 1.0), 2)


def get_complexity_label(score):
    if score < 0.35:
        return "Low"
    elif score < 0.55:
        return "Medium"
    elif score < 0.75:
        return "High"
    else:
        return "Very High"


def get_high_risk_features(features, threshold=0.65):
    return [f for f in features if f["score"] >= threshold]
