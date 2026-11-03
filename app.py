
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SAHARA | Product Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# SAHARA DESIGN SYSTEM
# --------------------------------------------------

GREEN = "#19382F"
DARK = "#122A23"
GOLD = "#B69A68"
CREAM = "#F6F4EE"
TEXT = "#252B27"
MUTED = "#777D75"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

:root {
    --green: #19382F;
    --dark: #122A23;
    --gold: #B69A68;
    --cream: #F6F4EE;
    --text: #252B27;
    --muted: #777D75;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
}

.stApp {
    background: var(--cream);
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1440px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

/* Header */

.brand {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
    font-size: 29px;
    letter-spacing: 5px;
    color: var(--green);
}

.brand-sub {
    color: var(--gold);
    font-size: 9px;
    letter-spacing: 3px;
    font-weight: 600;
    margin-top: -3px;
}

.top-nav {
    display: flex;
    justify-content: flex-end;
    gap: 30px;
    align-items: center;
    padding-top: 12px;
    color: #59645D;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1px;
}

.nav-active {
    color: var(--green);
    border-bottom: 2px solid var(--gold);
    padding-bottom: 8px;
}

/* Hero */

.hero {
    background: var(--dark);
    border-radius: 5px;
    overflow: hidden;
    margin-top: 25px;
    position: relative;
    min-height: 420px;
}

.hero-inner {
    padding: 58px 55px;
    color: white;
}

.eyebrow {
    color: #D1B98B;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(38px, 5vw, 65px);
    line-height: 1.12;
    color: #F8F5ED;
    font-weight: 500;
    margin: 24px 0 17px 0;
}

.hero-copy {
    font-size: 14px;
    color: #D0D9D2;
    line-height: 1.9;
    max-width: 440px;
}

.hero-note {
    margin-top: 34px;
    font-size: 10px;
    letter-spacing: 2px;
    color: #D1B98B;
    font-weight: 600;
}

/* Section */

.section-kicker {
    color: var(--gold);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    font-weight: 500;
    color: var(--green);
    margin-top: 7px;
}

.section-description {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.8;
}

/* Category cards */

.category-name {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--green);
    margin-top: 13px;
}

.category-copy {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
}

.category-line {
    height: 1px;
    background: #D9D5C9;
    margin-top: 15px;
}

/* Workspace */

.workspace {
    background: white;
    border: 1px solid #E8E4D9;
    padding: 28px;
    min-height: 190px;
}

.workspace-title {
    font-family: 'Playfair Display', serif;
    color: var(--green);
    font-size: 22px;
}

.workspace-copy {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.8;
}

/* Footer */

.footer {
    border-top: 1px solid #DCD8CE;
    padding-top: 22px;
    margin-top: 55px;
    color: #85877E;
    font-size: 10px;
    letter-spacing: 1px;
}

/* Buttons */

.stButton > button {
    background: var(--green);
    color: white;
    border: 1px solid var(--green);
    border-radius: 2px;
    padding: 12px 24px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    min-height: 43px;
}

.stButton > button:hover {
    background: #294D40;
    border-color: #294D40;
    color: white;
}

div[data-testid="stImage"] img {
    border-radius: 2px;
}

hr {
    border-color: #DEDACF;
}

@media(max-width: 700px) {
    .hero-inner {
        padding: 35px 25px;
    }
    .section-title {
        font-size: 28px;
    }
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

header_left, header_right = st.columns([1, 2])

with header_left:
    st.markdown("""
    <div class="brand">SAHARA</div>
    <div class="brand-sub">UK FOODS · EST. 2017</div>
    """, unsafe_allow_html=True)

with header_right:
    st.markdown("""
    <div class="top-nav">
        <span class="nav-active">OVERVIEW</span>
        <span>PRODUCTS</span>
        <span>SPECIFICATIONS</span>
        <span>INTELLIGENCE</span>
        <span>DOCUMENTS</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# HERO
# --------------------------------------------------

hero_left, hero_right = st.columns([1.05, 0.95], gap="small")

with hero_left:
    st.markdown("""
    <div class="hero" style="height:420px;">
        <div class="hero-inner">
            <div class="eyebrow">SAHARA PRODUCT INTELLIGENCE</div>
            <div class="hero-title">
                Naturally<br>
                exceptional.<br>
                Precisely specified.
            </div>
            <div class="hero-copy">
                A smarter way to understand product quality,
                specifications and documentation across
                our global food portfolio.
            </div>
            <div class="hero-note">
                QUALITY · TRANSPARENCY · CONFIDENCE
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.image(
        "https://images.unsplash.com/photo-1601493700631-2b16ec4b4716",
        use_container_width=True,
        height=420
    )


# --------------------------------------------------
# INTRODUCTION
# --------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">OUR PRODUCT COLLECTION</div>
<div class="section-title">Explore our world of ingredients</div>
<div class="section-description">
Carefully sourced products. Detailed specifications.
A complete view of the ingredients we trade.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# PRODUCT CATEGORIES
# --------------------------------------------------

categories = [
    {
        "name": "Dates",
        "description": "Premium varieties, pitted dates, chopped dates and date ingredients.",
        "image": "https://images.unsplash.com/photo-1596591606975-97ee5cef3a1e"
    },
    {
        "name": "Nuts",
        "description": "Almonds, pistachios, walnuts, cashews and more.",
        "image": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46"
    },
    {
        "name": "Dried Fruits",
        "description": "Apricots, figs, raisins and carefully selected dried fruits.",
        "image": "https://images.unsplash.com/photo-1596591606975-97ee5cef3a1e"
    },
    {
        "name": "Ingredients",
        "description": "Date paste, date syrup and other food manufacturing ingredients.",
        "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950"
    }
]

cols = st.columns(4, gap="medium")

for col, item in zip(cols, categories):
    with col:
        st.image(item["image"], use_container_width=True)
        st.markdown(
            f'<div class="category-name">{item["name"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="category-copy">{item["description"]}</div>'
            '<div class="category-line"></div>',
            unsafe_allow_html=True
        )


# --------------------------------------------------
# INTELLIGENCE WORKSPACE
# --------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">THE SAHARA WORKSPACE</div>
<div class="section-title">Everything about your product. In one place.</div>
<div class="section-description">
A unified environment for specifications, quality information
and supporting documents.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

w1, w2, w3 = st.columns(3, gap="medium")

with w1:
    st.markdown("""
    <div class="workspace">
        <div class="section-kicker">01 · PRODUCT DATA</div>
        <div class="workspace-title">Product Catalogue</div>
        <p class="workspace-copy">
        Browse products, identify product codes and access
        the relevant specification records.
        </p>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class="workspace">
        <div class="section-kicker">02 · DOCUMENTATION</div>
        <div class="workspace-title">Specification Library</div>
        <p class="workspace-copy">
        Access original product specifications, technical
        documents and supporting PDF files.
        </p>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class="workspace">
        <div class="section-kicker">03 · ANALYSIS</div>
        <div class="workspace-title">Product Intelligence</div>
        <p class="workspace-copy">
        Find documented quality values, allergens,
        nutritional information and compliance evidence.
        </p>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# BRAND STATEMENT
# --------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:#19382F;
    padding:42px 35px;
    text-align:center;
    border-radius:3px;
">
    <div style="
        font-family:'Playfair Display',serif;
        color:#F6F2E8;
        font-size:30px;
    ">
        Quality begins with knowing.
    </div>
    <div style="
        color:#D0C3A7;
        font-size:11px;
        letter-spacing:2px;
        margin-top:12px;
    ">
        SAHARA UK FOODS
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    <span>SAHARA UK FOODS LTD</span>
    <span style="float:right;">PRODUCT INTELLIGENCE PLATFORM</span>
</div>
""", unsafe_allow_html=True)
