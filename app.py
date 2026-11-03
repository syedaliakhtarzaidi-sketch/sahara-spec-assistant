
import streamlit as st

st.set_page_config(
    page_title="SAHARA | Product Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# SAHARA UK FOODS — PREMIUM DESIGN SYSTEM
# ==================================================

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

.stApp {
    background: var(--cream);
    color: var(--text);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
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

/* BRAND */

.brand {
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
}

/* NAVIGATION */

.top-nav {
    display: flex;
    justify-content: flex-end;
    gap: 25px;
    align-items: center;
    padding-top: 12px;
    color: #59645D;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
}

.nav-active {
    color: var(--green);
    border-bottom: 2px solid var(--gold);
    padding-bottom: 8px;
}

/* HERO */

.hero {
    background: var(--dark);
    border-radius: 4px;
    min-height: 410px;
    height: 410px;
}

.hero-inner {
    padding: 48px 42px;
    color: white;
}

.eyebrow {
    color: #D1B98B;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(35px, 4vw, 58px);
    line-height: 1.13;
    color: #F8F5ED;
    font-weight: 500;
    margin: 25px 0 17px;
}

.hero-copy {
    font-size: 13px;
    color: #D0D9D2;
    line-height: 1.9;
    max-width: 430px;
}

.hero-note {
    margin-top: 30px;
    font-size: 10px;
    letter-spacing: 2px;
    color: #D1B98B;
    font-weight: 600;
}

/* SECTIONS */

.section-kicker {
    color: var(--gold);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 33px;
    font-weight: 500;
    color: var(--green);
    margin-top: 7px;
}

.section-description {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.8;
}

/* CATEGORY */

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
    min-height: 65px;
}

.category-line {
    height: 1px;
    background: #D9D5C9;
    margin-top: 15px;
}

/* WORKSPACE */

.workspace {
    background: white;
    border: 1px solid #E8E4D9;
    padding: 25px;
    min-height: 190px;
}

.workspace-title {
    font-family: 'Playfair Display', serif;
    color: var(--green);
    font-size: 21px;
}

.workspace-copy {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.8;
}

/* BRAND STATEMENT */

.brand-statement {
    background: var(--green);
    padding: 42px 25px;
    text-align: center;
    border-radius: 3px;
}

.statement-title {
    font-family: 'Playfair Display', serif;
    color: #F6F2E8;
    font-size: 30px;
}

.statement-subtitle {
    color: #D0C3A7;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 12px;
}

/* FOOTER */

.footer {
    border-top: 1px solid #DCD8CE;
    padding-top: 22px;
    margin-top: 50px;
    color: #85877E;
    font-size: 10px;
    letter-spacing: 1px;
}

div[data-testid="stImage"] img {
    border-radius: 3px;
    object-fit: cover;
}

@media(max-width: 700px) {
    .hero-inner {
        padding: 30px 22px;
    }

    .section-title {
        font-size: 27px;
    }

    .top-nav {
        gap: 10px;
        font-size: 8px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

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


# ==================================================
# HERO
# ==================================================

hero_left, hero_right = st.columns([1.05, 0.95], gap="small")

with hero_left:
    st.markdown("""
    <div class="hero">
        <div class="hero-inner">
            <div class="eyebrow">
                SAHARA PRODUCT INTELLIGENCE
            </div>

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
        use_container_width=True
    )


# ==================================================
# PRODUCT COLLECTION
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">
    OUR PRODUCT COLLECTION
</div>

<div class="section-title">
    Explore our world of ingredients
</div>

<div class="section-description">
    Carefully sourced products. Detailed specifications.
    A complete view of the ingredients we trade.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ==================================================
# CATEGORY CARDS
# ==================================================

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
        st.image(
            item["image"],
            use_container_width=True
        )

        st.markdown(
            f'<div class="category-name">{item["name"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="category-copy">{item["description"]}</div>'
            '<div class="category-line"></div>',
            unsafe_allow_html=True
        )


# ==================================================
# INTELLIGENCE WORKSPACE
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-kicker">
    THE SAHARA WORKSPACE
</div>

<div class="section-title">
    Everything about your product. In one place.
</div>

<div class="section-description">
    A unified environment for specifications, quality
    information and supporting documents.
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


# ==================================================
# BRAND STATEMENT
# ==================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="brand-statement">
    <div class="statement-title">
        Quality begins with knowing.
    </div>

    <div class="statement-subtitle">
        SAHARA UK FOODS
    </div>
</div>
""", unsafe_allow_html=True)


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    <span>SAHARA UK FOODS LTD</span>
    <span style="float:right;">
        PRODUCT INTELLIGENCE PLATFORM
    </span>
</div>
""", unsafe_allow_html=True)
