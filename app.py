
import streamlit as st

# =========================================================
# SAHARA UK FOODS - SIGNATURE INTELLIGENCE
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- VERIFIED PRODUCT IMAGES --------------------

DATES_IMAGE = (
    "https://eat-vegan.b-cdn.net/ingredients/"
    "medjool-datteln-entsteint-1774389719217.png?class=card"
)

NUTS_IMAGE = (
    "https://www.coville.com.tw/upload/4170/"
    "ckeditor_images/c76623f9-3b1a-41cb-a658-5a4f24d27504.webp"
)

DRIED_FRUITS_IMAGE = (
    "https://nutsultan.com/media/hero_slides/"
    "hero_dried_fruits_JzSj4F9_6UXinW1.webp"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #081b15;
    color: #edf5ee;
}

[data-testid="stSidebar"] {
    background: #102b21;
    border-right: 1px solid #244537;
}

[data-testid="stSidebar"] * {
    color: #e8f1e9;
}

.brand {
    font-size: 25px;
    font-weight: 800;
    color: #d5ed9b;
    letter-spacing: 1px;
    padding: 10px 0 2px 0;
}

.brand-sub {
    color: #9bb8a5;
    font-size: 11px;
    letter-spacing: 3px;
    margin-bottom: 35px;
}

.hero {
    background: linear-gradient(115deg, #173c2c, #102a20 70%, #1d422d);
    border: 1px solid #31543d;
    border-radius: 22px;
    padding: 36px;
    margin: 12px 0 28px 0;
}

.hero h1 {
    color: #f2f7ed;
    font-size: 42px;
    line-height: 1.15;
    margin: 12px 0;
}

.hero p {
    color: #b9cbbb;
    font-size: 15px;
    max-width: 700px;
}

.hero-tag {
    display: inline-block;
    color: #d9ef9e;
    background: #294b35;
    border: 1px solid #56744a;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 10px;
    letter-spacing: 2px;
}

div[data-testid="stImage"] img {
    width: 100%;
    height: 215px;
    object-fit: cover;
    border-radius: 12px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #10291f;
    border: 1px solid #294737;
    border-radius: 16px;
}

.metric-card {
    background: #102b21;
    border: 1px solid #294737;
    border-radius: 14px;
    padding: 18px;
}

.metric-label {
    color: #9db5a4;
    font-size: 12px;
}

.metric-value {
    color: #d9edaa;
    font-size: 25px;
    font-weight: 800;
    margin-top: 5px;
}

div.stButton > button {
    background: #c9e58f;
    color: #10291e;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    padding: 10px 18px;
}

div.stButton > button:hover {
    background: #d9efaa;
    color: #10291e;
}

.stTextInput input,
.stTextArea textarea {
    background: #102b21;
    color: #edf5e9;
    border: 1px solid #355442;
    border-radius: 9px;
}

hr {
    border-color: #294737;
}

.footer {
    color: #789282;
    font-size: 11px;
    text-align: center;
    padding: 25px 0;
}
</style>
""", unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown(
        '<div class="brand">SAHARA</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="brand-sub">UK FOODS</div>',
        unsafe_allow_html=True
    )

    st.markdown("### INTELLIGENCE")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Product Intelligence",
            "Specification Library",
            "AI Assistant",
            "Compliance Centre"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption("SAHARA UK FOODS LTD")
    st.caption("Specification Intelligence")
    st.caption("Premium Food Ingredients")


# -------------------- HERO --------------------

st.markdown("""
<div class="hero">
    <span class="hero-tag">SAHARA AI INTELLIGENCE</span>
    <h1>Intelligence behind<br>every ingredient.</h1>
    <p>
        Your central intelligence workspace for product specifications,
        quality information, ingredient data and compliance documentation.
    </p>
</div>
""", unsafe_allow_html=True)


# -------------------- OVERVIEW --------------------

if page == "Overview":

    st.markdown("### Welcome to Sahara Intelligence")
    st.caption("Your ingredient portfolio at a glance.")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">PRODUCT CATEGORIES</div>
            <div class="metric-value">07</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">SPECIFICATION LIBRARY</div>
            <div class="metric-value">250+</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">INTELLIGENCE STATUS</div>
            <div class="metric-value">Ready</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # INGREDIENT WORLD

    st.markdown("### Our Ingredient World")
    st.caption(
        "Explore the premium ingredients supplied by Sahara UK Foods."
    )

    col1, col2, col3 = st.columns(3, gap="large")

    # DATES

    with col1:
        with st.container(border=True):

            st.image(
                DATES_IMAGE,
                use_container_width=True
            )

            st.markdown("**Dates**")
            st.caption(
                "Medjool · Deglet Noor · Pitted Dates"
            )

    # NUTS

    with col2:
        with st.container(border=True):

            st.image(
                NUTS_IMAGE,
                use_container_width=True
            )

            st.markdown("**Nuts**")
            st.caption(
                "Almonds · Cashews · Pistachios · Walnuts"
            )

    # DRIED FRUITS

    with col3:
        with st.container(border=True):

            st.image(
                DRIED_FRUITS_IMAGE,
                use_container_width=True
            )

            st.markdown("**Dried Fruits**")
            st.caption(
                "Dried Apricots · Raisins · Figs · Prunes"
            )


# -------------------- PRODUCT INTELLIGENCE --------------------

elif page == "Product Intelligence":

    st.markdown("### Product Intelligence")
    st.caption("Explore Sahara's product portfolio.")

    category = st.selectbox(
        "Select product category",
        [
            "Dates",
            "Dried Fruits",
            "Nuts",
            "Seeds & Oils",
            "Spices & Herbs",
            "Pulses & Flours",
            "Other"
        ]
    )

    st.info(
        f"Selected category: {category}. "
        "Connect your product database to display live product records here."
    )


# -------------------- SPECIFICATION LIBRARY --------------------

elif page == "Specification Library":

    st.markdown("### Specification Library")
    st.caption("Search and access product specification documents.")

    search = st.text_input(
        "Search product code or product name",
        placeholder="Example: SUFL7334"
    )

    uploaded_files = st.file_uploader(
        "Upload a specification PDF",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for index, pdf in enumerate(uploaded_files):

            st.write(pdf.name)

            st.download_button(
                "Download PDF",
                data=pdf.getvalue(),
                file_name=pdf.name,
                mime="application/pdf",
                key=f"download_{index}"
            )

    st.info(
        "The existing Excel product database and PDF matching engine "
        "still need to be connected to this page."
    )


# -------------------- AI ASSISTANT --------------------

elif page == "AI Assistant":

    st.markdown("### Sahara AI Assistant")
    st.caption(
        "Ask questions about product specifications and quality data."
    )

    question = st.text_area(
        "Your question",
        placeholder=(
            "Example: What is the total aflatoxin value in this product?"
        )
    )

    if st.button("Analyse Specification"):

        if question.strip():

            st.warning(
                "The AI analysis engine has not yet been connected. "
                "No specification values are being generated."
            )

        else:

            st.error("Please enter a question first.")


# -------------------- COMPLIANCE CENTRE --------------------

elif page == "Compliance Centre":

    st.markdown("### Compliance Centre")
    st.caption(
        "A central workspace for quality and compliance information."
    )

    topics = [
        "Aflatoxin",
        "Pesticide Residues",
        "Microbiological Analysis",
        "Allergen Information",
        "Nutrition Information",
        "Country of Origin",
        "Certificates & Documentation"
    ]

    for topic in topics:

        with st.container(border=True):

            st.markdown(f"**{topic}**")
            st.caption("Specification data connection required.")


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'SAHARA UK FOODS LTD · SPECIFICATION INTELLIGENCE'
    '</div>',
    unsafe_allow_html=True
)
