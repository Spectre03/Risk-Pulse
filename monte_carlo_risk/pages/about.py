import streamlit as st

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="rp-hero-sm">
    <div class="rp-hero-sm-title">ℹ️ About RiskPulse</div>
    <div class="rp-hero-sm-sub">
        A Monte Carlo simulation tool built for software project risk analysis —
        developed as part of a Simulation &amp; Modeling course project.
    </div>
</div>
""", unsafe_allow_html=True)

# ── The Problem ───────────────────────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">The Problem We Are Solving</div>', unsafe_allow_html=True)

c_left, c_right = st.columns([3, 2])
with c_left:
    st.markdown("""
Software projects fail at an alarming rate. The Standish Group CHAOS Report, which
has tracked project outcomes since 1994, consistently finds that **only about 31%
of software projects are delivered on time and within budget**.

The other 69%? Late, over budget, cancelled, or all three.

The root cause is rarely incompetence. It is **uncertainty that was never measured**.
Teams make single-point estimates ("it will take 60 days") when what they should say
is "there is a 58% probability it takes 60 days or less, and a 20% chance it takes
more than 90 days."

**RiskPulse was built to make that honest answer easy to produce** — for any project,
at any scale, using classical Monte Carlo simulation enhanced by a modern,
multi-dimensional complexity scoring engine.
""")

with c_right:
    st.markdown("""
    <div style="background:#fff8e8;border:1px solid #ffe082;border-radius:14px;padding:1.4rem;">
        <div style="font-size:2.5rem;font-weight:800;color:#e65100;text-align:center;">69%</div>
        <div style="text-align:center;color:#333;font-size:.9rem;margin-top:.3rem;">
            of software projects fail to meet their deadline and budget
        </div>
        <hr style="border-color:#ffe082;margin:1rem 0;">
        <div style="font-size:1.6rem;font-weight:800;color:#c62828;text-align:center;">31%</div>
        <div style="text-align:center;color:#333;font-size:.9rem;margin-top:.3rem;">
            succeed — and RiskPulse helps you be in that 31%
        </div>
        <div style="text-align:center;margin-top:.8rem;font-size:.75rem;color:#888;">
            Source: Standish Group CHAOS Report
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ── What Makes RiskPulse Different ────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">What Makes RiskPulse Different</div>', unsafe_allow_html=True)

diff = [
    ("🔬", "Complexity Is Derived, Not Guessed",
     "Most tools ask you to rate complexity as Low/Medium/High. RiskPulse derives "
     "complexity from 16 measurable factors across 6 dimensions — features, technical "
     "requirements, integrations, team fit, requirements clarity, and organizational "
     "context. You describe reality; the tool calculates the risk."),
    ("📊", "Full Probability Distributions, Not Point Estimates",
     "Instead of saying 'the project will take 60 days', RiskPulse runs 10,000 "
     "simulations and shows you the full distribution — best case, median, worst case, "
     "and exact probabilities for hitting your deadline and budget."),
    ("🌪️", "Sensitivity Analysis Tells You What to Fix",
     "The tornado chart identifies which risk factor — bug rate, scope creep, "
     "team availability — has the biggest impact on your timeline. This turns "
     "the simulation into an actionable decision-making tool, not just a number."),
    ("🕸️", "Visual Complexity Radar",
     "A spider chart instantly shows which dimensions of your project are most "
     "complex. At a glance you can see if your risk is concentrated in team fit, "
     "integrations, or unclear requirements — and focus accordingly."),
]

for icon, title, body in diff:
    st.markdown(
        f'<div class="dim-card" style="margin-bottom:.6rem;">'
        f'<div style="font-size:1.4rem;margin-bottom:.3rem;">{icon}</div>'
        f'<div style="font-weight:700;color:#1F3864;margin-bottom:.3rem;">{title}</div>'
        f'<div style="color:#444;font-size:.9rem;line-height:1.6;">{body}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.divider()

# ── Tech Stack ────────────────────────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">Technology Stack</div>', unsafe_allow_html=True)

st.markdown("""
<div style="margin-bottom:1rem;">
    <b>Simulation Core</b><br>
    <span class="tech-badge">Python 3</span>
    <span class="tech-badge">NumPy</span>
    <span class="tech-badge">Pandas</span>
    <span class="tech-badge">SciPy</span>
</div>
<div style="margin-bottom:1rem;">
    <b>Visualisation</b><br>
    <span class="tech-badge">Plotly</span>
    <span class="tech-badge">Streamlit</span>
</div>
<div style="margin-bottom:1rem;">
    <b>Statistical Distributions Used</b><br>
    <span class="tech-badge">Normal (productivity)</span>
    <span class="tech-badge">Poisson (bug rate)</span>
    <span class="tech-badge">Lognormal (bug fix time)</span>
    <span class="tech-badge">Triangular (availability)</span>
    <span class="tech-badge">Bernoulli (scope creep)</span>
</div>
<div>
    <b>Deployment</b><br>
    <span class="tech-badge">Streamlit Cloud (shareable URL)</span>
    <span class="tech-badge">GitHub</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Simulation Methodology ────────────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">Simulation Methodology</div>', unsafe_allow_html=True)

st.markdown("""
Each simulation run models **one possible version of your project** from day 0 to
completion. Here is what happens inside each of the 10,000 runs:
""")

method_steps = [
    ("Day Loop Begins",
     "The simulation advances day by day until all tasks are complete or 3.5× "
     "the deadline is reached (a hard cap to prevent infinite loops)."),
    ("Team Availability Sampled",
     "Each day, team availability is sampled from a **Triangular distribution** "
     "with your team's min/peak/max availability. This models sick days, leave, "
     "and coordination overhead."),
    ("Productivity Sampled",
     "Each active developer's daily output is sampled from a **Normal distribution** "
     "with mean and std derived from seniority mix and complexity score."),
    ("Bugs Introduced",
     "New bugs are sampled from a **Poisson distribution** proportional to tasks "
     "completed. Higher complexity = higher bug rate."),
    ("Bugs Fixed",
     "A random number of bugs are fixed each day. Each fix consumes hours sampled "
     "from a **Lognormal distribution** — most bugs are quick, but some take days."),
    ("Scope Creep Event",
     "Each day has a small probability (derived from complexity) of a scope creep "
     "event — new tasks are added to the backlog via a **Bernoulli trial**."),
    ("Cost Accumulated",
     "Daily cost = active developers × average daily rate (derived from seniority "
     "mix), with a PM overhead multiplier if a PM is assigned."),
    ("QA Phase Added",
     "If a QA phase is enabled, a random QA duration (~12% of development days) "
     "is added at the end of each simulation run."),
]

for i, (title, detail) in enumerate(method_steps, start=1):
    st.markdown(
        f'<div class="rp-step">'
        f'<div class="rp-step-num">{i}</div>'
        f'<div><div class="rp-step-title">{title}</div>'
        f'<div class="rp-step-body">{detail}</div></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.divider()

# ── Course Context ────────────────────────────────────────────────────────────
st.markdown('<div class="rp-section-hdr">Course & Project Context</div>', unsafe_allow_html=True)
st.markdown("""
<div class="dim-card">
    <div style="font-weight:700;color:#1F3864;margin-bottom:.5rem;">
        Simulation &amp; Modeling — Group 4
    </div>
    <div style="color:#444;font-size:.9rem;line-height:1.7;">
        <b>Topic assigned:</b> Monte Carlo Simulation in Risk Management<br>
        <b>Base example (from course PDF):</b> Simulate risks for a mobile app development project<br>
        <b>What we built:</b> A fully functional, multi-page web application that extends the base
        concept into a real decision-making tool — with a 6-dimension complexity engine,
        16 context factors, sensitivity analysis, and interactive visual analytics.<br>
        <b>Presentation time:</b> 10 minutes
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    if st.button("Launch the Simulator →", type="primary", use_container_width=True):
        st.switch_page("pages/simulator.py")
