
import streamlit as st

st.set_page_config(
    page_title="Sahara | AI Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# SAHARA SIGNATURE — PREMIUM DESIGN
# =====================================================

st.markdown("""
<style>

/* MAIN APPLICATION */
.stApp {
    background: #101B15;
    color: #F4F5EF;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #14251C;
    border-right: 1px solid #2A4031;
}

section[data-testid="stSidebar"] * {
    color: #E8EEE7;
}

.brand {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #A6D936;
}

.brand-sub {
    color: #9CAEA0;
    font-size: 11px;
    letter-spacing: 3px;
    margin-top: -5px;
}

.nav-label {
    color: #839589;
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 12px;
}

/* HEADINGS */
.eyebrow {
    color: #A6D936;
    font-size: 11px;
    letter-spacing: 3px;
    font-weight: 700;
}

.main-heading {
    font-size: 39px;
    font-weight: 750;
    color: #F4F5EF;
    line-height: 1.2;
    margin-top: 8px;
}

.sub-heading {
    color: #9DADA2;
    font-size: 14px;
    line-height: 1.7;
}

/* HERO */
.hero {
    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(166,217,54,0.15),
            transparent 35%
        ),
        linear-gradient(120deg, #1C3527, #17281E 70%);
    border: 1px solid #35513A;
    border-radius: 22px;
    padding: 34px;
    margin-top: 25px;
    margin-bottom: 25px;
}

.hero-title {
    color: #FFFFFF;
    font-size: 29px;
    font-weight: 750;
}

.hero-text {
    color: #B8C7B9;
    font-size: 14px;
    line-height: 1.8;
}

.hero-tag {
    display: inline-block;
    background: rgba(166,217,54,0.13);
    color: #B8E66A;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 11px;
    letter-spacing: 1px;
    margin-bottom: 16px;
}

/* CARDS */
.panel {
    background: #1A2B21;
    border: 1px solid #304638;
    border-radius: 17px;
    padding: 21px;
    min-height: 145px;
    margin-bottom: 14px;
}

.panel-title {
    color: #EAF0E8;
    font-size: 15px;
    font-weight: 700;
}

.panel-description {
    color: #9DADA2;
    font-size: 12px;
    line-height: 1.7;
    margin-top: 8px;
}

.panel-icon {
    font-size: 23px;
    margin-bottom: 13px;
}

/* SECTION */
.section-heading {
    color: #F1F4ED;
    font-size: 19px;
    font-weight: 700;
    margin-top: 22px;
    margin-bottom: 15px;
}

/* STATUS */
.status {
    color: #B5E36B;
    font-size: 11px;
    background: #263E2B;
    border: 1px solid #45663D;
    border-radius: 20px;
    padding: 6px 12px;
}

/* INPUT */
.stTextInput input,
.stTextArea textarea {
    background: #192B20 !important;
    color: #F4F5EF !important;
    border: 1px solid #3B5541 !important;
    border-radius: 12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #A6D936 !important;
    box-shadow: 0 0 0 1px #A6D936 !important;
}

/* BUTTON */
.stButton button {
    background: #A6D936;
    color: #142016;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 10px 18px;
    transition: 0.2s;
}

.stButton button:hover {
    background: #B9EB51;
    color: #142016;
    border: none;
}

/* DIVIDER */
hr {
    border-color: #304638;
}

/* HIDE STREAMLIT BRANDING */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("""
    <div style="padding:10px 0 25px 0;">
        <div class="brand">SAHARA<span style="color:white;">.</span></div>
        <div class="brand-sub">UK FOODS</div>
        <div style="color:#718B77;font-size:10px;margin-top:12px;">
            INTELLIGENCE PLATFORM
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-label">WORKSPACE</div>',
                unsafe_allow_html=True)

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
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown('<div class="nav-label">SYSTEM</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div style="color:#A4B3A6;font-size:12px;line-height:2.3;">
        ◈ Knowledge Library<br>
        ◈ Document Centre<br>
        ◈ Settings
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style="font-size:11px;color:#829486;">
        SAHARA UK FOODS<br>
        <span style="color:#A6D936;">●</span> Intelligence Workspace
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# TOP HEADER
# =====================================================

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <div class="eyebrow">SAHARA SIGNATURE / INTELLIGENCE</div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align:right;">
        <span class="status">● SYSTEM ONLINE</span>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# MAIN HERO
# =====================================================

st.markdown("""
<div class="hero">

    <div class="hero-tag">SAHARA AI INTELLIGENCE</div>

    <div class="hero-title">
        Intelligence behind<br>
        every ingredient.
    </div>

    <p class="hero-text">
        Your central workspace for product specifications,
        food quality intelligence, technical documentation
        and compliance analysis.
    </p>

    <div style="
        color:#A6D936;
        font-size:11px;
        letter-spacing:2px;
        margin-top:25px;
        font-weight:700;">
        SAHARA UK FOODS
    </div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# AI WORKSPACE
# =====================================================

st.markdown('<div class="section-heading">AI Intelligence Workspace</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="panel" style="min-height:100px;">
    <div class="panel-title">What would you like to analyse?</div>
    <div class="panel-description">
        Ask questions about product specifications,
        quality parameters, allergens or compliance documents.
    </div>
</div>
""", unsafe_allow_html=True)

question = st.text_area(
    "Ask Sahara AI",
    placeholder="Example: Analyse aflatoxin levels in this product specification...",
    height=100,
    label_visibility="collapsed"
)

if st.button("✦  Start Analysis", use_container_width=True):
    if question.strip():
        st.info(
            "Design preview only. The AI analysis engine "
            "will be connected to your existing product and PDF database."
        )
    else:
        st.warning("Please enter a question first.")


# =====================================================
# INTELLIGENCE MODULES
# =====================================================

st.markdown('<div class="section-heading">Intelligence Modules</div>',
            unsafe_allow_html=True)

modules = [
    ("◈", "Product Intelligence",
     "Explore product specifications and technical documents."),

    ("✧", "Quality Analysis",
     "Analyse aflatoxin, moisture and microbiological parameters."),

    ("◇", "Allergen Intelligence",
     "Review allergen declarations and product risks."),

    ("▤", "Nutrition Analysis",
     "Review nutritional values and product comparisons."),

    ("⬡", "Compliance Centre",
     "Review food safety documentation and compliance evidence."),

    ("⌘", "Knowledge Library",
     "Access the central product and document knowledge base.")
]

cols = st.columns(3)

for i, module in enumerate(modules):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="panel">

            <div class="panel-icon">{module[0]}</div>

            <div class="panel-title">{module[1]}</div>

            <div class="panel-description">
                {module[2]}
            </div>

        </div>
        """, unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div style="
    display:flex;
    justify-content:space-between;
    color:#718578;
    font-size:10px;
    letter-spacing:1px;">

    <span>SAHARA UK FOODS</span>

    <span>INTELLIGENCE PLATFORM</span>

    <span>VERSION 1.0</span>

</div>
""", unsafe_allow_html=True)
