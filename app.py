
import os
import re
import html
import base64
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sahara | Food Science Intelligence",
    page_icon="🌿",
    layout="wide"
)

# ---------------- THEME ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

.stApp {
    background:#17251F;
    color:#F1F0E9;
    font-family:'DM Sans',sans-serif;
}
.block-container {
    max-width:1450px;
    padding-top:2rem;
}
[data-testid="stSidebar"] {
    background:#14221B;
    border-right:1px solid #405247;
}
h1,h2,h3,h4,p,label {
    color:#F1F0E9 !important;
}
.muted {color:#B8C5BB;font-size:13px;}
.eyebrow {
    color:#D4B879;
    font-size:10px;
    font-weight:700;
    letter-spacing:2px;
}
.hero {
    font-size:34px;
    font-weight:700;
    margin-top:8px;
}
.panel {
    background:#22352B;
    border:1px solid #405247;
    border-radius:12px;
    padding:18px;
    margin-bottom:12px;
}
.metric {
    background:#22352B;
    border:1px solid #405247;
    border-radius:10px;
    padding:16px;
}
.metric-number {
    color:#D4B879;
    font-size:26px;
    font-weight:700;
}
.stButton button {
    background:#D4B879;
    color:#17251F;
    border:0;
    border-radius:7px;
    font-weight:700;
}
.stButton button:hover {
    background:#E5CB92;
    color:#17251F;
}
.stTextInput input {
    background:#22352B !important;
    color:#F1F0E9 !important;
    border:1px solid #405247 !important;
}
hr {border-color:#405247;}
</style>
""", unsafe_allow_html=True)


# ---------------- CONSTANTS ----------------

CATEGORIES = [
    "All Products",
    "Dates",
    "Dried Fruits",
    "Nuts",
    "Seeds & Oils",
    "Spices & Herbs",
    "Pulses & Flours",
    "Other"
]


# ---------------- DATA ----------------

@st.cache_data
def load_products():

    path = "Product_Specs_Summary.xlsx"

    if not os.path.exists(path):
        return pd.DataFrame()

    df = pd.read_excel(path)
    df.columns = [str(c).strip() for c in df.columns]

    required = [
        "Product Code",
        "Product Name",
        "Country of Origin"
    ]

    missing = [c for c in required if c not in df.columns]

    if missing:
        return pd.DataFrame()

    df = df.copy()

    df["Product Code"] = df["Product Code"].astype(str).str.strip()
    df["Product Name"] = df["Product Name"].fillna("").astype(str).str.strip()
    df["Country of Origin"] = (
        df["Country of Origin"]
        .fillna("Not specified")
        .astype(str)
        .str.strip()
    )

    df = df[
        (df["Product Code"] != "") &
        (df["Product Code"].str.lower() != "nan") &
        (df["Product Code"] != "SUFL7548")
    ]

    df = df.drop_duplicates(subset=["Product Code"])

    df.loc[
        df["Product Code"] == "SUFL7390",
        "Country of Origin"
    ] = "Algeria / Tunisia"

    df = df.sort_values("Product Name").reset_index(drop=True)

    return df


def identify_category(name):

    n = str(name).lower()

    categories = {
        "Dates": [
            "date", "sayer", "aseel", "deglet", "medjool",
            "ajwa", "khudri", "zahedi"
        ],
        "Dried Fruits": [
            "apricot", "fig", "raisin", "sultana",
            "cranberry", "prune", "plum", "mango",
            "banana", "pineapple", "physalis", "goldenberry"
        ],
        "Nuts": [
            "almond", "pistachio", "cashew", "walnut",
            "hazelnut", "peanut", "pecan", "pinenut"
        ],
        "Seeds & Oils": [
            "sesame", "seed", "oil", "coconut"
        ],
        "Spices & Herbs": [
            "saffron", "garlic", "spice", "herb",
            "pepper", "turmeric", "cinnamon"
        ],
        "Pulses & Flours": [
            "pea", "lentil", "flour", "bean",
            "chickpea", "pulse", "cacao", "cocoa"
        ]
    }

    for category, keywords in categories.items():
        if any(word in n for word in keywords):
            return category

    return "Other"


# ---------------- PDF MAPPING ----------------

@st.cache_data
def get_pdf_mapping(product_codes):

    mapping = {}

    search_dirs = ["pdfs", "PDFs", "pdf", "."]

    for directory in search_dirs:

        if not os.path.isdir(directory):
            continue

        try:
            files = os.listdir(directory)
        except OSError:
            continue

        for filename in files:

            if not filename.lower().endswith(".pdf"):
                continue

            for code in product_codes:

                if code.lower() in filename.lower():

                    full_path = os.path.join(directory, filename)

                    if code not in mapping:
                        mapping[code] = full_path

    return mapping


# ---------------- LOAD DATABASE ----------------

df = load_products()

if not df.empty:

    df["Category"] = df["Product Name"].apply(identify_category)

    pdf_map = get_pdf_mapping(
        tuple(df["Product Code"].tolist())
    )

else:
    pdf_map = {}


# ---------------- SESSION STATE ----------------

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("""
    <div style="margin-bottom:25px">
        <div style="font-size:25px;font-weight:800;letter-spacing:2px">
            SAHARA
        </div>
        <div style="font-size:9px;letter-spacing:2px;color:#D4B879">
            FOOD SCIENCE INTELLIGENCE
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="eyebrow">MAIN MENU</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        ["Dashboard", "Product Database"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption("SAHARA UK FOODS LTD")


# ---------------- HEADER ----------------

st.markdown("""
<div class="eyebrow">SAHARA UK FOODS / WORKSPACE</div>
<div class="hero">Food Science Intelligence</div>
<p class="muted">
Centralised product information and technical documentation.
</p>
<hr>
""", unsafe_allow_html=True)


# ---------------- DASHBOARD ----------------

if page == "Dashboard":

    st.markdown("### Overview")

    if df.empty:

        st.error("Product database could not be loaded.")

    else:

        a, b, c = st.columns(3)

        with a:
            st.markdown(f"""
            <div class="metric">
                <div class="muted">TOTAL PRODUCTS</div>
                <div class="metric-number">{len(df)}</div>
            </div>
            """, unsafe_allow_html=True)

        with b:
            st.markdown(f"""
            <div class="metric">
                <div class="muted">SPECIFICATION PDFs</div>
                <div class="metric-number">{len(pdf_map)}</div>
            </div>
            """, unsafe_allow_html=True)

        with c:
            st.markdown(f"""
            <div class="metric">
                <div class="muted">PRODUCT CATEGORIES</div>
                <div class="metric-number">{df['Category'].nunique()}</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.markdown("### Product Categories")

        counts = df["Category"].value_counts()

        columns = st.columns(4)

        for i, category in enumerate(CATEGORIES[1:]):

            count = int(counts.get(category, 0))

            with columns[i % 4]:

                st.markdown(f"""
                <div class="metric" style="margin-bottom:12px">
                    <div class="muted">{html.escape(category.upper())}</div>
                    <div class="metric-number">{count}</div>
                    <div class="muted">Products</div>
                </div>
                """, unsafe_allow_html=True)


# ---------------- PRODUCT DATABASE ----------------

elif page == "Product Database":

    st.markdown("### Product Database")

    st.markdown(
        '<p class="muted">Select a category to explore its products and technical documentation.</p>',
        unsafe_allow_html=True
    )

    if df.empty:

        st.error("Product database is empty or Excel file is unavailable.")

    else:

        # CATEGORY SELECTION

        st.markdown("#### 01 — Select Category")

        selected_category = st.selectbox(
            "Product Category",
            CATEGORIES,
            key="category_selector"
        )

        filtered = df.copy()

        if selected_category != "All Products":

            filtered = filtered[
                filtered["Category"] == selected_category
            ]

        # SEARCH

        st.markdown("#### 02 — Find a Product")

        search = st.text_input(
            "Search",
            placeholder="Search by product code, name or country of origin...",
            key="product_search"
        )

        if search.strip():

            term = search.strip().lower()

            mask = (
                filtered["Product Code"].str.lower().str.contains(term, na=False) |
                filtered["Product Name"].str.lower().str.contains(term, na=False) |
                filtered["Country of Origin"].str.lower().str.contains(term, na=False)
            )

            filtered = filtered[mask]

        st.markdown(
            f'<div class="muted">{len(filtered)} matching products</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        # PRODUCT SELECTION

        if filtered.empty:

            st.warning("No matching products found.")

        else:

            product_lookup = {
                row["Product Code"]: row["Product Name"]
                for _, row in filtered.iterrows()
            }

            product_options = filtered["Product Code"].tolist()

            selected_code = st.selectbox(
                "Product",
                product_options,
                format_func=lambda code: (
                    f"{code}  —  {product_lookup.get(code, '')}"
                ),
                key="product_selector"
            )

            # SELECTED PRODUCT DETAILS

            selected = df[
                df["Product Code"] == selected_code
            ]

            if not selected.empty:

                row = selected.iloc[0]

                code = row["Product Code"]
                name = row["Product Name"]
                origin = row["Country of Origin"]
                category = row["Category"]

                st.markdown("---")
                st.markdown("#### 03 — Product Information")

                st.markdown(f"""
                <div class="panel">
                    <div class="eyebrow">PRODUCT INFORMATION</div>
                    <h3>{html.escape(name)}</h3>
                    <p class="muted">Product Code: {html.escape(code)}</p>
                    <p class="muted">Country of Origin: {html.escape(origin)}</p>
                    <p class="muted">Category: {html.escape(category)}</p>
                </div>
                """, unsafe_allow_html=True)

                # PDF VIEW AND DOWNLOAD

                pdf_path = pdf_map.get(code)

                st.markdown("#### 04 — Technical Documentation")

                if pdf_path and os.path.exists(pdf_path):

                    with open(pdf_path, "rb") as file:
                        pdf_bytes = file.read()

                    st.success("Original specification PDF found.")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.download_button(
                            "Download Original PDF",
                            data=pdf_bytes,
                            file_name=os.path.basename(pdf_path),
                            mime="application/pdf",
                            use_container_width=True
                        )

                    with col2:

                        if st.button(
                            "View Original PDF",
                            use_container_width=True
                        ):
                            st.session_state.show_pdf = not st.session_state.get(
                                "show_pdf", False
                            )

                    if st.session_state.get("show_pdf", False):

                        encoded_pdf = base64.b64encode(
                            pdf_bytes
                        ).decode("utf-8")

                        pdf_html = f"""
                        <iframe
                            src="data:application/pdf;base64,{encoded_pdf}"
                            width="100%"
                            height="800"
                            style="border:1px solid #405247;border-radius:10px"
                            type="application/pdf">
                        </iframe>
                        """

                        components.html(
                            pdf_html,
                            height=820,
                            scrolling=True
                        )

                else:

                    st.warning(
                        "No matching PDF was found for this product."
                    )
