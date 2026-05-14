import streamlit as st

st.set_page_config(
    page_title="RiskPulse — Project Risk Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
html,body,[class*="css"],.stApp{font-family:'Inter',system-ui,sans-serif!important}
.stApp{background:#f1f4ff!important}
.block-container{padding-top:.5rem!important;padding-bottom:4rem!important;max-width:1280px!important;padding-left:2rem!important;padding-right:2rem!important}
header[data-testid="stHeader"]{display:none!important}
[data-testid="stToolbar"]{display:none!important}
[data-testid="stDecoration"]{display:none!important}
[data-testid="collapsedControl"]{display:none!important}
section[data-testid="stSidebar"]{display:none!important}
footer{display:none!important}
.stDeployButton{display:none!important}
#MainMenu{display:none!important}

/* Buttons */
div[data-testid="stButton"]>button[kind="primary"]{background:linear-gradient(135deg,#4f46e5,#7c3aed)!important;color:#fff!important;border:none!important;border-radius:12px!important;font-weight:600!important;font-size:.95rem!important;padding:.56rem 2rem!important;box-shadow:0 5px 20px rgba(79,70,229,.42)!important;transition:all .2s!important}
div[data-testid="stButton"]>button[kind="primary"]:hover{opacity:.9!important;transform:translateY(-2px)!important}
div[data-testid="stButton"]>button[kind="secondary"]{border-radius:12px!important;border:1.5px solid #c7d2fe!important;color:#4f46e5!important;font-weight:600!important;background:#fff!important;transition:all .2s!important}
div[data-testid="stButton"]>button[kind="secondary"]:hover{background:#eef2ff!important;border-color:#4f46e5!important}

/* Inputs */
[data-testid="stTextInput"] input,[data-testid="stNumberInput"] input{border-radius:10px!important;border:1.5px solid #e0e7ff!important;background:#fff!important}
[data-testid="stTextInput"] input:focus,[data-testid="stNumberInput"] input:focus{border-color:#6366f1!important;box-shadow:0 0 0 3px rgba(99,102,241,.15)!important}
[data-baseweb="select"]>div{border-radius:10px!important;border:1.5px solid #e0e7ff!important;background:#fff!important}

/* Tabs */
[data-testid="stTabs"] [data-baseweb="tab-list"]{background:#eef2ff!important;border-radius:12px!important;padding:4px!important;border:1px solid #e0e7ff!important;gap:.25rem!important}
[data-testid="stTabs"] [data-baseweb="tab"]{border-radius:9px!important;font-weight:500!important;font-size:.87rem!important;color:#4b5563!important;padding:.44rem 1rem!important;background:transparent!important}
[data-testid="stTabs"] [aria-selected="true"]{background:#fff!important;color:#4f46e5!important;font-weight:700!important;box-shadow:0 2px 10px rgba(79,70,229,.12)!important}

/* Expanders */
[data-testid="stExpander"]{border:1px solid #e0e7ff!important;border-radius:14px!important;background:#fff!important;margin-bottom:.6rem!important}
[data-testid="stExpander"] summary{font-weight:600!important;color:#0f172a!important}

/* Divider */
hr{border-color:#e0e7ff!important;margin:1.5rem 0!important}

/* page_link nav styling */
[data-testid="stPageLink"] a{color:#9d8ecf!important;font-size:.83rem!important;font-weight:600!important;padding:.4rem .85rem!important;border-radius:8px!important;text-decoration:none!important;transition:all .18s!important;white-space:nowrap!important;}
[data-testid="stPageLink"] a:hover{background:rgba(139,92,246,.2)!important;color:#e2d9ff!important;}
[data-testid="stPageLink"] a[aria-current="page"]{background:rgba(139,92,246,.28)!important;color:#c4b5fd!important;font-weight:700!important;}
[data-testid="stPageLink"]{margin:0!important;padding:0!important;}

/* Scrollbar */
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-thumb{background:#c7c2e8;border-radius:99px}

/* ── Shared page components ─────────────────────────────────── */
.rp-hero-sm{background:linear-gradient(135deg,#07050f 0%,#130b2e 40%,#1c1050 70%,#2d0f7e 100%);border-radius:20px;padding:2.4rem 2.8rem;margin-bottom:1.8rem;box-shadow:0 20px 60px rgba(7,5,15,.4),0 0 0 1px rgba(139,92,246,.15);}
.rp-hero-sm-title{font-size:1.75rem;font-weight:900;color:#f5f3ff;letter-spacing:-.5px;margin-bottom:.5rem;}
.rp-hero-sm-sub{font-size:.95rem;color:#9d8ecf;line-height:1.7;max-width:680px;}
.rp-section-hdr{font-size:1.35rem;font-weight:800;color:#0f172a;margin:1.8rem 0 .6rem;letter-spacing:-.4px;}
.rp-section-sub{font-size:.88rem;color:#6b7280;margin-bottom:1.2rem;}
.step-hdr{font-size:1.22rem;font-weight:800;color:#0f172a;margin:0 0 .5rem;letter-spacing:-.3px;}
.note-box{background:#eef2ff;border-left:3px solid #6366f1;border-radius:0 10px 10px 0;padding:.75rem 1.1rem;font-size:.86rem;color:#3730a3;line-height:1.65;margin-bottom:1.2rem;}
.risk-low{background:#dcfce7;color:#166534;border-radius:20px;padding:3px 12px;font-size:.76rem;font-weight:700;}
.risk-med{background:#fef9c3;color:#854d0e;border-radius:20px;padding:3px 12px;font-size:.76rem;font-weight:700;}
.risk-high{background:#fee2e2;color:#991b1b;border-radius:20px;padding:3px 12px;font-size:.76rem;font-weight:700;}
.dim-card{background:#fff;border:1px solid #e0e7ff;border-radius:14px;padding:1.1rem 1.3rem;margin-bottom:.5rem;box-shadow:0 1px 8px rgba(79,70,229,.05);}
.driver-tag{background:#ede9fe;color:#5b21b6;border-radius:20px;padding:2px 10px;font-size:.7rem;font-weight:700;margin-left:.6rem;}
.rp-card{background:#fff;border:1px solid #e0e7ff;border-radius:16px;padding:1.5rem;box-shadow:0 2px 12px rgba(79,70,229,.06);}
.rp-card-icon{font-size:1.8rem;margin-bottom:.6rem;}
.rp-card-title{font-size:.97rem;font-weight:700;color:#0f172a;margin-bottom:.4rem;}
.rp-card-body{font-size:.86rem;color:#475569;line-height:1.65;}
.rp-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem 1.3rem;background:#fff;border-radius:12px;border:1px solid #e0e7ff;margin-bottom:.55rem;box-shadow:0 1px 8px rgba(79,70,229,.04);}
.rp-step-num{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-radius:50%;min-width:30px;height:30px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.82rem;flex-shrink:0;box-shadow:0 3px 10px rgba(79,70,229,.35);}
.rp-step-title{font-weight:700;color:#0f172a;font-size:.93rem;}
.rp-step-body{font-size:.83rem;color:#475569;margin-top:.15rem;line-height:1.6;}
.tech-badge{display:inline-block;background:#eef2ff;color:#3730a3;border:1px solid #c7d2fe;border-radius:20px;padding:3px 13px;font-size:.78rem;font-weight:600;margin:.2rem .2rem 0 0;}
.hiw-box{background:#f8faff;border:1px solid #e0e7ff;border-radius:12px;padding:1.1rem 1.3rem;margin-bottom:.6rem;}
.hiw-box h4{color:#1e3a8a;font-size:.97rem;font-weight:700;margin:0 0 .35rem;}
.hiw-box p{color:#374151;font-size:.87rem;line-height:1.65;margin:0;}
</style>
""", unsafe_allow_html=True)

# ── Pages ─────────────────────────────────────────────────────────────────────
home_pg  = st.Page("pages/home.py",         title="Home",         icon="🏠", default=True)
sim_pg   = st.Page("pages/simulator.py",    title="Simulator",    icon="📊")
hiw_pg   = st.Page("pages/how_it_works.py", title="How It Works", icon="🔬")
about_pg = st.Page("pages/about.py",        title="About",        icon="ℹ️")

pg = st.navigation([home_pg, sim_pg, hiw_pg, about_pg], position="hidden")

# ── Top navigation bar (pure HTML — no widget splitting) ─────────────────────
st.markdown('<div style="background:linear-gradient(90deg,#07050f 0%,#130b2e 50%,#1c1050 100%);border-radius:16px;padding:.8rem 1.8rem;margin-bottom:1.4rem;display:flex;align-items:center;justify-content:space-between;box-shadow:0 4px 24px rgba(7,5,15,.35),0 0 0 1px rgba(139,92,246,.15);"><div style="display:flex;align-items:center;gap:.75rem;"><span style="font-size:1.6rem;line-height:1;">📊</span><div><div style="font-size:1.12rem;font-weight:900;color:#fff;letter-spacing:-.3px;line-height:1.2;">RiskPulse</div><div style="font-size:.58rem;color:#5b4d8a;text-transform:uppercase;letter-spacing:2.2px;font-weight:700;">Project Risk Intelligence</div></div></div><div style="display:flex;align-items:center;gap:.2rem;"><a href="/" target="_self" style="color:#9d8ecf;font-size:.85rem;font-weight:600;padding:.45rem .95rem;border-radius:8px;text-decoration:none;white-space:nowrap;">🏠 Home</a><a href="/simulator" target="_self" style="color:#9d8ecf;font-size:.85rem;font-weight:600;padding:.45rem .95rem;border-radius:8px;text-decoration:none;white-space:nowrap;">📊 Simulator</a><a href="/how_it_works" target="_self" style="color:#9d8ecf;font-size:.85rem;font-weight:600;padding:.45rem .95rem;border-radius:8px;text-decoration:none;white-space:nowrap;">🔬 How It Works</a><a href="/about" target="_self" style="color:#9d8ecf;font-size:.85rem;font-weight:600;padding:.45rem .95rem;border-radius:8px;text-decoration:none;white-space:nowrap;">ℹ️ About</a></div></div>', unsafe_allow_html=True)

# ── Run page ──────────────────────────────────────────────────────────────────
pg.run()
