BRAND_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ═══ BASE ══════════════════════════════════════════════════════════════ */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
}
.stApp { background: #f1f5ff !important; }

/* ═══ HIDE STREAMLIT CHROME (keep sidebar toggle) ══════════════════════ */
header[data-testid="stHeader"]  { display: none !important; }
[data-testid="stToolbar"]       { display: none !important; }
[data-testid="stDecoration"]    { display: none !important; }
[data-testid="stStatusWidget"]  { display: none !important; }
.stDeployButton                 { display: none !important; }
#MainMenu                       { display: none !important; }
footer                          { display: none !important; }

/* ═══ CONTENT AREA ══════════════════════════════════════════════════════ */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1200px !important;
}

/* ═══════════════════════════════════════════════════════════════════════
   SIDEBAR  — belt-and-suspenders targeting for Streamlit 1.57
   ═══════════════════════════════════════════════════════════════════════ */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div:first-child,
section[data-testid="stSidebar"] > div > div:first-child {
    background: linear-gradient(180deg,
        #09090f 0%,
        #0e0b2e 30%,
        #150e3d 60%,
        #1a1250 100%) !important;
}
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(139,92,246,0.15) !important;
    box-shadow: 4px 0 40px rgba(0,0,0,0.5) !important;
    min-width: 250px !important;
}
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"],
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
    background: transparent !important;
    background-color: transparent !important;
}

/* sidebar text (spans, paragraphs — not divs to avoid overriding custom classes) */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span:not(.sb-brand-name):not(.sb-brand-sub):not(.sb-nav-label) {
    color: #a89ec0 !important;
}
section[data-testid="stSidebar"] hr {
    border-color: rgba(139,92,246,0.12) !important; margin: .5rem 0 !important;
}

/* ── Brand block ── */
.sb-brand {
    padding: 1.7rem 1.1rem 1.2rem;
    text-align: center;
    border-bottom: 1px solid rgba(139,92,246,0.12);
    margin-bottom: .7rem;
}
.sb-brand-icon { font-size: 2.6rem; line-height: 1; display: block; }
.sb-brand-name {
    display: block;
    font-size: 1.38rem !important; font-weight: 900 !important;
    color: #ffffff !important; letter-spacing: -.5px; margin-top: .4rem;
}
.sb-brand-sub {
    display: block;
    font-size: .64rem !important; color: #5b4d8a !important;
    text-transform: uppercase; letter-spacing: 2.2px;
    font-weight: 700; margin-top: .28rem;
}

/* ── Nav label ── */
.sb-nav-label {
    display: block;
    font-size: .62rem !important; font-weight: 800 !important;
    color: #3b2f6e !important; text-transform: uppercase;
    letter-spacing: 2.2px; padding: .65rem 1.1rem .3rem;
}

/* ── Nav links ── */
section[data-testid="stSidebar"] a {
    display: flex !important; align-items: center !important; gap: 10px !important;
    padding: 9px 14px !important; border-radius: 10px !important;
    color: #9d8ecf !important; font-weight: 500 !important;
    font-size: .875rem !important; text-decoration: none !important;
    transition: all .2s ease !important;
    margin: 2px 8px !important; border: none !important;
    background: transparent !important;
}
section[data-testid="stSidebar"] a:hover {
    background: rgba(139,92,246,0.15) !important;
    color: #e2d9ff !important;
    transform: translateX(4px) !important;
}
section[data-testid="stSidebar"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(139,92,246,0.28), rgba(139,92,246,0.06)) !important;
    color: #c4b5fd !important; font-weight: 700 !important;
    border-left: 3px solid #8b5cf6 !important;
    padding-left: 11px !important;
}

/* ── Footer ── */
.sb-footer {
    display: block;
    padding: .9rem 1.1rem;
    border-top: 1px solid rgba(139,92,246,0.1);
    margin-top: .5rem; font-size: .69rem !important;
    color: #2e2554 !important; text-align: center; line-height: 1.75;
}

/* ═══ SCROLLBAR ══════════════════════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #c7c2e8; border-radius: 99px; }

/* ═══════════════════════════════════════════════════════════════════════
   HOME HERO
   ═══════════════════════════════════════════════════════════════════════ */
.rp-hero {
    background: linear-gradient(135deg,
        #07050f 0%, #130b2e 25%, #1c1050 55%, #250e6e 80%, #2d0f7e 100%);
    border-radius: 24px; padding: 0; margin-bottom: 2rem;
    position: relative; overflow: hidden;
    box-shadow: 0 28px 80px rgba(7,5,15,0.55), 0 0 0 1px rgba(139,92,246,0.15);
}
.rp-hero::before {
    content: ""; position: absolute; top: -140px; right: -80px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(139,92,246,.22) 0%, transparent 60%);
    border-radius: 50%; pointer-events: none;
}
.rp-hero::after {
    content: ""; position: absolute; bottom: -100px; left: 10%;
    width: 340px; height: 340px;
    background: radial-gradient(circle, rgba(99,102,241,.14) 0%, transparent 65%);
    border-radius: 50%; pointer-events: none;
}
.hero-inner {
    display: grid; grid-template-columns: 1fr 380px;
    gap: 2.5rem; padding: 3.8rem 3.5rem 3.8rem; position: relative; z-index: 1;
    align-items: center;
}
@media (max-width: 900px) {
    .hero-inner { grid-template-columns: 1fr; }
    .hero-visual { display: none; }
}
.rp-hero-eyebrow {
    font-size: .7rem; font-weight: 700; color: #a78bfa;
    letter-spacing: 3px; text-transform: uppercase; margin-bottom: .75rem;
    display: flex; align-items: center; gap: .5rem;
}
.rp-hero-eyebrow::before {
    content: ""; display: inline-block; width: 24px; height: 2px;
    background: #8b5cf6; border-radius: 2px;
}
.rp-hero-title {
    font-size: 3.4rem; font-weight: 900; color: #f5f3ff;
    line-height: 1.03; letter-spacing: -2px; margin: 0 0 1.1rem;
}
.rp-hero-title .accent {
    background: linear-gradient(135deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.rp-hero-sub {
    font-size: 1.03rem; color: #9d8ecf; max-width: 500px;
    line-height: 1.78; margin-bottom: 1.7rem;
}
.rp-hero-tags { display: flex; gap: .4rem; flex-wrap: wrap; }
.rp-tag {
    background: rgba(139,92,246,0.15); backdrop-filter: blur(8px);
    color: #c4b5fd; border-radius: 20px; padding: 5px 13px;
    font-size: .74rem; font-weight: 500;
    border: 1px solid rgba(139,92,246,0.25);
}

/* ── Hero visual panel ── */
.hero-visual {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 18px; padding: 1.4rem; backdrop-filter: blur(12px);
    position: relative; z-index: 1;
}
.hv-title {
    font-size: .65rem; text-transform: uppercase; letter-spacing: 2px;
    color: #7c6ba8; font-weight: 700; margin-bottom: 1rem;
}
.hv-metric {
    display: flex; align-items: center; justify-content: space-between;
    padding: .65rem .9rem; border-radius: 10px; margin-bottom: .5rem;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.06);
}
.hv-metric-label { font-size: .78rem; color: #8b7fb5; font-weight: 500; }
.hv-metric-val { font-size: 1.25rem; font-weight: 800; }
.hv-green  { color: #34d399; }
.hv-yellow { color: #fbbf24; }
.hv-red    { color: #f87171; }
.hv-bars { margin-top: .9rem; }
.hv-bar-row { margin-bottom: .55rem; }
.hv-bar-label { font-size: .7rem; color: #7c6ba8; margin-bottom: .22rem; font-weight: 500; }
.hv-bar-track {
    height: 6px; background: rgba(255,255,255,0.07);
    border-radius: 99px; overflow: hidden;
}
.hv-bar-fill { height: 100%; border-radius: 99px; }

/* Small hero (inner pages) */
.rp-hero-sm {
    background: linear-gradient(135deg, #07050f 0%, #130b2e 40%, #1c1050 100%);
    border-radius: 20px; padding: 2.2rem 2.6rem; margin-bottom: 2rem;
    box-shadow: 0 16px 52px rgba(7,5,15,0.35), 0 0 0 1px rgba(139,92,246,0.12);
    position: relative; overflow: hidden;
}
.rp-hero-sm::before {
    content: ""; position: absolute; top: -70px; right: -70px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(139,92,246,.18) 0%, transparent 65%);
    border-radius: 50%; pointer-events: none;
}
.rp-hero-sm-title {
    font-size: 1.9rem; font-weight: 800; color: #f5f3ff;
    margin: 0 0 .45rem; letter-spacing: -.6px; position: relative; z-index: 1;
}
.rp-hero-sm-sub {
    color: #9d8ecf; font-size: .96rem; margin: 0;
    line-height: 1.7; position: relative; z-index: 1;
}

/* ═══ STAT CARDS ══════════════════════════════════════════════════════════ */
.rp-stats {
    display: grid; grid-template-columns: repeat(4,1fr);
    gap: 1.1rem; margin: 0 0 2.6rem;
}
.rp-stat-card {
    background: #ffffff; border-radius: 18px; padding: 1.6rem 1.1rem;
    text-align: center; border: 1px solid #e0e7ff;
    box-shadow: 0 2px 18px rgba(79,70,229,0.07);
    transition: transform .25s, box-shadow .25s;
    position: relative; overflow: hidden;
}
.rp-stat-card::before {
    content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #7c3aed, #4f46e5, #818cf8);
}
.rp-stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 44px rgba(79,70,229,0.14);
}
.rp-stat-num {
    font-size: 2.5rem; font-weight: 900;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1;
}
.rp-stat-lbl {
    font-size: .7rem; color: #6b7280; margin-top: .45rem;
    font-weight: 600; text-transform: uppercase; letter-spacing: .7px;
}

/* ═══ FEATURE CARDS ══════════════════════════════════════════════════════ */
.rp-card {
    background: #fff; border: 1px solid #e0e7ff; border-radius: 18px;
    padding: 1.7rem 1.5rem; height: 100%;
    box-shadow: 0 2px 18px rgba(79,70,229,0.06);
    transition: transform .25s, box-shadow .25s, border-color .25s;
    position: relative; overflow: hidden;
}
.rp-card::after {
    content: ""; position: absolute; bottom: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    transform: scaleX(0); transform-origin: left; transition: transform .3s;
}
.rp-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 56px rgba(79,70,229,0.14);
    border-color: #c7d2fe;
}
.rp-card:hover::after { transform: scaleX(1); }
.rp-card-icon { font-size: 2.1rem; margin-bottom: .8rem; display: block; }
.rp-card-title { font-size: 1rem; font-weight: 700; color: #0f172a; margin-bottom: .45rem; }
.rp-card-body  { font-size: .87rem; color: #475569; line-height: 1.68; }

/* ═══ STEPS ══════════════════════════════════════════════════════════════ */
.rp-step {
    display: flex; align-items: flex-start; gap: 1.1rem;
    padding: 1.1rem 1.5rem; background: #fff; border-radius: 14px;
    border: 1px solid #e0e7ff; margin-bottom: .7rem;
    box-shadow: 0 1px 12px rgba(79,70,229,0.05);
    transition: border-color .2s, box-shadow .2s, transform .2s;
}
.rp-step:hover {
    border-color: #c7d2fe;
    box-shadow: 0 6px 28px rgba(79,70,229,0.1);
    transform: translateX(4px);
}
.rp-step-num {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff; border-radius: 50%; min-width: 32px; height: 32px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: .85rem; flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(79,70,229,0.4);
}
.rp-step-title { font-weight: 700; color: #0f172a; font-size: .96rem; }
.rp-step-body  { font-size: .85rem; color: #475569; margin-top: .2rem; line-height: 1.62; }

/* ═══ SECTION HEADERS ════════════════════════════════════════════════════ */
.rp-section-hdr {
    font-size: 1.55rem; font-weight: 800; color: #0f172a;
    margin: 2.4rem 0 .3rem; letter-spacing: -.5px;
}
.rp-section-sub { font-size: .9rem; color: #6b7280; margin-bottom: 1.3rem; }

/* ═══ SIMULATOR UI ═══════════════════════════════════════════════════════ */
.step-hdr {
    font-size: 1.2rem; font-weight: 700; color: #0f172a;
    border-bottom: 2px solid #4f46e5;
    padding-bottom: .38rem; margin-bottom: 1.1rem;
}
.note-box {
    background: linear-gradient(135deg, #eef2ff, #f5f3ff);
    border-left: 4px solid #6366f1;
    padding: .72rem 1.2rem; border-radius: 0 12px 12px 0;
    margin-bottom: 1.1rem; font-size: .88rem;
    color: #312e81; line-height: 1.68;
}

/* ═══ RISK LABELS ════════════════════════════════════════════════════════ */
.risk-low   { color: #059669; font-weight: 700; }
.risk-med   { color: #d97706; font-weight: 700; }
.risk-high  { color: #dc2626; font-weight: 700; }
.risk-vhigh { color: #7c3aed; font-weight: 700; }

/* ═══ DIMENSION CARD ═════════════════════════════════════════════════════ */
.dim-card {
    background: #fff; border: 1px solid #e0e7ff; border-radius: 13px;
    padding: .9rem 1.1rem; margin: .35rem 0;
    transition: border-color .2s, box-shadow .2s;
}
.dim-card:hover { border-color: #c7d2fe; box-shadow: 0 4px 16px rgba(79,70,229,0.08); }
.driver-tag {
    background: linear-gradient(135deg, #fef2f2, #fee2e2);
    color: #b91c1c; border-radius: 20px; padding: 2px 10px;
    font-size: .72rem; font-weight: 700;
    display: inline-block; margin-left: 8px; border: 1px solid #fecaca;
}

/* ═══ BUTTONS ════════════════════════════════════════════════════════════ */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    color: #fff !important; border: none !important;
    border-radius: 12px !important; font-weight: 600 !important;
    font-size: .95rem !important; padding: .58rem 2rem !important;
    box-shadow: 0 5px 20px rgba(79,70,229,0.42) !important;
    transition: all .2s !important; letter-spacing: .1px !important;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
    opacity: .92 !important; transform: translateY(-2px) !important;
    box-shadow: 0 10px 36px rgba(79,70,229,0.52) !important;
}
div[data-testid="stButton"] > button[kind="secondary"] {
    border-radius: 12px !important; border: 1.5px solid #c7d2fe !important;
    color: #4f46e5 !important; font-weight: 600 !important;
    background: #fff !important; transition: all .2s !important;
}
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    background: #eef2ff !important; border-color: #4f46e5 !important;
    transform: translateY(-1px) !important;
}

/* ═══ INPUTS ══════════════════════════════════════════════════════════════ */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    border-radius: 10px !important; border: 1.5px solid #e0e7ff !important;
    font-size: .92rem !important; background: #fff !important;
    transition: border-color .2s, box-shadow .2s !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}
[data-baseweb="select"] > div {
    border-radius: 10px !important; border: 1.5px solid #e0e7ff !important; background: #fff !important;
}

/* ═══ METRICS ════════════════════════════════════════════════════════════ */
[data-testid="stMetric"] {
    background: #fff; border-radius: 15px; padding: 1.1rem 1.3rem;
    border: 1px solid #e0e7ff; box-shadow: 0 2px 14px rgba(79,70,229,0.06);
}
[data-testid="stMetricLabel"] { font-size: .77rem !important; color: #6b7280 !important; font-weight: 500 !important; }
[data-testid="stMetricValue"] { font-size: 1.75rem !important; font-weight: 800 !important; color: #0f172a !important; }

/* ═══ TABS ════════════════════════════════════════════════════════════════ */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: .3rem; background: #eef2ff; border-radius: 13px;
    padding: 5px; border: 1px solid #e0e7ff;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    border-radius: 10px !important; font-weight: 500 !important;
    font-size: .87rem !important; color: #4b5563 !important;
    padding: .45rem 1.1rem !important; background: transparent !important;
    transition: all .2s !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    background: #fff !important; color: #4f46e5 !important;
    font-weight: 700 !important; box-shadow: 0 2px 10px rgba(79,70,229,0.12) !important;
}

/* ═══ EXPANDERS ══════════════════════════════════════════════════════════ */
[data-testid="stExpander"] {
    border: 1px solid #e0e7ff !important; border-radius: 14px !important;
    background: #fff !important; margin-bottom: .65rem !important;
    box-shadow: 0 1px 8px rgba(79,70,229,0.04) !important;
}
[data-testid="stExpander"] summary {
    font-weight: 600 !important; color: #0f172a !important; font-size: .95rem !important;
}

/* ═══ DIVIDER ════════════════════════════════════════════════════════════ */
hr { border-color: #e0e7ff !important; margin: 1.6rem 0 !important; }

/* ═══ HIW BOXES ══════════════════════════════════════════════════════════ */
.hiw-box {
    background: #fff; border: 1px solid #e0e7ff; border-radius: 14px;
    padding: 1.2rem 1.5rem; margin-bottom: .8rem; transition: border-color .2s;
}
.hiw-box:hover { border-color: #c7d2fe; }
.hiw-box h4 { color: #0f172a; margin-bottom: .35rem; font-size: .97rem; font-weight: 700; }
.hiw-box p  { color: #475569; font-size: .87rem; line-height: 1.7; margin: 0; }

/* ═══ TECH BADGES ════════════════════════════════════════════════════════ */
.tech-badge {
    display: inline-block; background: #eef2ff; color: #3730a3;
    border-radius: 20px; padding: 4px 14px; font-size: .78rem;
    font-weight: 600; margin: 3px; border: 1px solid #c7d2fe; transition: background .2s;
}
.tech-badge:hover { background: #e0e7ff; }

/* ═══ CTA BANNER ═════════════════════════════════════════════════════════ */
.cta-banner {
    background: linear-gradient(135deg,
        #07050f 0%, #130b2e 40%, #1c1050 70%, #2d0f7e 100%);
    border-radius: 24px; padding: 3rem 3.2rem;
    text-align: center; margin: 1.8rem 0;
    box-shadow: 0 24px 72px rgba(7,5,15,0.35), 0 0 0 1px rgba(139,92,246,0.15);
    position: relative; overflow: hidden;
}
.cta-banner::before {
    content: ""; position: absolute; top: -90px; right: -90px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(139,92,246,.22) 0%, transparent 65%);
    border-radius: 50%;
}
.cta-banner h3 {
    color: #f5f3ff; font-size: 1.6rem; font-weight: 800;
    margin-bottom: .55rem; position: relative; z-index: 1;
}
.cta-banner p {
    color: #9d8ecf; font-size: .95rem; margin-bottom: 1.5rem;
    position: relative; z-index: 1;
}
</style>
"""

# Injected directly inside st.sidebar for belt-and-suspenders background fix
SIDEBAR_BG_CSS = """
<style>
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div:first-child,
section[data-testid="stSidebar"] > div > div:first-child {
    background: linear-gradient(180deg,
        #09090f 0%, #0e0b2e 30%, #150e3d 60%, #1a1250 100%) !important;
}
</style>
"""
