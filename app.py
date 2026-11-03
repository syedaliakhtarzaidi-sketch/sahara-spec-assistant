
import streamlit as st

# ==========================================================
# SAHARA UK FOODS | PREMIUM FOOD TRADING INTELLIGENCE
# European Luxury B2B Design | Free Streamlit Edition
# ==========================================================

st.set_page_config(
    page_title="Sahara UK Foods | Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------- CSS ----------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap');

:root {
    --cream: #F5F3EC;
    --paper: #FBFAF6;
    --green: #193D32;
    --green2: #285747;
    --gold: #B49A65;
    --brown: #74513A;
    --text: #25352D;
    --muted: #858D81;
    --line: #E7E4D9;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: var(--cream);
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

header[data-testid="stHeader"]::after {
    display: none !important;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.6rem !important;
    padding-bottom: 3rem !important;
}

[data-testid="stToolbar"] {
    right: 1rem;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: var(--green);
    border-right: none;
}

section[data-testid="stSidebar"] > div {
    padding: 1.5rem 1.1rem;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #E9E9DD !important;
}

section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #E9E9DD;
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 9px 10px;
    border-radius: 7px;
    font-size: 13px;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.08);
}

/* Typography */

h1, h2, h3 {
    color: var(--green) !important;
    font-family: 'Playfair Display', serif !important;
}

p {
    color: var(--text);
}

/* Inputs */

.stTextInput input,
.stTextArea textarea {
    background: #FFFDF8 !important;
    border: 1px solid #DEDCCD !important;
    border-radius: 7px !important;
    color: var(--text) !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: var(--green2) !important;
    box-shadow: 0 0 0 1px var(--green2) !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #FFFDF8;
    border-color: #DEDCCD;
    border-radius: 7px;
    color: var(--text);
}

/* Buttons */

.stButton button {
    background: var(--green);
    color: #FFFFFF !important;
    border: 1px solid var(--green);
    border-radius: 6px;
    min-height: 42px;
    font-weight: 600;
    transition: all .2s ease;
}

.stButton button:hover {
    background: var(--green2);
    border-color: var(--green2);
    color: white !important;
    transform: translateY(-1px);
}

/* Dividers */

hr {
    border-color: var(--line) !important;
}

/* Main hero */

.hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 85% 20%, rgba(190,163,103,.22), transparent 27%),
        linear-gradient(115deg, #173C30 0%, #214D3D 65%, #315D48 100%);
    border-radius: 12px;
    padding: 43px 42px;
    min-height: 265px;
    color: white;
    margin: 24px 0 30px 0;
    border: 1px solid rgba(180,154,101,.35);
}

.hero::after {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    right: -85px;
    top: -120px;
    border: 1px solid rgba(225,208,164,.25);
    border-radius: 50%;
    box-shadow:
      0 0 0 25px rgba(255,255,255,.025),
      0 0 0 55px rgba(255,255,255,.02);
}

.hero-eyebrow {
    color: #D8C79D;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(30px, 4vw, 48px);
    line-height: 1.12;
    color: #FFFFFF;
    margin-top: 17px;
    max-width: 650px;
}

.hero-description {
    font-size: 13px;
    color: #D6E0D7;
    margin-top: 15px;
    line-height: 1.8;
    max-width: 550px;
}

.hero-stamp {
    position: absolute;
    right: 45px;
    bottom: 34px;
    z-index: 1;
    border: 1px solid rgba(221,201,151,.55);
    color: #E6D4A8;
    border-radius: 50%;
    width: 116px;
    height: 116px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 15px;
    line-height: 1.3;
}

/* Section titles */

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    font-weight: 600;
    color: var(--green);
}

.section-subtitle {
    font-size: 11px;
    color: var(--muted);
    margin-top: 5px;
}

/* Metric cards */

.metric {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 19px;
    min-height: 112px;
}

.metric-label {
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 1.2px;
    font-weight: 700;
}

.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    color: var(--green);
    margin-top: 12px;
}

.metric-note {
    font-size: 10px;
    color: var(--muted);
    margin-top: 3px;
}

/* Category cards */

.category {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 19px;
    min-height: 160px;
    transition: all .2s ease;
}

.category:hover {
    border-color: var(--gold);
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(34,55,42,.06);
}

.category-symbol {
    width: 43px;
    height: 43px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: var(--green);
    background: #EAEDE2;
}

.category-name {
    color: var(--green);
    font-size: 14px;
    font-weight: 700;
    margin-top: 15px;
}

.category-caption {
    font-size: 10px;
    color: var(--muted);
    margin-top: 5px;
    line-height: 1.5;
}

/* Feature panels */

.feature {
    background: #FFFDF8;
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 22px;
    min-height: 148px;
}

.feature-mark {
    color: var(--gold);
    font-size: 21px;
}

.feature-title {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    color: var(--green);
    margin-top: 12px;
}

.feature-copy {
    font-size: 11px;
    color: var(--muted);
    line-height: 1.7;
    margin-top: 7px;
}

.small-label {
    color: var(--gold);
    font-size: 9px;
    letter-spacing: 1.7px;
    font-weight: 700;
}

.footer {
    border-top: 1px solid var(--line);
    margin-top: 48px;
    padding-top: 18px;
    color: #929589;
    font-size: 9px;
    letter-spacing: 1.5px;
    text-align: center;
}

@media(max-width: 700px) {
    .hero {
        padding: 28px 23px;
    }
    .hero-stamp {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------------- UI HELPERS ------------------------

def heading(title, subtitle=""):
    st.markdown(f"""
    <div style="margin:12px 0 19px 0;">
      <div class="section-heading">{title}</div>
      <div class="section-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def metric(label, value, note):
    st.markdown(f"""
    <div class="metric">
      <div class="metric-label">{label}</div>
      <div class="metric-value">{value}</div>
      <div class="metric-note">{note}</div>
    </div>
    """, unsafe_allow_html=True)


def category(symbol, title, description):
    st.markdown(f"""
    <div class="category">
      <div class="category-symbol">{symbol}</div>
      <div class="category-name">{title}</div>
      <div class="category-caption">{description}</div>
    </div>
    """, unsafe_allow_html=True)


def feature(symbol, title, description):
    st.markdown(f"""
    <div class="feature">
      <div class="feature-mark">{symbol}</div>
      <div class="feature-title">{title}</div>
      <div class="feature-copy">{description}</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------- SIDEBAR ----------------------------

with st.sidebar:

    st.markdown("""
    <div style="padding:8px 3px 29px 3px;">
      <div style="font-family:'Playfair Display',serif;
                  font-size:27px;color:#F7F4E9;
                  letter-spacing:2px;">
        SAHARA
      </div>
      <div style="font-size:9px;color:#D6C394;
                  letter-spacing:3px;margin-top:2px;">
        UK FOODS LTD
      </div>
      <div style="height:1px;background:rgba(221,208,173,.35);
                  margin-top:21px;"></div>
      <div style="font-size:9px;color:#B7C7B8;
                  letter-spacing:2px;margin-top:19px;">
        TRADE INTELLIGENCE
      </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Product Catalogue",
            "Specifications",
            "Intelligence",
            "Comparisons",
            "Compliance",
            "Documents",
            "About Sahara"
        ],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="margin-top:40px;padding:14px 12px;
        border:1px solid rgba(218,202,157,.25);
        border-radius:7px;background:rgba(255,255,255,.045);">
      <div style="font-family:'Playfair Display',serif;
                  font-size:15px;color:#E5D4AA;">
        Naturally exceptional.
      </div>
      <div style="font-size:10px;color:#C2D0C4;
                  margin-top:7px;line-height:1.7;">
        A refined workspace for product specifications
        and food commodity intelligence.
      </div>
    </div>

    <div style="font-size:9px;color:#A6B8A8;
                text-align:center;margin-top:28px;
                letter-spacing:1.5px;">
        SAHARA UK FOODS LTD
    </div>
    """, unsafe_allow_html=True)


# ---------------------- MAIN HEADER -----------------------

left, right = st.columns([3, 1])

with left:
    st.markdown("""
    <div style="padding:3px 0 10px 0;">
      <div class="small-label">SAHARA UK FOODS &nbsp; / &nbsp; INTELLIGENCE</div>
      <div style="font-family:'Playfair Display',serif;
                  font-size:27px;color:#193D32;
                  margin-top:5px;">
        The Specification Workspace
      </div>
      <div style="font-size:11px;color:#858D81;margin-top:4px;">
        A clearer view of every product, every detail.
      </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div style="text-align:right;padding-top:9px;">
      <div style="font-size:9px;color:#858D81;
                  letter-spacing:1.5px;">WORKSPACE</div>
      <div style="font-family:'Playfair Display',serif;
                  font-size:17px;color:#193D32;">
        Sahara
      </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------- OVERVIEW --------------------------

if page == "Overview":

    st.markdown("""
    <div class="hero">
      <div class="hero-eyebrow">
        PREMIUM FOOD COMMODITIES &nbsp; · &nbsp; PRODUCT INTELLIGENCE
      </div>
      <div class="hero-title">
        Naturally exceptional.<br>
        Precisely specified.
      </div>
      <div class="hero-description">
        One considered workspace for Sahara's world of dates,
        nuts and dried fruits — bringing product information
        and specification intelligence together.
      </div>
      <div class="hero-stamp">
        QUALITY<br>IN EVERY<br>DETAIL
      </div>
    </div>
    """, unsafe_allow_html=True)

    heading(
        "Your portfolio at a glance",
        "A central view of the Sahara product and specification workspace."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric("PRODUCT RECORDS", "—", "Connected database")

    with c2:
        metric("SPECIFICATION FILES", "—", "Original PDF library")

    with c3:
        metric("PRODUCT CATEGORIES", "—", "Portfolio classification")

    with c4:
        metric("INTELLIGENCE", "READY", "Workspace interface")

    heading(
        "Explore our product world",
        "A considered collection of the categories at the heart of our business."
    )

    a, b, c, d = st.columns(4)

    with a:
        category("D", "Dates", "Pitted, chopped and whole dates.")

    with b:
        category("N", "Nuts", "Almonds, pistachios and more.")

    with c:
        category("F", "Dried Fruits", "Apricots, figs and raisins.")

    with d:
        category("I", "Ingredients", "Natural ingredients and food products.")

    heading(
        "Intelligence & operations",
        "Your tools for understanding and managing product information."
    )

    x, y, z = st.columns(3)

    with x:
        feature(
            "01",
            "Product Specifications",
            "Explore product records and access specification information."
        )

    with y:
        feature(
            "02",
            "Specification Intelligence",
            "Find important details and trace them back to their source."
        )

    with z:
        feature(
            "03",
            "Product Comparison",
            "Review product parameters side by side."
        )

    x, y, z = st.columns(3)

    with x:
        feature(
            "04",
            "Compliance Review",
            "Review documented declarations and quality information."
        )

    with y:
        feature(
            "05",
            "Document Library",
            "Keep original product documents accessible."
        )

    with z:
        feature(
            "06",
            "Portfolio Management",
            "A central view of the product information workspace."
        )


# ---------------------- PRODUCT CATALOGUE -----------------

elif page == "Product Catalogue":

    heading(
        "The Product Collection",
        "Explore the categories that define the Sahara portfolio."
    )

    st.text_input(
        "Search the collection",
        placeholder="Search by product name or product code..."
    )

    a, b, c, d = st.columns(4)

    with a:
        category("D", "Dates", "Whole, pitted and chopped.")

    with b:
        category("N", "Nuts", "A selection of natural nuts.")

    with c:
        category("F", "Dried Fruits", "Naturally dried selections.")

    with d:
        category("I", "Ingredients", "Other food ingredients.")

    st.info("Product records will be connected in the data integration phase.")


# ---------------------- SPECIFICATIONS --------------------

elif page == "Specifications":

    heading(
        "Specification Library",
        "A considered view of product documentation and technical details."
    )

    st.text_input(
        "Find a specification",
        placeholder="Enter product code or product name..."
    )

    st.markdown("""
    <div class="feature">
      <div class="feature-title">Original Product Documentation</div>
      <div class="feature-copy">
        Product specifications, technical documents and supporting
        evidence will appear in this workspace.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("PDF library connection will be restored in the integration phase.")


# ---------------------- INTELLIGENCE ----------------------

elif page == "Intelligence":

    heading(
        "Specification Intelligence",
        "A focused workspace for product specification questions."
    )

    st.markdown("""
    <div class="hero" style="min-height:190px;padding:30px;">
      <div class="hero-eyebrow">PRODUCT KNOWLEDGE</div>
      <div class="hero-title" style="font-size:31px;">
        Every detail matters.
      </div>
      <div class="hero-description">
        Search product specifications, quality parameters,
        allergens and nutritional information.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.text_area(
        "Your specification question",
        placeholder="Example: What are the aflatoxin B1 and total aflatoxin values?"
    )

    st.button("Analyse Specification", use_container_width=True)

    st.caption("Design preview only. Answers are not generated in this prototype.")


# ---------------------- COMPARISONS -----------------------

elif page == "Comparisons":

    heading(
        "Product Comparison",
        "A clear side-by-side view of selected product specifications."
    )

    a, b = st.columns(2)

    with a:
        st.selectbox("First product", ["Select product"])

    with b:
        st.selectbox("Second product", ["Select product"])

    st.info("Product comparison will be connected in the integration phase.")


# ---------------------- COMPLIANCE ------------------------

elif page == "Compliance":

    heading(
        "Compliance & Quality",
        "A structured view of documented product information."
    )

    a, b = st.columns(2)

    with a:
        feature(
            "01",
            "Allergen Declarations",
            "Contains, may contain, free-from and not declared."
        )

    with b:
        feature(
            "02",
            "Quality Parameters",
            "Review documented analytical and quality parameters."
        )

    st.info("Compliance records will be connected in the integration phase.")


# ---------------------- DOCUMENTS -------------------------

elif page == "Documents":

    heading(
        "Document Centre",
        "A central home for original product documents."
    )

    st.info("Document library integration will be connected in the next phase.")


# ---------------------- ABOUT -----------------------------

elif page == "About Sahara":

    heading(
        "About Sahara UK Foods",
        "A premium food trading business and its intelligence workspace."
    )

    st.markdown("""
    <div class="hero">
      <div class="hero-eyebrow">SAHARA UK FOODS LTD</div>
      <div class="hero-title">A world of natural ingredients.</div>
      <div class="hero-description">
        Dates, nuts and dried fruits — supported by a dedicated
        product specification and intelligence workspace.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------- FOOTER ----------------------------

st.markdown("""
<div class="footer">
    SAHARA UK FOODS LTD
    &nbsp; · &nbsp;
    PRODUCT SPECIFICATION INTELLIGENCE
    &nbsp; · &nbsp;
    ENGLISH INTERFACE
</div>
""", unsafe_allow_html=True)
