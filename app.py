
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# SAHARA UK FOODS
# SPECIFICATION INTELLIGENCE
# PREMIUM UI DESIGN PROTOTYPE
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DESIGN SYSTEM --------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #071426;
    --navy2: #0B1C33;
    --panel: #10233D;
    --panel2: #142B48;
    --gold: #D6AD55;
    --gold-light: #F1D28A;
    --green: #35A879;
    --text: #F2F5FA;
    --muted: #91A2B9;
    --border: rgba(255,255,255,.08);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 85% 0%, rgba(34,93,130,.15), transparent 38%),
        linear-gradient(135deg,#071426 0%,#09182B 55%,#071426 100%);
    color: var(--text);
}

/* Remove Streamlit top header line */
header[data-testid="stHeader"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

header[data-testid="stHeader"]::after {
    display: none !important;
}

[data-testid="stToolbar"] {
    right: 1rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 2rem !important;
    max-width: 1500px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #08172A;
    border-right: 1px solid rgba(214,173,85,.15);
}

section[data-testid="stSidebar"] > div {
    padding: 1.4rem 1rem;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #C3D0DF !important;
}

/* Inputs */
.stTextInput input {
    background: #10233D !important;
    border: 1px solid rgba(255,255,255,.10) !important;
    border-radius: 10px !important;
    color: white !important;
    min-height: 45px;
}

.stTextInput input:focus {
    border-color: #D6AD55 !important;
    box-shadow: 0 0 0 1px #D6AD55 !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg,#D6AD55,#B88A35);
    color: #101B2A !important;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    min-height: 42px;
    transition: .2s ease;
}

.stButton button:hover {
    background: #F1D28A;
    transform: translateY(-1px);
}

/* Radio navigation */
section[data-testid="stSidebar"] .stRadio label {
    padding: 8px 10px;
    border-radius: 8px;
}

/* Select boxes */
.stSelectbox div[data-baseweb="select"] > div {
    background: #10233D;
    border-color: rgba(255,255,255,.12);
    color: white;
    border-radius: 9px;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,.08) !important;
}

/* Headings */
h1, h2, h3 {
    color: #F5F7FB !important;
    font-family: 'Manrope', sans-serif !important;
}

/* Remove excess empty spacing */
[data-testid="stVerticalBlock"] {
    gap: 1rem;
}

</style>
""", unsafe_allow_html=True)


# -------------------- REUSABLE UI --------------------

def section_title(title, subtitle=""):
    st.markdown(f"""
    <div style="margin:12px 0 20px 0;">
        <div style="font-size:23px;font-weight:800;
                    color:#F3F6FC;font-family:Manrope;">
            {title}
        </div>
        <div style="font-size:12px;color:#91A2B9;margin-top:5px;">
            {subtitle}
        </div>
    </div>
    """, unsafe_allow_html=True)


def metric_card(label, value, detail, symbol):
    st.markdown(f"""
    <div style="
        background:linear-gradient(145deg,#122945,#0E2038);
        border:1px solid rgba(255,255,255,.075);
        border-radius:15px;
        padding:20px 19px;
        min-height:135px;
        box-shadow:0 8px 25px rgba(0,0,0,.12);
    ">
        <div style="display:flex;justify-content:space-between;">
            <span style="font-size:12px;color:#91A2B9;
                         font-weight:600;">{label}</span>
            <span style="color:#D6AD55;font-size:19px;">{symbol}</span>
        </div>
        <div style="font-size:29px;font-weight:800;
                    color:#F5F7FB;margin-top:12px;">
            {value}
        </div>
        <div style="font-size:11px;color:#91A2B9;margin-top:5px;">
            {detail}
        </div>
    </div>
    """, unsafe_allow_html=True)


def feature_card(icon, title, description, status="AVAILABLE"):
    st.markdown(f"""
    <div style="
        background:linear-gradient(145deg,#122945,#0D2037);
        border:1px solid rgba(255,255,255,.075);
        border-radius:14px;
        padding:20px;
        min-height:150px;
        height:100%;
    ">
        <div style="font-size:25px;margin-bottom:13px;">{icon}</div>
        <div style="font-size:15px;font-weight:700;color:#F2F5FA;">
            {title}
        </div>
        <div style="font-size:11px;color:#91A2B9;
                    line-height:1.6;margin-top:8px;">
            {description}
        </div>
        <div style="font-size:9px;letter-spacing:1px;
                    color:#D6AD55;margin-top:15px;font-weight:700;">
            {status}
        </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("""
    <div style="padding:8px 4px 25px 4px;">
        <div style="display:flex;align-items:center;gap:12px;">
            <div style="
                width:43px;height:43px;border-radius:12px;
                background:linear-gradient(135deg,#D6AD55,#A77B2E);
                display:flex;align-items:center;justify-content:center;
                font-size:23px;color:#071426;font-weight:900;">
                S
            </div>
            <div>
                <div style="font-size:17px;font-weight:800;
                            color:#F5F7FB;letter-spacing:.4px;">
                    SAHARA
                </div>
                <div style="font-size:9px;color:#D6AD55;
                            letter-spacing:2px;">
                    UK FOODS LTD
                </div>
            </div>
        </div>
    </div>
    <div style="font-size:9px;color:#71849E;
                letter-spacing:2px;padding:0 5px 10px;">
        WORKSPACE
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Browse Products",
            "Specification Viewer",
            "AI Assistant",
            "Product Comparison",
            "Compliance Hub",
            "Downloads",
            "About Sahara"
        ],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="margin-top:35px;padding:15px;
        background:#10233D;border:1px solid rgba(214,173,85,.16);
        border-radius:12px;">
        <div style="font-size:10px;color:#D6AD55;
                    letter-spacing:1px;font-weight:700;">
            SAHARA INTELLIGENCE
        </div>
        <div style="font-size:11px;color:#91A2B9;
                    margin-top:8px;line-height:1.6;">
            Product specification management and
            document intelligence workspace.
        </div>
    </div>
    <div style="font-size:9px;color:#647991;
                margin-top:25px;text-align:center;">
        SAHARA UK FOODS LTD<br>
        ENTERPRISE WORKSPACE
    </div>
    """, unsafe_allow_html=True)


# -------------------- MAIN HEADER --------------------

st.markdown("""
<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:4px 0 20px 0;
    border-bottom:1px solid rgba(214,173,85,.18);
">
    <div>
        <div style="font-size:10px;color:#D6AD55;
                    letter-spacing:2px;font-weight:700;">
            SAHARA UK FOODS LTD
        </div>
        <div style="font-size:27px;font-weight:800;
                    font-family:Manrope;color:#F5F7FB;
                    margin-top:5px;">
            Specification Intelligence
        </div>
        <div style="font-size:11px;color:#91A2B9;margin-top:4px;">
            Smarter Search. Accurate Answers.
        </div>
    </div>
    <div style="
        background:#10233D;
        border:1px solid rgba(214,173,85,.25);
        border-radius:10px;
        padding:10px 15px;
        text-align:right;">
        <div style="font-size:9px;color:#91A2B9;letter-spacing:1px;">
            WORKSPACE
        </div>
        <div style="font-size:12px;color:#D6AD55;font-weight:700;">
            SAHARA
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------- DASHBOARD --------------------

if page == "Dashboard":

    section_title(
        "Command Centre",
        "Your central workspace for product specifications and intelligence."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("PRODUCT DATABASE", "—", "Awaiting data connection", "▦")

    with c2:
        metric_card("SPECIFICATION FILES", "—", "PDF library", "▤")

    with c3:
        metric_card("PRODUCT CATEGORIES", "—", "Database categories", "◈")

    with c4:
        metric_card("AI INTELLIGENCE", "READY", "Interface preview", "✦")

    section_title(
        "Intelligence Workspace",
        "Access the key areas of your specification management system."
    )

    a, b, c = st.columns(3)

    with a:
        feature_card(
            "▤", "Product Specifications",
            "Browse product records and access their original specification documents."
        )

    with b:
        feature_card(
            "✦", "AI Specification Assistant",
            "Find relevant specification information and supporting evidence."
        )

    with c:
        feature_card(
            "◈", "Product Comparison",
            "Compare product information across available specification records."
        )

    d, e, f = st.columns(3)

    with d:
        feature_card(
            "✓", "Compliance Intelligence",
            "Review documented compliance information and product declarations."
        )

    with e:
        feature_card(
            "◎", "Document Library",
            "Access and organise your product specification documents."
        )

    with f:
        feature_card(
            "⌘", "Data Management",
            "Manage the information powering the intelligence workspace."
        )

    section_title("Quick Access", "Choose where you want to go next.")

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button("Browse Products", use_container_width=True):
            st.session_state["navigation_request"] = "Browse Products"
            st.rerun()

    with q2:
        if st.button("Open AI Assistant", use_container_width=True):
            st.session_state["navigation_request"] = "AI Assistant"
            st.rerun()

    with q3:
        if st.button("Compliance Hub", use_container_width=True):
            st.session_state["navigation_request"] = "Compliance Hub"
            st.rerun()


# -------------------- OTHER SECTIONS --------------------

elif page == "Browse Products":

    section_title(
        "Product Explorer",
        "Search and explore the Sahara product specification database."
    )

    st.text_input("Search products", placeholder="Enter product name or product code...")

    st.info("Product database integration will be connected in the functionality phase.")


elif page == "Specification Viewer":

    section_title(
        "Specification Viewer",
        "Access original product specification documents."
    )

    st.info("Original PDF viewer integration will be connected in the functionality phase.")


elif page == "AI Assistant":

    section_title(
        "AI Specification Assistant",
        "Ask questions about product specifications and documented values."
    )

    st.markdown("""
    <div style="background:#10233D;padding:22px;border-radius:14px;
        border:1px solid rgba(214,173,85,.2);">
        <div style="font-size:17px;font-weight:700;color:#F5F7FB;">
            Specification Intelligence
        </div>
        <div style="font-size:12px;color:#91A2B9;margin-top:7px;">
            Ask about aflatoxin, allergens, moisture, nutritional values,
            origin or other specification fields.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.text_area(
        "Your question",
        placeholder="Example: What are the aflatoxin B1 and total aflatoxin values?"
    )

    st.button("Analyse Specification", use_container_width=True)

    st.caption("Design preview only. No specification answers are generated in this prototype.")


elif page == "Product Comparison":

    section_title(
        "Product Comparison",
        "Compare specification information across selected products."
    )

    x, y = st.columns(2)

    with x:
        st.selectbox("First product", ["Select product"])

    with y:
        st.selectbox("Second product", ["Select product"])

    st.info("Comparison engine will be connected in the functionality phase.")


elif page == "Compliance Hub":

    section_title(
        "Compliance Intelligence",
        "Review documented product declarations and compliance information."
    )

    a, b = st.columns(2)

    with a:
        feature_card("✓", "Allergen Declarations",
                     "Review contains, may contain and free-from declarations.")

    with b:
        feature_card("◈", "Quality Parameters",
                     "Review documented quality and analytical specification fields.")

    st.info("Compliance data will be connected in the functionality phase.")


elif page == "Downloads":

    section_title(
        "Document Centre",
        "Access product specification documents and available exports."
    )

    st.info("Document library integration will be connected in the functionality phase.")


elif page == "About Sahara":

    section_title(
        "About Sahara UK Foods",
        "Product specification intelligence workspace."
    )

    st.markdown("""
    <div style="background:#10233D;border:1px solid rgba(214,173,85,.2);
        border-radius:15px;padding:28px;">
        <div style="font-size:28px;font-weight:800;color:#F5F7FB;">
            SAHARA <span style="color:#D6AD55;">UK FOODS</span>
        </div>
        <div style="font-size:12px;color:#91A2B9;margin-top:15px;">
            Specification Intelligence Workspace
        </div>
        <div style="font-size:13px;color:#C3D0DF;line-height:1.8;
                    margin-top:20px;">
            A central workspace designed to make product specification
            information easier to access, understand and manage.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- FOOTER --------------------

st.markdown("""
<div style="
    margin-top:45px;
    padding:17px 0 5px 0;
    border-top:1px solid rgba(214,173,85,.15);
    text-align:center;
    color:#647991;
    font-size:9px;
    letter-spacing:1.5px;">
    SAHARA UK FOODS LTD &nbsp; · &nbsp;
    SPECIFICATION INTELLIGENCE &nbsp; · &nbsp;
    ENGLISH INTERFACE
</div>
""", unsafe_allow_html=True)
