
import streamlit as st

# =========================================================
# SAHARA UK FOODS | SAHARA SIGNATURE
# AI INTELLIGENCE PLATFORM
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | AI Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DESIGN CSS --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0C1711;
    --sidebar: #101F16;
    --panel: #17291E;
    --border: #294332;
    --lime: #A6D936;
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

/* SIDEBAR BRAND */

.brand-logo {
    font-family: 'Manrope', sans-serif;
    font-size: 31px;
    font-weight: 800;
    letter-spacing: 3px;
    color: var(--lime);
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

.sidebar-label {
    color: #809487;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-top: 30px;
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

.hero-section {
    background:
        radial-gradient(circle at 90% 10%, rgba(166,217,54,0.13), transparent 30%),
        linear-gradient(115deg, #183523 0%, #14291D 55%, #1B3422 100%);
    border: 1px solid #36543C;
    border-radius: 20px;
    padding: 42px 38px;
    margin-bottom: 30px;
}

.hero-tag {
    color: var(--lime);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
}

.hero-section h1 {
    color: var(--white);
    font-family: 'Manrope', sans-serif;
    font-size: clamp(32px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.16;
    letter-spacing: -1.8px;
    margin-top: 18px;
    margin-bottom: 15px;
}

.hero-section p {
    color: #B8C9BA;
    font-size: 14px;
    line-height: 1.8;
    max-width: 650px;
}

.hero-company {
    color: var(--lime);
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-top: 22px;
}

/* SECTION HEADINGS */

.section-heading {
    color: var(--white);
    font-family: 'Manrope', sans-serif;
    font-size: 21px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 16px;
}

/* IMAGE GALLERY */

div[data-testid="stImage"] img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 12px;
}

div[data-testid="stImage"] {
    overflow: hidden;
    border-radius: 12px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg, #1B3023, #15271C);
    border: 1px solid var(--border);
    border-radius: 15px;
}

/* WORKSPACE */

.workspace-title {
    color: var(--white);
    font-family: 'Manrope', sans-serif;
    font-size: 19px;
    font-weight: 800;
}

.workspace-description {
    color: var(--muted);
    font-size: 12px;
    line-height: 1.7;
    margin-top: 5px;
}

/* MODULES */

.module-icon {
    color: var(--lime);
    font-size: 26px;
    font-weight: 700;
}

.module-title {
    color: var(--white);
    font-size: 15px;
    font-weight: 700;
}

.module-description {
    color: #A7B7A9;
    font-size: 12px;
    line-height: 1.7;
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
    background: #C1EA65 !important;
}

div[data-testid="stRadio"] label {
    color: #D7E2D7;
    font-size: 13px;
}

/* FOOTER */

.footer {
    border-top: 1px solid var(--border);
    margin-top: 35px;
    padding-top: 20px;
    color: #849688;
    font-size: 9px;
    letter-spacing: 1.5px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("""
    <div style="padding:8px 5px 25px 5px;">
        <div class="brand-logo">SAHARA.</div>
        <div class="brand-subtitle">UK FOODS</div>
        <div class="brand-caption">INTELLIGENCE PLATFORM</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-label">MAIN WORKSPACE</div>',
        unsafe_allow_html=True
    )

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

    st.markdown(
        '<div class="sidebar-label">RESOURCES</div>',
        unsafe_allow_html=True
    )

    resource = st.radio(
        "Resources",
        [
            "Knowledge Library",
            "Document Centre",
            "Settings"
        ],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sidebar-bottom">
        <div style="color:#A6D936;font-weight:700;">
            SAHARA AI SYSTEM
        </div>
        Version 1.0<br>
        Premium Intelligence Workspace
    </div>
    """, unsafe_allow_html=True)


# -------------------- TOP HEADER --------------------

st.markdown("""
<div class="top-header">
    <div class="top-label">
        SAHARA SIGNATURE / INTELLIGENCE
    </div>
    <div class="system-status">
        ● SYSTEM ONLINE
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# AI INTELLIGENCE HOME PAGE
# =========================================================

if page == "AI Intelligence":

    # HERO BANNER - NO HTML CONTENT FRAGMENTS

    st.markdown('<div class="hero-section">', unsafe_allow_html=True)

    st.markdown(
        '<div class="hero-tag">SAHARA AI INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.markdown("# Intelligence behind<br>every ingredient.",
                unsafe_allow_html=True)

    st.markdown("""
    <p>
    Your central workspace for product specifications,
    food quality intelligence, technical documentation
    and compliance analysis.
    </p>
    <div class="hero-company">SAHARA UK FOODS</div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------- INGREDIENT GALLERY --------------------

    st.markdown(
        '<div class="section-heading">Our Ingredient World</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Quality ingredients. Trusted product knowledge.</div>',
        unsafe_allow_html=True
    )

    ingredients = [
        {
            "name": "Dates & Date Products",
            "image": "https://images.unsplash.com/photo-1596591606975-97ee5cef3a1e?w=900&h=600&fit=crop",
            "description": "Premium dates, pitted dates and date ingredients."
        },
        {
            "name": "Nuts & Kernels",
            "image": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=900&h=600&fit=crop",
            "description": "Almonds, pistachios, cashews and walnuts."
        },
        {
            "name": "Dried Fruits",
            "image": "https://images.unsplash.com/photo-1547514701-42782101795e?w=900&h=600&fit=crop",
            "description": "Apricots, figs, raisins and other dried fruits."
        }
    ]

    image_columns = st.columns(3, gap="large")

    for col, item in zip(image_columns, ingredients):

        with col:

            with st.container(border=True):

                try:
                    st.image(
                        item["image"],
                        use_container_width=True
                    )
                except Exception:
                    st.warning("Image could not be loaded.")

                st.markdown(f"**{item['name']}**")
                st.caption(item["description"])

    # -------------------- AI WORKSPACE --------------------

    st.markdown(
        '<div class="section-heading">AI Intelligence Workspace</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.markdown(
            '<div class="workspace-title">What would you like to analyse?</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="workspace-description">'
            'Ask questions about product specifications, quality parameters, '
            'allergens or compliance documents.'
            '</div>',
            unsafe_allow_html=True
        )

        question = st.text_input(
            "Your question",
            placeholder="e.g. What is the aflatoxin level in this product?",
            label_visibility="collapsed",
            key="sahara_question"
        )

        if st.button("Start Analysis", key="start_analysis"):

            if question.strip():
                st.info(
                    "The AI analysis engine has not yet been connected. "
                    "This is currently a design preview."
                )
            else:
                st.warning("Please enter a question first.")

    # -------------------- INTELLIGENCE MODULES --------------------

    st.markdown(
        '<div class="section-heading">Intelligence Modules</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore the specialist intelligence areas of Sahara UK Foods.'
        '</div>',
        unsafe_allow_html=True
    )

    modules = [
        ("◈", "Product Intelligence",
         "Explore product specifications and technical documents."),

        ("⬡", "Compliance Centre",
         "Review food safety documentation and compliance evidence."),

        ("▤", "Nutrition Analysis",
         "Review nutritional values and product comparisons."),

        ("◇", "Allergen Intelligence",
         "Review allergen declarations and product risks."),

        ("✧", "Quality Analysis",
         "Analyse aflatoxin, moisture and microbiological parameters."),

        ("⌘", "Knowledge Library",
         "Access the central product and document knowledge base.")
    ]

    module_columns = st.columns(3, gap="large")

    for index, (icon, title, description) in enumerate(modules):

        with module_columns[index % 3]:

            with st.container(border=True):

                st.markdown(
                    f'<div class="module-icon">{icon}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="module-title">{title}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="module-description">{description}</div>',
                    unsafe_allow_html=True
                )


# =========================================================
# OTHER NAVIGATION PAGES
# =========================================================

elif page == "Product Intelligence":

    st.title("Product Intelligence")
    st.write("Explore product specifications, origins and technical documents.")
    st.info("Product database integration is planned for the next phase.")

elif page == "Quality Analysis":

    st.title("Quality Analysis")
    st.write("Review aflatoxin, moisture and microbiological parameters.")
    st.info("Quality document analysis is planned for the next phase.")

elif page == "Allergen Intelligence":

    st.title("Allergen Intelligence")
    st.write("Review allergen declarations and product risk information.")
    st.info("Allergen analysis is planned for the next phase.")

elif page == "Nutrition Analysis":

    st.title("Nutrition Analysis")
    st.write("Review nutritional values and compare product information.")
    st.info("Nutrition analysis is planned for the next phase.")

elif page == "Compliance Centre":

    st.title("Compliance Centre")
    st.write("Review food safety documentation and compliance evidence.")
    st.info("Compliance analysis is planned for the next phase.")


# -------------------- RESOURCE PAGES --------------------

if resource == "Knowledge Library":
    if page != "AI Intelligence":
        st.info("Knowledge Library integration is planned for the next phase.")

elif resource == "Document Centre":
    st.info("Document Centre integration is planned for the next phase.")

elif resource == "Settings":
    st.info("Platform settings are planned for a future update.")


# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
    SAHARA UK FOODS
    &nbsp;&nbsp;&nbsp;&nbsp;
    INTELLIGENCE PLATFORM
    &nbsp;&nbsp;&nbsp;&nbsp;
    VERSION 1.0
</div>
""", unsafe_allow_html=True)
import streamlit as st

# =========================================================
# SAHARA UK FOODS
# PREMIUM AI INTELLIGENCE PLATFORM
# SAHARA SIGNATURE EDITION
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | AI Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CSS DESIGN --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #0C1711;
    --sidebar: #101F16;
    --panel: #17291E;
    --border: #294332;
    --lime: #A6D936;
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
    min-height: 300px;
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
    margin-bottom: 8px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 18px;
}

/* INGREDIENT CARDS */

.ingredient-card {
    background: #17291E;
    border: 1px solid #294332;
    border-radius: 15px;
    overflow: hidden;
    margin-bottom: 15px;
}

.ingredient-name {
    color: #F4F5EF;
    font-size: 15px;
    font-weight: 700;
    padding: 15px 16px 5px 16px;
}

.ingredient-description {
    color: #A1B1A3;
    font-size: 12px;
    line-height: 1.6;
    padding: 0 16px 18px 16px;
}

/* WORKSPACE */

.workspace {
    background: #14251B;
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 25px;
    margin-top: 18px;
    margin-bottom: 15px;
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
    line-height: 1.7;
}

/* MODULES */

.panel {
    background: linear-gradient(145deg, #1B3023, #15271C);
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 22px;
    min-height: 165px;
    margin-bottom: 14px;
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

/* INPUT */

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
    background: #C1EA65 !important;
}

div[data-testid="stRadio"] label {
    color: #D7E2D7;
    font-size: 13px;
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

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("""
    <div style="padding:8px 5px 25px 5px;">
        <div class="brand-logo">SAHARA.</div>
        <div class="brand-subtitle">UK FOODS</div>
        <div class="brand-caption">INTELLIGENCE PLATFORM</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-label">MAIN WORKSPACE</div>',
        unsafe_allow_html=True
    )

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

    st.markdown(
        '<div class="sidebar-label">RESOURCES</div>',
        unsafe_allow_html=True
    )

    resource = st.radio(
        "Resources",
        [
            "Knowledge Library",
            "Document Centre",
            "Settings"
        ],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sidebar-bottom">
        <div style="color:#A6D936;font-weight:700;">
            SAHARA AI SYSTEM
        </div>
        Version 1.0<br>
        Premium Intelligence Workspace
    </div>
    """, unsafe_allow_html=True)


# -------------------- TOP HEADER --------------------

st.markdown("""
<div class="top-header">
    <div class="top-label">
        SAHARA SIGNATURE / INTELLIGENCE
    </div>
    <div class="system-status">
        ● SYSTEM ONLINE
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------- AI INTELLIGENCE PAGE --------------------

if page == "AI Intelligence":

    # HERO

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

        <div class="hero-company">
            SAHARA UK FOODS
        </div>
    </div>
    """, unsafe_allow_html=True)

    # INGREDIENT GALLERY

    st.markdown("""
    <div class="section-heading">Our Ingredient World</div>
    <div class="section-subtitle">
        Quality ingredients. Trusted product knowledge.
    </div>
    """, unsafe_allow_html=True)

    ingredients = [
        {
            "name": "Dates & Date Products",
            "image": "https://images.unsplash.com/photo-1596591606975-97ee5cef3a1e?w=900",
            "description": "Premium dates, pitted dates and date ingredients."
        },
        {
            "name": "Nuts & Kernels",
            "image": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=900",
            "description": "Almonds, pistachios, cashews and walnuts."
        },
        {
            "name": "Dried Fruits",
            "image": "https://images.unsplash.com/photo-1596591606975-97ee5cef3a1e?w=900",
            "description": "Apricots, figs, raisins and other dried fruits."
        }
    ]

    image_cols = st.columns(3)

    for col, item in zip(image_cols, ingredients):
        with col:
            st.markdown('<div class="ingredient-card">', unsafe_allow_html=True)

            try:
                st.image(
                    item["image"],
                    use_container_width=True
                )
            except Exception:
                st.markdown(
                    '<div style="padding:35px;text-align:center;color:#A6D936;">'
                    'Image unavailable</div>',
                    unsafe_allow_html=True
                )

            st.markdown(
                f'<div class="ingredient-name">{item["name"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="ingredient-description">{item["description"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

    # AI WORKSPACE

    st.markdown(
        '<div class="section-heading">AI Intelligence Workspace</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="workspace">
        <div class="workspace-title">
            What would you like to analyse?
        </div>
        <div class="workspace-description">
            Ask questions about product specifications,
            quality parameters, allergens or compliance documents.
        </div>
    </div>
    """, unsafe_allow_html=True)

    question = st.text_input(
        "Your question",
        placeholder="e.g. What is the aflatoxin level in this product?",
        label_visibility="collapsed",
        key="sahara_question"
    )

    if st.button("Start Analysis", key="start_analysis"):
        if question.strip():
            st.info(
                "AI analysis engine integration is planned for the next phase."
            )
        else:
            st.warning("Please enter a question first.")

    # INTELLIGENCE MODULES

    st.markdown(
        '<div class="section-heading">Intelligence Modules</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore the specialist intelligence areas of Sahara UK Foods.'
        '</div>',
        unsafe_allow_html=True
    )

    modules = [
        ("◈", "Product Intelligence",
         "Explore product specifications and technical documents."),

        ("▤", "Nutrition Analysis",
         "Review nutritional values and product comparisons."),

        ("✧", "Quality Analysis",
         "Analyse aflatoxin, moisture and microbiological parameters."),

        ("⬡", "Compliance Centre",
         "Review food safety documentation and compliance evidence."),

        ("◇", "Allergen Intelligence",
         "Review allergen declarations and product risks."),

        ("⌘", "Knowledge Library",
         "Access the central product and document knowledge base.")
    ]

    columns = st.columns(3)

    for index, (icon, title, description) in enumerate(modules):
        with columns[index % 3]:
            st.markdown(f"""
            <div class="panel">
                <div class="panel-icon">{icon}</div>
                <div class="panel-title">{title}</div>
                <div class="panel-description">{description}</div>
            </div>
            """, unsafe_allow_html=True)


# -------------------- OTHER PAGES --------------------

elif page == "Product Intelligence":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">PRODUCT INTELLIGENCE</div>
        <div class="hero-title">Product knowledge.<br>One workspace.</div>
        <p class="hero-text">
            Explore product specifications, origins and technical documents.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Product database integration is planned for the next phase.")

elif page == "Quality Analysis":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">QUALITY INTELLIGENCE</div>
        <div class="hero-title">Quality you can<br>verify.</div>
        <p class="hero-text">
            Review aflatoxin, moisture and microbiological parameters.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Quality document analysis is planned for the next phase.")

elif page == "Allergen Intelligence":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">ALLERGEN INTELLIGENCE</div>
        <div class="hero-title">Understand every<br>ingredient.</div>
        <p class="hero-text">
            Review allergen declarations and product risk information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Allergen analysis is planned for the next phase.")

elif page == "Nutrition Analysis":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">NUTRITION INTELLIGENCE</div>
        <div class="hero-title">Nutrition data.<br>Clear insights.</div>
        <p class="hero-text">
            Review nutritional values and compare product information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Nutrition analysis is planned for the next phase.")

elif page == "Compliance Centre":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">COMPLIANCE CENTRE</div>
        <div class="hero-title">Documentation<br>with confidence.</div>
        <p class="hero-text">
            Review food safety documents and compliance evidence.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Compliance document analysis is planned for the next phase.")


# -------------------- RESOURCE PAGES --------------------

if resource == "Knowledge Library":
    if page != "AI Intelligence":
        st.info("Knowledge Library integration is planned for the next phase.")

elif resource == "Document Centre":
    st.info("Document Centre integration is planned for the next phase.")

elif resource == "Settings":
    st.info("Platform settings are planned for a future update.")


# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
    <span>SAHARA UK FOODS</span>
    <span>INTELLIGENCE PLATFORM</span>
    <span>VERSION 1.0</span>
</div>
""", unsafe_allow_html=True)
