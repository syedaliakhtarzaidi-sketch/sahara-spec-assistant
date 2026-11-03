
import streamlit as st

# ==========================================
# SAHARA UK FOODS
# CLEAN FOOD SCIENCE THEME
# ==========================================

st.set_page_config(
    page_title="Sahara | Food Science Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# THEME CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --background: #17251F;
    --surface: #22352B;
    --surface-light: #293D32;
    --border: #405247;
    --gold: #D4B879;
    --white: #F1F0E9;
    --muted: #B8C5BB;
}

.stApp {
    background-color: var(--background);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

[data-testid="stSidebar"] {
    background-color: #14221B;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--white);
}

h1, h2, h3 {
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
}

p {
    color: var(--muted);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 28px;
}

.brand-logo {
    width: 43px;
    height: 43px;
    border-radius: 10px;
    background: var(--gold);
    color: #17251F;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    font-weight: 800;
}

.brand-name {
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 2px;
    color: var(--white);
}

.brand-sub {
    font-size: 9px;
    letter-spacing: 1.5px;
    color: var(--muted);
}

.eyebrow {
    color: var(--gold);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-title {
    font-size: 36px;
    font-weight: 700;
    letter-spacing: -1px;
    margin-top: 8px;
    color: var(--white);
}

.hero-description {
    font-size: 14px;
    color: var(--muted);
    margin-top: 6px;
    line-height: 1.7;
}

.divider {
    height: 1px;
    background: var(--border);
    margin: 24px 0;
}

.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 19px;
    min-height: 110px;
}

.metric-label {
    font-size: 10px;
    letter-spacing: 1.5px;
    color: var(--muted);
    font-weight: 700;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: var(--gold);
    margin-top: 9px;
}

.metric-description {
    font-size: 11px;
    color: var(--muted);
    margin-top: 3px;
}

.content-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 14px;
}

.card-heading {
    font-size: 16px;
    font-weight: 700;
    color: var(--white);
}

.card-description {
    font-size: 12px;
    color: var(--muted);
    margin-top: 6px;
}

div[data-testid="stTextInput"] input {
    background: var(--surface) !important;
    color: var(--white) !important;
    border: 1px solid var(--border) !important;
    border-radius: 9px !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: var(--surface) !important;
}

.stButton button {
    background: var(--gold);
    color: #17251F;
    border: none;
    border-radius: 8px;
    font-weight: 700;
}

.stButton button:hover {
    background: #E5CB92;
    color: #17251F;
}

hr {
    border-color: var(--border);
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-logo">S</div>
        <div>
            <div class="brand-name">SAHARA</div>
            <div class="brand-sub">FOOD SCIENCE INTELLIGENCE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        '<div class="eyebrow">MAIN MENU</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Product Database",
            "Product Specifications",
            "Quality & Compliance",
            "Document Library"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        '<div class="eyebrow">PRODUCT CATEGORIES</div>',
        unsafe_allow_html=True
    )

    st.radio(
        "Categories",
        [
            "All Products",
            "Dates",
            "Dried Fruits",
            "Nuts",
            "Seeds & Oils",
            "Spices & Herbs",
            "Pulses & Flours"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("""
    <div style="font-size:11px;color:#B8C5BB;line-height:2">
        SAHARA UK FOODS LTD<br>
        Internal Workspace<br>
        <span style="color:#D4B879">FOOD QUALITY INTELLIGENCE</span>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MAIN HEADER
# ==========================================

st.markdown("""
<div class="eyebrow">SAHARA UK FOODS / WORKSPACE</div>

<div class="hero-title">
    Food Science Intelligence
</div>

<div class="hero-description">
    Product specifications, quality analysis and technical documentation.
</div>

<div class="divider"></div>
""", unsafe_allow_html=True)


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.markdown("### Overview")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("PRODUCT DATABASE", "—", "Awaiting data connection"),
        ("SPECIFICATION FILES", "—", "Awaiting data connection"),
        ("QUALITY PARAMETERS", "—", "Awaiting data connection"),
        ("DOCUMENT LIBRARY", "—", "Awaiting data connection")
    ]

    for col, metric in zip([c1, c2, c3, c4], metrics):

        with col:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{metric[0]}</div>
                <div class="metric-value">{metric[1]}</div>
                <div class="metric-description">{metric[2]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([1.4, 1])

    with left:

        st.markdown("""
        <div class="content-card">
            <div class="eyebrow">PRODUCT MANAGEMENT</div>
            <div class="card-heading" style="margin-top:10px">
                Product Database
            </div>
            <div class="card-description">
                Centralised product information and technical specifications.
            </div>
        </div>
        """, unsafe_allow_html=True)

        search = st.text_input(
            "Search",
            placeholder="Search product name, code or specification...",
            label_visibility="collapsed"
        )

        st.info(
            "Product database connection will be added in the next development phase."
        )

    with right:

        st.markdown("""
        <div class="content-card">
            <div class="eyebrow">QUALITY INTELLIGENCE</div>
            <div class="card-heading" style="margin-top:10px">
                Technical Modules
            </div>
            <div class="card-description">
                Core areas of food quality and specification management.
            </div>
        </div>
        """, unsafe_allow_html=True)

        modules = [
            "Chemical Analysis",
            "Physical Specifications",
            "Aflatoxin Analysis",
            "Microbiological Parameters",
            "Allergen Information",
            "Nutritional Analysis",
            "Compliance & Certificates"
        ]

        for module in modules:
            st.markdown(
                f"""
                <div style="
                    background:#22352B;
                    border:1px solid #405247;
                    border-radius:8px;
                    padding:11px 13px;
                    margin-bottom:8px;
                    color:#F1F0E9;
                    font-size:13px;
                ">
                    {module}
                </div>
                """,
                unsafe_allow_html=True
            )


# ==========================================
# OTHER PAGES - TEMPORARY PLACEHOLDERS
# ==========================================

else:

    st.markdown(f"### {page}")

    st.markdown(f"""
    <div class="content-card">
        <div class="eyebrow">SAHARA WORKSPACE</div>
        <div class="card-heading" style="margin-top:10px">
            {page}
        </div>
        <div class="card-description">
            This section will be developed in the next phase.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# FOOTER
# ==========================================

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    color:#91A497;
    font-size:10px;
    letter-spacing:1.5px;
    padding:10px">
    SAHARA UK FOODS LTD &nbsp; | &nbsp; FOOD SCIENCE INTELLIGENCE
</div>
""", unsafe_allow_html=True)
