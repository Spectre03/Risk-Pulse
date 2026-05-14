import streamlit as st

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#07050f 0%,#130b2e 25%,#1c1050 55%,#2d0f7e 100%);border-radius:24px;padding:3.5rem 3rem;margin-bottom:2rem;position:relative;overflow:hidden;box-shadow:0 28px 80px rgba(7,5,15,.55),0 0 0 1px rgba(139,92,246,.15);">
<div style="position:absolute;top:-140px;right:-80px;width:480px;height:480px;background:radial-gradient(circle,rgba(139,92,246,.22) 0%,transparent 60%);border-radius:50%;pointer-events:none;"></div>
<div style="display:grid;grid-template-columns:1fr 340px;gap:2.5rem;align-items:center;position:relative;z-index:1;">
<div>
<div style="font-size:.7rem;font-weight:700;color:#a78bfa;letter-spacing:3px;text-transform:uppercase;margin-bottom:.8rem;display:flex;align-items:center;gap:.5rem;"><span style="display:inline-block;width:22px;height:2px;background:#8b5cf6;border-radius:2px;flex-shrink:0;"></span>Monte Carlo Simulation · Risk Intelligence</div>
<div style="font-size:3rem;font-weight:900;color:#f5f3ff;line-height:1.04;letter-spacing:-2px;margin-bottom:1rem;">Know Your Risk.<br><span style="background:linear-gradient(135deg,#a78bfa,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Before You Build.</span></div>
<div style="font-size:1rem;color:#9d8ecf;max-width:500px;line-height:1.78;margin-bottom:1.6rem;">RiskPulse runs 10,000 simulated versions of your project and gives you the honest probability of hitting your deadline and budget — derived from your real features, team, and context. Not a guess. A distribution.</div>
<div style="display:flex;gap:.4rem;flex-wrap:wrap;">
<span style="background:rgba(139,92,246,.15);color:#c4b5fd;border-radius:20px;padding:5px 13px;font-size:.74rem;font-weight:500;border:1px solid rgba(139,92,246,.25);display:inline-block;">📊 Monte Carlo Engine</span>
<span style="background:rgba(139,92,246,.15);color:#c4b5fd;border-radius:20px;padding:5px 13px;font-size:.74rem;font-weight:500;border:1px solid rgba(139,92,246,.25);display:inline-block;">🔬 6-Dimension Complexity</span>
<span style="background:rgba(139,92,246,.15);color:#c4b5fd;border-radius:20px;padding:5px 13px;font-size:.74rem;font-weight:500;border:1px solid rgba(139,92,246,.25);display:inline-block;">⚡ 10,000+ Scenarios</span>
<span style="background:rgba(139,92,246,.15);color:#c4b5fd;border-radius:20px;padding:5px 13px;font-size:.74rem;font-weight:500;border:1px solid rgba(139,92,246,.25);display:inline-block;">🎯 Actionable Insights</span>
</div>
</div>
<div style="background:rgba(255,255,255,.05);border:1px solid rgba(139,92,246,.22);border-radius:18px;padding:1.4rem;">
<div style="font-size:.62rem;text-transform:uppercase;letter-spacing:2.2px;color:#6b5fa8;font-weight:700;margin-bottom:1rem;">Sample Risk Report</div>
<div style="display:flex;align-items:center;justify-content:space-between;padding:.6rem .85rem;border-radius:10px;margin-bottom:.4rem;background:rgba(52,211,153,.08);border:1px solid rgba(52,211,153,.2);"><span style="font-size:.77rem;color:#8b7fb5;font-weight:500;">On-Time Probability</span><span style="font-size:1.25rem;font-weight:800;color:#34d399;">72%</span></div>
<div style="display:flex;align-items:center;justify-content:space-between;padding:.6rem .85rem;border-radius:10px;margin-bottom:.4rem;background:rgba(251,191,36,.06);border:1px solid rgba(251,191,36,.2);"><span style="font-size:.77rem;color:#8b7fb5;font-weight:500;">On-Budget Probability</span><span style="font-size:1.25rem;font-weight:800;color:#fbbf24;">61%</span></div>
<div style="display:flex;align-items:center;justify-content:space-between;padding:.6rem .85rem;border-radius:10px;margin-bottom:.4rem;background:rgba(248,113,113,.06);border:1px solid rgba(248,113,113,.17);"><span style="font-size:.77rem;color:#8b7fb5;font-weight:500;">Complexity Score</span><span style="font-size:1.05rem;font-weight:800;color:#f87171;">High · 74/100</span></div>
<div style="margin-top:.9rem;padding-top:.9rem;border-top:1px solid rgba(139,92,246,.12);">
<div style="font-size:.62rem;text-transform:uppercase;letter-spacing:2px;color:#6b5fa8;font-weight:700;margin-bottom:.65rem;">Complexity Breakdown</div>
<div style="margin-bottom:.48rem;"><div style="display:flex;justify-content:space-between;font-size:.7rem;color:#8b7fb5;margin-bottom:.2rem;"><span>Technical</span><span style="color:#f87171;">68%</span></div><div style="height:5px;background:rgba(255,255,255,.07);border-radius:99px;overflow:hidden;"><div style="width:68%;height:100%;border-radius:99px;background:linear-gradient(90deg,#f87171,#fb923c);"></div></div></div>
<div style="margin-bottom:.48rem;"><div style="display:flex;justify-content:space-between;font-size:.7rem;color:#8b7fb5;margin-bottom:.2rem;"><span>Requirements</span><span style="color:#fbbf24;">52%</span></div><div style="height:5px;background:rgba(255,255,255,.07);border-radius:99px;overflow:hidden;"><div style="width:52%;height:100%;border-radius:99px;background:linear-gradient(90deg,#fbbf24,#f59e0b);"></div></div></div>
<div style="margin-bottom:.48rem;"><div style="display:flex;justify-content:space-between;font-size:.7rem;color:#8b7fb5;margin-bottom:.2rem;"><span>Team Fit</span><span style="color:#34d399;">38%</span></div><div style="height:5px;background:rgba(255,255,255,.07);border-radius:99px;overflow:hidden;"><div style="width:38%;height:100%;border-radius:99px;background:linear-gradient(90deg,#34d399,#10b981);"></div></div></div>
<div><div style="display:flex;justify-content:space-between;font-size:.7rem;color:#8b7fb5;margin-bottom:.2rem;"><span>Integration</span><span style="color:#f87171;">75%</span></div><div style="height:5px;background:rgba(255,255,255,.07);border-radius:99px;overflow:hidden;"><div style="width:75%;height:100%;border-radius:99px;background:linear-gradient(90deg,#f87171,#fb923c);"></div></div></div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ── Stat cards ────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4, gap="small")
for col, num, label in zip([c1,c2,c3,c4], ["10K+","6","16","5"],
    ["Simulations Per Run","Complexity Dimensions","Context Factors","Statistical Distributions"]):
    with col:
        st.markdown(f'<div style="background:#fff;border-radius:18px;padding:1.5rem 1rem;text-align:center;border:1px solid #e0e7ff;box-shadow:0 2px 16px rgba(79,70,229,.07);position:relative;overflow:hidden;"><div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#7c3aed,#4f46e5,#818cf8);"></div><div style="font-size:2.3rem;font-weight:900;line-height:1;background:linear-gradient(135deg,#4f46e5,#7c3aed);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">{num}</div><div style="font-size:.69rem;color:#6b7280;margin-top:.4rem;font-weight:600;text-transform:uppercase;letter-spacing:.7px;">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Why RiskPulse ─────────────────────────────────────────────────────────────
st.markdown('<div style="font-size:1.5rem;font-weight:800;color:#0f172a;margin:2rem 0 .3rem;letter-spacing:-.5px;">Why RiskPulse?</div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:.9rem;color:#6b7280;margin-bottom:1.3rem;">Most projects fail not because the team is bad — but because the risk was never honestly measured.</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")
for col, icon, title, body in zip([c1,c2,c3],
    ["📉","🎯","🔬"],
    ["69% of Projects Fail","Not a Guess — A Probability","Complexity From First Principles"],
    ["The Standish CHAOS Report finds only 31% of software projects are delivered on time and within budget. RiskPulse gives you the insight to be in that 31%.",
     "Instead of one optimistic estimate, RiskPulse runs 10,000 simulated versions: best case, median, worst case — with exact probabilities.",
     "Complexity is not a dropdown. RiskPulse derives it from your actual features, team, technology, integrations, and organisational context."]):
    with col:
        st.markdown(f'<div style="background:#fff;border:1px solid #e0e7ff;border-radius:18px;padding:1.6rem 1.5rem;box-shadow:0 2px 16px rgba(79,70,229,.06);"><div style="font-size:2rem;margin-bottom:.75rem;">{icon}</div><div style="font-size:.98rem;font-weight:700;color:#0f172a;margin-bottom:.45rem;">{title}</div><div style="font-size:.86rem;color:#475569;line-height:1.65;">{body}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── How it works ──────────────────────────────────────────────────────────────
st.markdown('<div style="font-size:1.5rem;font-weight:800;color:#0f172a;margin:2rem 0 1rem;letter-spacing:-.5px;">How It Works in 5 Steps</div>', unsafe_allow_html=True)

for i, (title, body) in enumerate([
    ("Describe Your Project", "Name your project and select its type. Each type carries a baseline risk profile."),
    ("Add Your Features", "List each major feature. Answer 3 quick questions — built before? third-party API? clear requirements?"),
    ("Answer 16 Context Questions", "Cover technical requirements, requirement stability, integrations, and organisational factors."),
    ("Enter Team & Constraints", "Specify your seniority mix, budget, and deadline. All distributions adjust to your team profile."),
    ("Get Your Full Risk Report", "On-time and on-budget probabilities, radar chart, sensitivity analysis, and recommendations."),
], start=1):
    st.markdown(f'<div style="display:flex;align-items:flex-start;gap:1rem;padding:1.1rem 1.4rem;background:#fff;border-radius:14px;border:1px solid #e0e7ff;margin-bottom:.65rem;box-shadow:0 1px 10px rgba(79,70,229,.05);"><div style="background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-radius:50%;min-width:32px;height:32px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.85rem;flex-shrink:0;box-shadow:0 4px 12px rgba(79,70,229,.4);">{i}</div><div><div style="font-weight:700;color:#0f172a;font-size:.95rem;">{title}</div><div style="font-size:.84rem;color:#475569;margin-top:.18rem;line-height:1.6;">{body}</div></div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── What you get ──────────────────────────────────────────────────────────────
st.markdown('<div style="font-size:1.5rem;font-weight:800;color:#0f172a;margin:2rem 0 1rem;letter-spacing:-.5px;">What You Get in the Report</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="medium")
with c1:
    for icon, title, body in [("📊","Timeline Distribution","Histogram of 10,000 simulated durations. Deadline marked — everything right of it is a miss."),("💰","Cost Distribution","Full spread of possible project costs with your budget as a reference line."),("🕸️","Complexity Radar","6-arm spider chart across Technical, Requirements, Integration, Team Fit, Feature Risk, Org.")]:
        st.markdown(f'<div style="background:#fff;border:1px solid #e0e7ff;border-radius:16px;padding:1.5rem;margin-bottom:.85rem;box-shadow:0 2px 14px rgba(79,70,229,.06);"><div style="font-size:1.7rem;margin-bottom:.7rem;">{icon}</div><div style="font-size:.97rem;font-weight:700;color:#0f172a;margin-bottom:.4rem;">{title}</div><div style="font-size:.86rem;color:#475569;line-height:1.65;">{body}</div></div>', unsafe_allow_html=True)
with c2:
    for icon, title, body in [("🌪️","Sensitivity Analysis","Tornado chart: which factor adds the most days if it gets 30% worse. Fix the longest bar first."),("📈","Convergence Proof","Probability plotted across all simulations — proves the Monte Carlo method is statistically valid."),("💡","Recommendations","Plain-English advice specific to your complexity profile, high-risk features, and outcomes.")]:
        st.markdown(f'<div style="background:#fff;border:1px solid #e0e7ff;border-radius:16px;padding:1.5rem;margin-bottom:.85rem;box-shadow:0 2px 14px rgba(79,70,229,.06);"><div style="font-size:1.7rem;margin-bottom:.7rem;">{icon}</div><div style="font-size:.97rem;font-weight:700;color:#0f172a;margin-bottom:.4rem;">{title}</div><div style="font-size:.86rem;color:#475569;line-height:1.65;">{body}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown('<div style="background:linear-gradient(135deg,#07050f 0%,#130b2e 40%,#1c1050 70%,#2d0f7e 100%);border-radius:24px;padding:3rem 3.2rem;text-align:center;margin:1.5rem 0;box-shadow:0 24px 72px rgba(7,5,15,.35),0 0 0 1px rgba(139,92,246,.15);position:relative;overflow:hidden;"><div style="font-size:1.6rem;font-weight:800;color:#f5f3ff;margin-bottom:.55rem;position:relative;z-index:1;">Ready to measure your project\'s real risk?</div><div style="font-size:.95rem;color:#9d8ecf;position:relative;z-index:1;">Use the Simulator to get your full risk report in under 5 minutes.</div></div>', unsafe_allow_html=True)

col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    if st.button("Launch the Simulator →", type="primary", use_container_width=True):
        st.switch_page("pages/simulator.py")

st.markdown('<div style="margin-top:3rem;padding-top:1.2rem;border-top:1px solid #e0e7ff;text-align:center;color:#9ca3af;font-size:.78rem;">RiskPulse · Monte Carlo Project Risk Simulator · Built with Python, NumPy, Streamlit &amp; Plotly · Simulation &amp; Modeling — Group 4</div>', unsafe_allow_html=True)
