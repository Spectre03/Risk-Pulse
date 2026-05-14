import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import numpy as np
import plotly.graph_objects as go
from utils.styling import BRAND_CSS

st.set_page_config(page_title="How It Works — RiskPulse", page_icon="📊",
                   layout="wide", initial_sidebar_state="expanded")
st.markdown(BRAND_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:1.2rem 0 .8rem;'>
        <div style='font-size:2rem'>📊</div>
        <div style='font-size:1.3rem;font-weight:800;color:#fff;letter-spacing:-.5px;'>RiskPulse</div>
        <div style='font-size:.75rem;color:#8aacd4;margin-top:2px;'>Project Risk Intelligence</div>
    </div>
    <hr style='border-color:rgba(255,255,255,0.1);margin:.5rem 0 1rem;'/>
    """, unsafe_allow_html=True)

# ── Page hero ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="rp-hero">
    <div class="rp-hero-title" style="font-size:2.2rem;">How RiskPulse Works</div>
    <div class="rp-hero-sub">
        The science behind Monte Carlo simulation, 6-dimension complexity scoring,
        and how they combine to give you an honest risk picture.
    </div>
</div>
""", unsafe_allow_html=True)

# ── SECTION 1: What is Monte Carlo ───────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">What is Monte Carlo Simulation?</div>', unsafe_allow_html=True)

c_left, c_right = st.columns([3, 2])
with c_left:
    st.markdown("""
Monte Carlo simulation is named after the famous casino in Monaco — because it works
by using **random chance, run thousands of times**, to model uncertain outcomes.

**The core idea:**

Instead of asking *"How long will this project take?"* and getting one optimistic guess,
Monte Carlo asks the same question 10,000 times — each time with slightly different
random conditions:

- Developer A is sick on day 12
- A bug takes 3 days instead of 3 hours
- The client requests 4 new features in week 5
- One junior dev is slower than average this sprint

After 10,000 runs, you don't get one answer. You get a **distribution** — a chart
showing all the possible outcomes and how likely each one is. This is honest.
This is what actually happens in real projects.
""")

with c_right:
    # Simple Monte Carlo demo chart
    rng = np.random.default_rng(42)
    samples = rng.normal(loc=65, scale=12, size=5000).clip(30, 120)
    fig = go.Figure(go.Histogram(
        x=samples, nbinsx=40,
        marker_color=["#2E75B6" if x <= 60 else "#d32f2f" for x in samples],
        opacity=0.85,
        hovertemplate="Duration: %{x:.0f} days<br>Count: %{y}<extra></extra>",
    ))
    fig.add_vline(x=60, line_dash="dash", line_color="#d32f2f", line_width=2,
                  annotation_text="  Deadline (60 days)", annotation_font_color="#d32f2f")
    fig.update_layout(
        title="Example: 5,000 simulated outcomes",
        xaxis_title="Project duration (days)",
        yaxis_title="Frequency",
        plot_bgcolor="#FAFAFA", paper_bgcolor="#FFFFFF",
        showlegend=False, height=320,
        margin=dict(t=50, b=40, l=40, r=20),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Each bar = a possible outcome. Red = missed deadline.")

st.divider()

# ── SECTION 2: Why not just estimate ─────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">Why Not Just Make an Estimate?</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
problems = [
    ("🙈", "Optimism Bias",
     "Humans systematically underestimate how long things take. We plan for the "
     "best case, not the realistic case. Monte Carlo forces you to account for "
     "the full range of what can go wrong."),
    ("📌", "Single-Point Estimates Lie",
     '"It will take 60 days" is not a probability — it is a wish. Monte Carlo '
     "gives you: '60 days has a 58% probability.' That is actionable."),
    ("🔗", "Risk Compounds",
     "If there are 10 uncertain things in your project and each has a 90% "
     "chance of going fine — the probability everything goes fine is 0.9^10 = 35%. "
     "Monte Carlo captures this compounding effect automatically."),
]
for col, (icon, title, body) in zip([c1, c2, c3], problems):
    with col:
        st.markdown(f'<div class="rp-card"><div class="rp-card-icon">{icon}</div>'
                    f'<div class="rp-card-title">{title}</div>'
                    f'<div class="rp-card-body">{body}</div></div>', unsafe_allow_html=True)

st.divider()

# ── SECTION 3: The 6 Dimensions ───────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">The 6-Dimension Complexity Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="rp-section-sub">Complexity is not a dropdown. RiskPulse derives it from 16 measurable factors across 6 dimensions.</div>', unsafe_allow_html=True)

dims = [
    ("🔧", "Technical", "22% weight",
     "Covers performance requirements (standard vs real-time), security and "
     "compliance obligations (GDPR, HIPAA, PCI), whether the team is using "
     "unfamiliar technology, how many mobile platforms are targeted, and whether "
     "offline support is needed.",
     ["Standard performance = low risk", "Real-time / ultra-low latency = very high risk",
      "New technology = +20% risk", "Compliance requirements = +40% risk"]),

    ("📋", "Requirements", "20% weight",
     "Measures how clear and stable requirements are, how many stakeholders "
     "can request changes, whether the domain is new to the team, and how "
     "likely mid-project change requests are.",
     ["Fully defined and frozen = 0% risk", "Vague / exploratory = 85% risk",
      "Every additional stakeholder increases risk", "High change likelihood = +30% risk"]),

    ("🔗", "Integration", "18% weight",
     "Scores the number of external APIs and third-party services, database "
     "complexity, whether data migration from an old system is needed, and "
     "whether the project must integrate with legacy or undocumented systems.",
     ["Each external API adds ~12% risk", "Data migration = +30% risk",
      "Legacy system integration = +25% risk", "Multiple databases = +20% risk"]),

    ("👥", "Team Fit", "18% weight",
     "Reflects the mismatch between team experience and project demands — "
     "the proportion of junior developers, whether the team has worked "
     "together before, tech stack familiarity, team size overhead, and "
     "remote-work coordination friction.",
     ["100% junior team = highest risk", "New team = +20% risk",
      "Unfamiliar stack = +30% risk", "Remote team = +10% risk"]),

    ("⚠️", "Feature Risk", "14% weight",
     "Derived directly from your feature list — the average risk score "
     "across all features, the score of the highest-risk feature, and "
     "the proportion of features rated high-risk.",
     ["Each feature is scored 0–100% from 3 questions",
      "Never built before = +20%", "Third-party dependency = +15%",
      "Unclear requirements = +25%"]),

    ("🏢", "Organizational", "8% weight",
     "Accounts for whether a Project Manager is assigned, how many approval "
     "stages exist before release, and how heavily the client is involved "
     "in the development process.",
     ["No PM = +30% risk", "Each extra approval stage = +12%",
      "High client involvement = +25% risk"]),
]

for icon, name, weight, desc, factors in dims:
    with st.expander(f"{icon}  {name}  —  {weight}", expanded=False):
        c_l, c_r = st.columns([3, 2])
        with c_l:
            st.markdown(f'<div class="hiw-box"><p>{desc}</p></div>', unsafe_allow_html=True)
        with c_r:
            st.markdown("**Score drivers:**")
            for f in factors:
                st.markdown(f"- {f}")

st.divider()

# ── SECTION 4: How dimensions feed simulation ─────────────────────────────────
st.markdown('<div class="rp-section-hdr">How Complexity Feeds the Simulation</div>', unsafe_allow_html=True)

st.markdown("""
Once the overall complexity score is calculated, it is used to **set the probability
distributions** that drive the Monte Carlo simulation. Higher complexity shifts
each distribution in the unfavourable direction.
""")

flow_items = [
    ("Overall Complexity Score", "0–100 weighted score from all 6 dimensions"),
    ("Developer Productivity", "Higher complexity → lower tasks/day → slower progress"),
    ("Bug Discovery Rate",     "Higher complexity → more bugs per task"),
    ("Bug Fix Time",           "Higher complexity → longer per-bug fix time (lognormal)"),
    ("Scope Creep Probability","Higher complexity → more likely new requirements are added"),
    ("Team Availability",      "Team Fit dimension directly adjusts availability distribution"),
]
for title, detail in flow_items:
    st.markdown(
        f'<div class="rp-step">'
        f'<div class="rp-step-num">→</div>'
        f'<div><div class="rp-step-title">{title}</div>'
        f'<div class="rp-step-body">{detail}</div></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.divider()

# ── SECTION 5: Reading the results ────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">Reading Your Results</div>', unsafe_allow_html=True)

results_guide = [
    ("On-Time Probability",
     "The percentage of the 10,000 simulations that finished on or before your deadline. "
     "≥70% = good, 50–70% = at risk, <50% = high risk."),
    ("On-Budget Probability",
     "The percentage of simulations that came in at or under your budget. Same thresholds apply."),
    ("Full Success Probability",
     "Simulations that were BOTH on time AND on budget. This is the most honest metric."),
    ("P10 / Median / P90",
     "P10 = best plausible outcome (10% chance of being this good or better). "
     "Median = the 50/50 outcome. P90 = worst plausible outcome (90% chance of being no worse than this)."),
    ("Complexity Radar",
     "A spider chart with 6 arms — one per dimension. Longer arms mean higher complexity "
     "in that dimension. The shape tells you WHERE your project's complexity is concentrated."),
    ("Sensitivity / Tornado Chart",
     "Shows which risk factor, if it gets 30% worse, adds the most days to your project. "
     "The longest bar is what you should focus your mitigation effort on first."),
    ("Convergence Chart",
     "Proof of statistical validity. The probability estimate jumps around with few "
     "simulations but converges to a stable number. A flat line at the end = reliable result."),
]

for title, explanation in results_guide:
    st.markdown(
        f'<div class="hiw-box"><h4>{title}</h4><p>{explanation}</p></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    if st.button("Go to the Simulator →", type="primary", use_container_width=True):
        st.switch_page("pages/1_Simulator.py")
