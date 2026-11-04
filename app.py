
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# SAHARA UK FOODS | SAHARA SIGNATURE
# PREMIUM AI INTELLIGENCE PLATFORM
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | AI Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DESIGN SYSTEM --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0C1711;
    --sidebar: #101F16;
    --panel: #17291E;
    --panel2: #1B3023;
    --border: #294332;
    --lime: #A6D936;
    --lime2: #C1EA65;
    --white: #F4F5EF;
    --muted: #A1B1A3;
}

.stApp {
    background: var(--bg);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.stAppToolbar {
    visibility: hidden;
}

section[data-testid="stSidebar"] {
    background: var(--sidebar);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* BRAND */

.brand-logo {
    font-family: 'Manrope', sans-serif;
    font-size: 31px;
    font-weight: 800;
    letter-spacing: 3px;
    color: var(--lime);
    line-height: 1;
}

.brand-subtitle {
    font-size: 10px;
    letter-spacing: 4px;
    color: #DCE7D9;
    margin-top: 8px;
}

.brand-caption {
    color: #819487;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 15px;
}

/* SIDEBAR */

.sidebar-label {
    color: #809487;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 32px;
    margin-bottom: 12px;
}

.sidebar-bottom {
    border-top: 1px solid var(--border);
    margin-top: 35px;
    padding-top: 20px;
    color: #819487;
    font-size: 11px;
    line-height: 2;
}

/* HEADER */

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 22px;
}

.top-label {
    color: #A6B5A7;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: 700;
}

.system-status {
    color: var(--lime);
    font-size: 10px;
    letter-spacing: 1.5px;
    border: 1px solid #45652E;
    background: #1A3020;
    border-radius: 30px;
    padding: 8px 15px;
}

/* HERO */

.hero {
    background:
        radial-gradient(circle at 90% 10%, rgba(166,217,54,0.13), transparent 30%),
        linear-gradient(115deg, #183523 0%, #14291D 55%, #1B3422 100%);
    border: 1px solid #36543C;
    border-radius: 20px;
    padding: 48px 45px;
    min-height: 310px;
    position: relative;
    overflow: hidden;
}

.hero-tag {
    color: var(--lime);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 20px;
}

.hero-title {
    color: var(--white);
    font-family: 'Manrope', sans-serif;
    font-size: clamp(32px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.16;
    letter-spacing: -1.8px;
}

.hero-text {
    color: #B8C9BA;
    font-size: 14px;
    line-height: 1.8;
    max-width: 620px;
    margin-top: 18px;
}

.hero-company {
    color: var(--lime);
    font-size: 10px;
    letter-spacing: 3px;
    margin-top: 25px;
    font-weight: 700;
}

/* SECTION */

.section-heading {
    color: var(--white);
    font-family: 'Manrope', sans-serif;
    font-size: 21px;
    font-weight: 800;
    margin-top: 34px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 18px;
}

/* PANELS */

.panel {
    background: linear-gradient(145deg, #1B3023, #15271C);
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 22px;
    min-height: 170px;
    margin-bottom: 14px;
    transition: all .2s ease;
}

.panel:hover {
    border-color: var(--lime);
    background: #203727;
}

.panel-icon {
    color: var(--lime);
    font-size: 26px;
    margin-bottom: 16px;
}

.panel-title {
    color: var(--white);
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 9px;
}

.panel-description {
    color: #A7B7A9;
    font-size: 12px;
    line-height: 1.7;
}

/* WORKSPACE */

.workspace {
    background: #14251B;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 25px;
    margin-top: 14px;
}

.workspace-title {
    font-family: 'Manrope', sans-serif;
    font-size: 19px;
    font-weight: 800;
    color: var(--white);
}

.workspace-description {
    color: var(--muted);
    font-size: 12px;
    margin-top: 7px;
}

/* INPUTS */

.stTextInput input {
    background: #0E1D14 !important;
    border: 1px solid #38523D !important;
    border-radius: 10px !important;
    color: white !important;
    min-height: 48px;
}

.stTextInput input:focus {
    border-color: var(--lime) !important;
    box-shadow: 0 0 0 1px var(--lime) !important;
}

.stButton button {
    background: var(--lime) !important;
    color: #132018 !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 800 !important;
    min-height: 43px;
    padding: 0 23px;
}

.stButton button:hover {
    background: var(--lime2) !important;
    color: #132018 !important;
}

div[data-testid="stRadio"] label {
    color: #D7E2D7;
    font-size: 13px;
}

.stAlert {
    border-radius: 10px;
}

/* FOOTER */

.footer {
    border-top: 1px solid var(--border);
    margin-top: 35px;
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    color: #849688;
    font-size: 9px;
    letter-spacing: 1.5px;
}

div[data-testid="stMarkdownContainer"] p {
    margin-bottom: 0;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -------------------- HTML HELPER --------------------

def render_html(html):
    st.markdown(html, unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

with st.sidebar:

    render_html("""
    <div style="padding: 8px 5px 25px 5px;">
        <div class="brand-logo">SAHARA.</div>
        <div class="brand-subtitle">UK FOODS</div>
        <div class="brand-caption">INTELLIGENCE PLATFORM</div>
    </div>

    <div class="sidebar-label">MAIN WORKSPACE</div>
    """)

    page = st.radio(
        "Navigation",
        [
            "AI Intelligence",
            "Product Intelligence",
            "Quality Analysis",
            "Allergen Intelligence",
            "Nutrition Analysis",
            "Compliance Centre"
        ],
        label_visibility="collapsed",
        key="main_navigation"
    )

    render_html("""
    <div class="sidebar-label">RESOURCES</div>
    """)

    resource = st.radio(
        "Resources",
        [
            "Knowledge Library",
            "Document Centre",
            "Settings"
        ],
        label_visibility="collapsed",
        key="resource_navigation"
    )

    render_html("""
    <div class="sidebar-bottom">
        <div style="color:#A6D936;font-weight:700;">
            SAHARA AI SYSTEM
        </div>
        <div>Version 1.0</div>
        <div>Premium Intelligence Workspace</div>
    </div>
    """)


# -------------------- TOP HEADER --------------------

render_html("""
<div class="top-header">
    <div class="top-label">
        SAHARA SIGNATURE / INTELLIGENCE
    </div>
    <div class="system-status">
        ● SYSTEM ONLINE
    </div>
</div>
""")


# -------------------- HERO SECTION --------------------

if page == "AI Intelligence":

    render_html("""
    <div class="hero">
        <div class="hero-tag">
            SAHARA AI INTELLIGENCE
        </div>

        <div class="hero-title">
            Intelligence behind<br>
            every ingredient.
        </div>

        <p class="hero-text">
            Your central workspace for product specifications,
            food quality intelligence, technical documentation
            and compliance analysis.
        </p>

        <div class="hero-company">
            SAHARA UK FOODS
        </div>
    </div>
    """)

    # -------------------- AI WORKSPACE --------------------

    render_html("""
    <div class="section-heading">
        AI Intelligence Workspace
    </div>

    <div class="workspace">
        <div class="workspace-title">
            What would you like to analyse?
        </div>

        <div class="workspace-description">
            Ask questions about product specifications,
            quality parameters, allergens or compliance documents.
        </div>
    </div>
    """)

    question = st.text_input(
        "Your question",
        placeholder="e.g. What is the aflatoxin level in this product?",
        label_visibility="collapsed",
        key="sahara_question"
    )

    if st.button("Start Analysis", key="start_analysis"):
        if question.strip():
            st.info(
                "Design preview: The AI analysis engine has not yet "
                "been connected. Your question was received."
            )
        else:
            st.warning("Please enter a question first.")

    # -------------------- MODULES --------------------

    render_html("""
    <div class="section-heading">
        Intelligence Modules
    </div>

    <div class="section-subtitle">
        Explore the specialist intelligence areas of Sahara UK Foods.
    </div>
    """)

    modules = [
        (
            "◈",
            "Product Intelligence",
            "Explore product specifications and technical documents."
        ),
        (
            "▤",
            "Nutrition Analysis",
            "Review nutritional values and product comparisons."
        ),
        (
            "✧",
            "Quality Analysis",
            "Analyse aflatoxin, moisture and microbiological parameters."
        ),
        (
            "⬡",
            "Compliance Centre",
            "Review food safety documentation and compliance evidence."
        ),
        (
            "◇",
            "Allergen Intelligence",
            "Review allergen declarations and product risks."
        ),
        (
            "⌘",
            "Knowledge Library",
            "Access the central product and document knowledge base."
        )
    ]

    cols = st.columns(3)

    for i, (icon, title, description) in enumerate(modules):
        with cols[i % 3]:
            render_html(f"""
            <div class="panel">
                <div class="panel-icon">{icon}</div>
                <div class="panel-title">{title}</div>
                <div class="panel-description">
                    {description}
                </div>
            </div>
            """)


# -------------------- OTHER NAVIGATION PAGES --------------------

elif page == "Product Intelligence":
    render_html("""
    <div class="hero">
        <div class="hero-tag">PRODUCT INTELLIGENCE</div>
        <div class="hero-title">Product knowledge.<br>One workspace.</div>
        <p class="hero-text">
            Explore product specifications, origins and technical documents.
        </p>
    </div>
    """)
    st.info("Product database integration will be connected in the next development phase.")

elif page == "Quality Analysis":
    render_html("""
    <div class="hero">
        <div class="hero-tag">QUALITY INTELLIGENCE</div>
        <div class="hero-title">Quality you can<br>verify.</div>
        <p class="hero-text">
            Review aflatoxin, moisture and microbiological parameters.
        </p>
    </div>
    """)
    st.info("Quality document analysis will be connected in the next development phase.")

elif page == "Allergen Intelligence":
    render_html("""
    <div class="hero">
        <div class="hero-tag">ALLERGEN INTELLIGENCE</div>
        <div class="hero-title">Understand every<br>ingredient.</div>
        <p class="hero-text">
            Review allergen declarations and product risk information.
        </p>
    </div>
    """)
    st.info("Allergen analysis will be connected in the next development phase.")

elif page == "Nutrition Analysis":
    render_html("""
    <div class="hero">
        <div class="hero-tag">NUTRITION INTELLIGENCE</div>
        <div class="hero-title">Nutrition data.<br>Clear insights.</div>
        <p class="hero-text">
            Review nutritional values and compare product information.
        </p>
    </div>
    """)
    st.info("Nutrition analysis will be connected in the next development phase.")

elif page == "Compliance Centre":
    render_html("""
    <div class="hero">
        <div class="hero-tag">COMPLIANCE CENTRE</div>
        <div class="hero-title">Documentation<br>with confidence.</div>
        <p class="hero-text">
            Review food safety documents and compliance evidence.
        </p>
    </div>
    """)
    st.info("Compliance document analysis will be connected in the next development phase.")


# -------------------- RESOURCE PAGES --------------------

if resource == "Knowledge Library":
    if page == "AI Intelligence":
        pass
    else:
        st.info("Knowledge Library integration is planned for the next phase.")

elif resource == "Document Centre":
    st.info("Document Centre integration is planned for the next phase.")

elif resource == "Settings":
    st.info("Platform settings will be available in a future update.")


# -------------------- FOOTER --------------------

render_html("""
<div class="footer">
    <span>SAHARA UK FOODS</span>
    <span>INTELLIGENCE PLATFORM</span>
    <span>VERSION 1.0</span>
</div>
""")
