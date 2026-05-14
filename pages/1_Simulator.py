import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.styling import BRAND_CSS
from simulator.feature_scorer import (
    PROJECT_TYPE_BASE_RISK, FEATURE_TYPE_BASE_COMPLEXITY,
    score_feature, estimate_tasks_from_features, get_high_risk_features,
)
from simulator.complexity_analyzer import compute_full_complexity
from simulator.distributions import get_distribution_params
from simulator.monte_carlo import run_simulation, sensitivity_analysis
from charts.histogram import plot_duration_histogram, plot_cost_histogram
from charts.tornado import plot_tornado_chart
from charts.convergence import plot_convergence_chart
from charts.radar import plot_complexity_radar, plot_dimension_bars

st.set_page_config(page_title="Simulator — RiskPulse", page_icon="📊",
                   layout="wide", initial_sidebar_state="expanded")
st.markdown(BRAND_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:1.2rem 0 .8rem;'>
        <div style='font-size:2rem'>📊</div>
        <div style='font-size:1.3rem;font-weight:800;color:#fff;letter-spacing:-.5px;'>RiskPulse</div>
        <div style='font-size:.75rem;color:#8aacd4;margin-top:2px;'>Project Risk Intelligence</div>
    </div>
    <hr style='border-color:rgba(255,255,255,0.1);margin:.5rem 0 1rem;'/>
    """, unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
DEFAULTS = {
    "step": 1, "project_info": {}, "features": [], "context": {},
    "team_profile": {}, "resources": {}, "complexity_result": None,
    "results": None, "params": None, "sensitivity": None,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#1F3864,#2E75B6);
            border-radius:14px;padding:1.8rem 2.2rem;margin-bottom:1.5rem;">
    <div style="font-size:1.8rem;font-weight:800;color:#fff;margin-bottom:.3rem;">
        Project Risk Simulator
    </div>
    <div style="color:#c8dbf5;font-size:.95rem;">
        Fill in your project details across 5 steps — RiskPulse will run
        10,000 Monte Carlo simulations and deliver a full risk report.
    </div>
</div>
""", unsafe_allow_html=True)

# ── Progress indicator ────────────────────────────────────────────────────────
STEPS = ["1 · Project", "2 · Features", "3 · Context", "4 · Team", "5 · Resources", "Results"]
cols = st.columns(len(STEPS))
for i, (col, lbl) in enumerate(zip(cols, STEPS), start=1):
    with col:
        if i < st.session_state.step:
            st.markdown(f"<div style='text-align:center;color:#388e3c;font-weight:600;font-size:.85rem;'>✅ {lbl}</div>", unsafe_allow_html=True)
        elif i == st.session_state.step:
            st.markdown(f"<div style='text-align:center;color:#2E75B6;font-weight:700;font-size:.85rem;background:#e8f0fe;border-radius:20px;padding:3px 0;'>🔵 {lbl}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align:center;color:#aaa;font-size:.85rem;'>⬜ {lbl}</div>", unsafe_allow_html=True)
st.divider()


# ═══════════════ STEP 1 — Project Info ══════════════════════════════════════
if st.session_state.step == 1:
    st.markdown('<div class="step-hdr">Step 1 — What Are You Building?</div>', unsafe_allow_html=True)
    st.markdown('<div class="note-box">Name your project and choose its type. The project type carries a baseline risk — a cross-platform mobile app is inherently more complex than a simple web app.</div>', unsafe_allow_html=True)

    name = st.text_input("Project Name", value=st.session_state.project_info.get("name", ""),
                         placeholder="e.g.  E-Commerce Mobile App")
    ptype = st.selectbox("Project Type", list(PROJECT_TYPE_BASE_RISK.keys()))
    st.caption(f"Base risk for **{ptype}**: `{int(PROJECT_TYPE_BASE_RISK[ptype]*100)}%`")

    st.markdown("")
    if st.button("Next →", type="primary", disabled=not name.strip()):
        st.session_state.project_info = {"name": name.strip(), "type": ptype}
        st.session_state.step = 2; st.rerun()


# ═══════════════ STEP 2 — Features ══════════════════════════════════════════
elif st.session_state.step == 2:
    st.markdown('<div class="step-hdr">Step 2 — Features Your Project Needs</div>', unsafe_allow_html=True)
    st.markdown('<div class="note-box">Add each major feature. Answer 3 questions per feature — this is how RiskPulse calculates real feature-level risk instead of relying on a vague "complexity" dropdown.</div>', unsafe_allow_html=True)

    if st.session_state.features:
        st.markdown(f"**{len(st.session_state.features)} feature(s) added:**")
        for i, f in enumerate(st.session_state.features):
            s = f["score"]
            cls = "risk-low" if s < .40 else ("risk-med" if s < .70 else "risk-high")
            lbl = "Low Risk" if s < .40 else ("Medium Risk" if s < .70 else "High Risk")
            c1, c2, c3 = st.columns([5, 2, 1])
            with c1: st.markdown(f"**{i+1}. {f['name']}**")
            with c2: st.markdown(f'<span class="{cls}">{lbl} ({int(s*100)}%)</span>', unsafe_allow_html=True)
            with c3:
                if st.button("✕", key=f"del_{i}"):
                    st.session_state.features.pop(i); st.rerun()
        st.caption(f"Estimated total work units: **~{estimate_tasks_from_features(st.session_state.features)}**")
        st.divider()

    st.markdown("**Add a Feature:**")
    c1, c2 = st.columns(2)
    with c1: ftype = st.selectbox("Feature Type", list(FEATURE_TYPE_BASE_COMPLEXITY.keys()), key="ft_type")
    with c2: fname = st.text_input("Custom name (optional)", placeholder="e.g.  Vendor Module", key="ft_name")

    c1, c2, c3 = st.columns(3)
    with c1: built  = st.radio("Built this before?",      ["Yes", "No"],                  horizontal=True, key="ft_built")
    with c2: thirdp = st.radio("Third-party API/service?", ["Yes", "No"],                  horizontal=True, key="ft_3p")
    with c3: reqc   = st.radio("Requirements clear?",      ["Yes", "Partially", "No"],     horizontal=True, key="ft_req")

    if st.button("+ Add Feature", type="secondary"):
        n = fname.strip() or ftype
        s = score_feature(ftype, built == "Yes", thirdp == "Yes", reqc)
        st.session_state.features.append({
            "name": n, "type": ftype, "score": s,
            "built_before": built=="Yes", "third_party": thirdp=="Yes", "req_clear": reqc,
        }); st.rerun()

    st.divider()
    cb, cn = st.columns(2)
    with cb:
        if st.button("← Back"): st.session_state.step = 1; st.rerun()
    with cn:
        if st.button("Next →", type="primary", disabled=not st.session_state.features):
            st.session_state.step = 3; st.rerun()


# ═══════════════ STEP 3 — Project Context ════════════════════════════════════
elif st.session_state.step == 3:
    st.markdown('<div class="step-hdr">Step 3 — Project Context & Deep Complexity Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="note-box">These 16 questions go beyond features. They cover your technical environment, requirement stability, integrations, and organisational dynamics — the factors that <b>actually drive</b> real-world project complexity.</div>', unsafe_allow_html=True)

    ctx = st.session_state.context

    with st.expander("Technical Requirements", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            perf = st.selectbox("Performance requirements",
                ["Standard", "High Performance", "Real-time / Ultra-low latency"],
                index=["Standard","High Performance","Real-time / Ultra-low latency"].index(ctx.get("performance_req","Standard")))
        with c2:
            sec = st.selectbox("Security / Compliance",
                ["Basic auth only","Role-based access control","Compliance required (HIPAA / GDPR / PCI)"],
                index=["Basic auth only","Role-based access control","Compliance required (HIPAA / GDPR / PCI)"].index(ctx.get("security_req","Basic auth only")))
        c1, c2, c3 = st.columns(3)
        with c1: new_tech   = st.radio("New technology the team has never used?", ["Yes","No"], index=0 if ctx.get("new_tech_involved") else 1, horizontal=True)
        with c2: mob_plat   = st.number_input("Mobile platforms (0=web only, 1=iOS or Android, 2=both)", 0, 2, ctx.get("mobile_platforms",0))
        with c3: offline    = st.radio("App must work offline?", ["Yes","No"], index=0 if ctx.get("offline_support") else 1, horizontal=True)

    with st.expander("Requirements Stability", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            req_c = st.selectbox("Overall requirements clarity",
                ["Fully defined and frozen","Mostly defined","Partially defined","Still being discussed","Vague / exploratory"],
                index=["Fully defined and frozen","Mostly defined","Partially defined","Still being discussed","Vague / exploratory"].index(ctx.get("req_clarity_overall","Partially defined")))
        with c2:
            n_stake = st.number_input("Stakeholders who can request changes", 1, 30, ctx.get("num_stakeholders",2))
        c1, c2 = st.columns(2)
        with c1: new_dom    = st.radio("Domain new to the team?",                  ["Yes","No"],          index=0 if ctx.get("new_domain") else 1, horizontal=True)
        with c2: change_r   = st.radio("Mid-project requirement change likelihood",["Low","Medium","High"],index=["Low","Medium","High"].index(ctx.get("change_request_risk","Medium")), horizontal=True)

    with st.expander("Integrations & Data", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1: n_apis   = st.number_input("External APIs / third-party services", 0, 20, ctx.get("num_external_apis",0))
        with c2:
            db_type = st.selectbox("Database complexity",
                ["Simple relational","Multiple databases","NoSQL / unstructured","Data warehouse / analytics DB"],
                index=["Simple relational","Multiple databases","NoSQL / unstructured","Data warehouse / analytics DB"].index(ctx.get("database_complexity","Simple relational")))
        with c3: data_mig = st.radio("Data migration from old system?", ["Yes","No"], index=0 if ctx.get("data_migration") else 1, horizontal=True)
        legacy = st.radio("Integration with legacy / undocumented system?", ["Yes","No"], index=0 if ctx.get("legacy_integration") else 1, horizontal=True)

    with st.expander("Organisational Factors", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1: approvals = st.number_input("Approval stages before release", 1, 10, ctx.get("approval_stages",1))
        with c2:
            client_inv = st.selectbox("Client involvement during development",
                ["Low","Medium","High — client reviews every sprint"],
                index=["Low","Medium","High — client reviews every sprint"].index(ctx.get("client_involvement","Low")))
        with c3: remote   = st.radio("Team fully or partially remote?", ["Yes","No"], index=0 if ctx.get("remote_team") else 1, horizontal=True)

    st.divider()
    cb, cn = st.columns(2)
    with cb:
        if st.button("← Back"): st.session_state.step = 2; st.rerun()
    with cn:
        if st.button("Next →", type="primary"):
            st.session_state.context = {
                "performance_req": perf, "security_req": sec,
                "new_tech_involved": new_tech=="Yes", "mobile_platforms": int(mob_plat),
                "offline_support": offline=="Yes", "req_clarity_overall": req_c,
                "num_stakeholders": int(n_stake), "new_domain": new_dom=="Yes",
                "change_request_risk": change_r, "num_external_apis": int(n_apis),
                "database_complexity": db_type, "data_migration": data_mig=="Yes",
                "legacy_integration": legacy=="Yes", "approval_stages": int(approvals),
                "client_involvement": client_inv, "remote_team": remote=="Yes",
            }
            st.session_state.step = 4; st.rerun()


# ═══════════════ STEP 4 — Team ═══════════════════════════════════════════════
elif st.session_state.step == 4:
    st.markdown('<div class="step-hdr">Step 4 — Your Team</div>', unsafe_allow_html=True)
    st.markdown('<div class="note-box">Team composition determines speed, bug rate, and coordination overhead. A junior-heavy team on unfamiliar tech produces a very different risk profile than a senior team.</div>', unsafe_allow_html=True)

    tp = st.session_state.team_profile
    c1, c2, c3 = st.columns(3)
    with c1: senior = st.number_input("Senior Developers (5+ yrs)",  0, 30, tp.get("senior",1))
    with c2: mid    = st.number_input("Mid-level Developers (2–5 yrs)", 0, 30, tp.get("mid",2))
    with c3: junior = st.number_input("Junior Developers (0–2 yrs)", 0, 30, tp.get("junior",1))

    total = int(senior + mid + junior)
    if total:
        st.caption(f"Team of **{total}** — {int(senior/total*100)}% senior / {int(mid/total*100)}% mid / {int(junior/total*100)}% junior")

    c1, c2 = st.columns(2)
    with c1: worked = st.radio("Team worked together before?", ["Yes","No"], horizontal=True)
    with c2: fstack = st.radio("Tech stack familiar to team?", ["Yes","Partially","No"], horizontal=True)

    st.divider()
    cb, cn = st.columns(2)
    with cb:
        if st.button("← Back"): st.session_state.step = 3; st.rerun()
    with cn:
        if st.button("Next →", type="primary", disabled=total==0):
            st.session_state.team_profile = {
                "senior": int(senior), "mid": int(mid), "junior": int(junior),
                "worked_together": worked=="Yes", "familiar_stack": fstack=="Yes",
            }
            st.session_state.step = 5; st.rerun()


# ═══════════════ STEP 5 — Resources ═══════════════════════════════════════════
elif st.session_state.step == 5:
    st.markdown('<div class="step-hdr">Step 5 — Budget, Deadline & Run</div>', unsafe_allow_html=True)
    st.markdown('<div class="note-box">Set your hard constraints. RiskPulse will tell you the probability of meeting each one and show the realistic range of outcomes.</div>', unsafe_allow_html=True)

    res = st.session_state.resources
    c1, c2 = st.columns(2)
    with c1: budget   = st.number_input("Total Budget ($)",           1_000, 10_000_000, res.get("budget",80_000),   1_000, format="%d")
    with c2: deadline = st.number_input("Deadline (days from today)", 7,     730,         res.get("deadline",90),    5)

    c1, c2, c3 = st.columns(3)
    with c1: has_qa  = st.radio("Dedicated QA / Testing phase?", ["Yes","No"], horizontal=True)
    with c2: has_pm  = st.radio("Project Manager assigned?",     ["Yes","No"], horizontal=True)
    with c3: n_sims  = st.select_slider("Simulations to run", [1_000,5_000,10_000,20_000], 10_000)

    st.divider()
    cb, cr = st.columns(2)
    with cb:
        if st.button("← Back"): st.session_state.step = 4; st.rerun()
    with cr:
        if st.button("Run Simulation →", type="primary"):
            st.session_state.resources = {
                "budget": int(budget), "deadline": int(deadline),
                "has_qa": has_qa=="Yes", "has_pm": has_pm=="Yes", "n_sims": int(n_sims),
            }
            with st.spinner("Analysing complexity and running Monte Carlo simulations..."):
                cx = compute_full_complexity(
                    features=st.session_state.features,
                    project_type=st.session_state.project_info["type"],
                    team_profile=st.session_state.team_profile,
                    context=st.session_state.context,
                    has_pm=has_pm=="Yes",
                )
                st.session_state.complexity_result = cx

                params = get_distribution_params(cx["overall"], st.session_state.team_profile)
                st.session_state.params = params

                total_tasks = estimate_tasks_from_features(st.session_state.features)

                df = run_simulation(
                    total_tasks=total_tasks, deadline_days=int(deadline),
                    budget=int(budget), params=params, n_simulations=int(n_sims),
                    has_qa=has_qa=="Yes", has_pm=has_pm=="Yes",
                )
                st.session_state.results = df

                sens = sensitivity_analysis(
                    base_params=params, total_tasks=total_tasks,
                    deadline_days=int(deadline), budget=int(budget),
                    n_simulations=min(int(n_sims), 3_000),
                    has_qa=has_qa=="Yes", has_pm=has_pm=="Yes",
                )
                st.session_state.sensitivity = sens

            st.session_state.step = 6; st.rerun()


# ═══════════════ STEP 6 — Results ════════════════════════════════════════════
elif st.session_state.step == 6:
    df          = st.session_state.results
    cx          = st.session_state.complexity_result
    deadline    = st.session_state.resources["deadline"]
    budget      = st.session_state.resources["budget"]
    sensitivity = st.session_state.sensitivity
    pname       = st.session_state.project_info["name"]

    p_on_time   = df["on_time"].mean()   * 100
    p_on_budget = df["on_budget"].mean() * 100
    p_success   = (df["on_time"] & df["on_budget"]).mean() * 100

    p10_d = int(df["days"].quantile(0.10))
    p50_d = int(df["days"].median())
    p90_d = int(df["days"].quantile(0.90))
    p10_c = int(df["cost"].quantile(0.10))
    p50_c = int(df["cost"].median())
    p90_c = int(df["cost"].quantile(0.90))

    def outcome_color(p):
        return "#388e3c" if p >= 70 else ("#e65100" if p >= 45 else "#c62828")

    # ── Result hero banner ────────────────────────────────────────────────────
    overall_color = outcome_color(p_success)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#1F3864,#2E75B6);
                border-radius:14px;padding:1.8rem 2.2rem;margin-bottom:1.2rem;">
        <div style="font-size:.85rem;color:#a8c8f0;margin-bottom:.2rem;">Risk Report for</div>
        <div style="font-size:1.9rem;font-weight:800;color:#fff;">{pname}</div>
        <div style="margin-top:.8rem;display:flex;gap:2.5rem;flex-wrap:wrap;">
            <div>
                <div style="font-size:2.4rem;font-weight:800;
                            color:{'#6adf8a' if p_on_time>=70 else '#ffb74d' if p_on_time>=45 else '#ef9a9a'};">
                    {p_on_time:.0f}%
                </div>
                <div style="color:#c8dbf5;font-size:.82rem;">On-Time Probability</div>
            </div>
            <div>
                <div style="font-size:2.4rem;font-weight:800;
                            color:{'#6adf8a' if p_on_budget>=70 else '#ffb74d' if p_on_budget>=45 else '#ef9a9a'};">
                    {p_on_budget:.0f}%
                </div>
                <div style="color:#c8dbf5;font-size:.82rem;">On-Budget Probability</div>
            </div>
            <div>
                <div style="font-size:2.4rem;font-weight:800;
                            color:{'#6adf8a' if p_success>=70 else '#ffb74d' if p_success>=45 else '#ef9a9a'};">
                    {p_success:.0f}%
                </div>
                <div style="color:#c8dbf5;font-size:.82rem;">Full Success Probability</div>
            </div>
            <div>
                <div style="font-size:2.4rem;font-weight:800;color:#fff;">
                    {cx['label']}
                </div>
                <div style="color:#c8dbf5;font-size:.82rem;">
                    Overall Complexity ({int(cx['overall']*100)}/100)
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tabs ──────────────────────────────────────────────────────────────────
    tab_cx, tab_time, tab_cost, tab_sens, tab_conv = st.tabs([
        "🔬 Complexity Profile",
        "📅 Timeline",
        "💰 Cost",
        "🌪️ Risk Factors",
        "📈 Convergence",
    ])

    # Complexity Profile
    with tab_cx:
        st.markdown("### 6-Dimension Complexity Radar")
        cl, cr = st.columns(2)
        with cl:
            st.plotly_chart(plot_complexity_radar(cx["dimensions"], cx["overall"], cx["label"]), use_container_width=True)
        with cr:
            st.plotly_chart(plot_dimension_bars(cx["dimensions"], cx["drivers"]), use_container_width=True)

        st.markdown("#### What Each Dimension Means")
        dim_info = {
            "Technical":      ("Performance needs, security/compliance, new technology, mobile platforms, offline support.",   cx["drivers"]),
            "Requirements":   ("Clarity and stability of requirements, number of stakeholders, domain familiarity, change risk.", cx["drivers"]),
            "Integration":    ("External APIs, database complexity, data migration burden, legacy system coupling.",              cx["drivers"]),
            "Team Fit":       ("Mismatch between team experience and project demands — junior ratio, new stack, new team, remote.", cx["drivers"]),
            "Feature Risk":   ("Average feature risk, highest-risk feature score, proportion of high-risk features.",             cx["drivers"]),
            "Organizational": ("Absence of PM, approval stages, and client involvement level.",                                   cx["drivers"]),
        }
        for dim, score in cx["dimensions"].items():
            desc, drivers = dim_info[dim]
            pct = int(score * 100)
            color = "#c62828" if pct >= 70 else ("#e65100" if pct >= 45 else "#2e7d32")
            driver_tag = '<span class="driver-tag">Top Driver</span>' if dim in drivers else ""
            st.markdown(
                f'<div class="dim-card">'
                f'<b style="color:{color}">{dim}</b> &nbsp;—&nbsp; '
                f'<b>{pct}/100</b>{driver_tag}'
                f'<br><span style="color:#555;font-size:.88rem;">{desc}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
        st.info(f"**Top complexity drivers:** {', '.join(cx['drivers'])}. These contribute the most to your risk and should be addressed first.")

    # Timeline
    with tab_time:
        cl, cr = st.columns([3, 2])
        with cl:
            st.plotly_chart(plot_duration_histogram(df["days"].values, deadline), use_container_width=True)
            st.caption("Everything to the RIGHT of the red dashed line is a missed deadline.")
        with cr:
            st.markdown("### Timeline")
            gap = p50_d - deadline
            st.markdown(f"""
| Scenario | Duration |
|---|---|
| Best Case (P10) | **{p10_d} days** |
| Most Likely (Median) | **{p50_d} days** |
| Worst Case (P90) | **{p90_d} days** |
| Your Deadline | **{deadline} days** |
""")
            if gap > 0:
                st.warning(f"Median finish is **{gap} days late**.")
            else:
                st.success(f"Median finish is **{abs(gap)} days ahead** of deadline.")

    # Cost
    with tab_cost:
        cl, cr = st.columns([3, 2])
        with cl:
            st.plotly_chart(plot_cost_histogram(df["cost"].values, budget), use_container_width=True)
            st.caption("Everything to the RIGHT of the red dashed line is a budget overrun.")
        with cr:
            st.markdown("### Cost")
            gap_c = p50_c - budget
            st.markdown(f"""
| Scenario | Cost |
|---|---|
| Best Case (P10) | **${p10_c:,}** |
| Most Likely (Median) | **${p50_c:,}** |
| Worst Case (P90) | **${p90_c:,}** |
| Your Budget | **${budget:,}** |
""")
            if gap_c > 0:
                st.warning(f"Median cost exceeds budget by **${gap_c:,}**.")
            else:
                st.success(f"Median cost is **${abs(gap_c):,} under budget**.")

    # Risk Factors
    with tab_sens:
        if sensitivity:
            st.plotly_chart(plot_tornado_chart(sensitivity), use_container_width=True)
            top = list(sensitivity.keys())[0]
            st.info(f"**Most impactful factor: {top}** — making this 30% worse adds ~{list(sensitivity.values())[0]:.0f} days. Fix this first.")

    # Convergence
    with tab_conv:
        st.plotly_chart(plot_convergence_chart(df["on_time"].values), use_container_width=True)
        st.caption("The probability stabilises as more simulations run — proof the Monte Carlo method is statistically valid.")

    st.divider()

    # High-risk features
    high_risk = get_high_risk_features(st.session_state.features)
    if high_risk:
        st.markdown("### High-Risk Features")
        st.warning("Address these before development starts.")
        for f in high_risk:
            reasons = []
            if not f["built_before"]:   reasons.append("never built before")
            if f["third_party"]:        reasons.append("third-party dependency")
            if f["req_clear"] != "Yes": reasons.append("unclear requirements")
            st.markdown(f"- **{f['name']}** — Risk `{int(f['score']*100)}%` — _{', '.join(reasons)}_")

    # Recommendations
    st.markdown("### Recommendations")
    recs = []
    if p_on_time < 70:
        recs.append(f"On-time probability is only **{p_on_time:.0f}%**. Median finish is **{p50_d-deadline:+d} days** vs your deadline. Extend the deadline, cut scope, or add senior developers.")
    if p_on_budget < 70:
        recs.append(f"Budget risk is high. Median cost (**${p50_c:,}**) exceeds budget (**${budget:,}**). Increase budget or reduce team cost.")
    if cx["drivers"]:
        recs.append(f"Biggest complexity driver: **{cx['drivers'][0]}**. Reducing this dimension has the largest positive impact on your risk score.")
    if not st.session_state.resources["has_qa"]:
        recs.append("No QA phase planned. This significantly increases post-release defect risk.")
    if p_success >= 75:
        recs.append("Your project looks well-planned. Proceed with confidence.")
    for r in recs:
        st.markdown(f"- {r}")

    st.divider()
    c_dl, c_rst = st.columns(2)
    with c_dl:
        st.download_button("Download Results (CSV)", data=df.to_csv(index=False),
                           file_name=f"{pname.replace(' ','_')}_risk_report.csv", mime="text/csv")
    with c_rst:
        if st.button("Start New Simulation"):
            for k, v in DEFAULTS.items(): st.session_state[k] = v
            st.rerun()
