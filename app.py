
import streamlit as st
import pandas as pd
import base64
import re
from pathlib import Path

# =========================================================
# SAHARA UK FOODS
# FOOD SCIENCE INTELLIGENCE
# PREMIUM DASHBOARD
# =========================================================

st.set_page_config(
    page_title="Sahara | Food Science Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- PATHS --------------------

BASE_DIR = Path(__file__).parent
EXCEL_FILE = BASE_DIR / "Product_Specs_Summary.xlsx"

PDF_DIRS = [
    BASE_DIR / "pdfs",
    BASE_DIR / "PDFs",
    BASE_DIR / "pdf",
    BASE_DIR
]

# -------------------- DESIGN SYSTEM --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg: #101B17;
    --surface: #172720;
    --surface2: #1D3027;
    --border: #30463A;
    --gold: #D4B879;
    --text: #F2F1E9;
    --muted: #A6B7AB;
}

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

[data-testid="stSidebar"] {
    background: #14231C;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--text);
}

h1, h2, h3 {
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

p, label, span {
    font-family: 'DM Sans', sans-serif;
}

.brand {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 8px 0 24px 0;
}

.brand-mark {
    width: 46px;
    height: 46px;
    border-radius: 13px;
    background: linear-gradient(145deg,#E4CD98,#B59454);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #15221B;
    font-family: 'Playfair Display',serif;
    font-size: 29px;
    font-weight: 700;
}

.brand-name {
    color: #F4F0E5;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
}

.brand-sub {
    color: #A6B7AB;
    font-size: 9px;
    letter-spacing: 2px;
    margin-top: 2px;
}

.eyebrow {
    color: var(--gold);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(30px,4vw,43px);
    font-weight: 700;
    color: #F4F1E8;
    letter-spacing: -1.5px;
    margin: 8px 0 5px 0;
}

.hero-subtitle {
    color: #A8B9AE;
    font-size: 14px;
    line-height: 1.7;
}

.panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 14px;
}

.panel-title {
    color: #F2F0E8;
    font-size: 16px;
    font-weight: 700;
}

.panel-sub {
    color: var(--muted);
    font-size: 12px;
    margin-top: 5px;
}

.metric-card {
    background: linear-gradient(145deg,#1C3027,#172720);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 19px;
    min-height: 118px;
}

.metric-label {
    color: #A7B8AC;
    font-size: 10px;
    letter-spacing: 1.5px;
    font-weight: 700;
}

.metric-value {
    color: var(--gold);
    font-size: 30px;
    font-weight: 700;
    margin-top: 8px;
}

.metric-note {
    color: #91A499;
    font-size: 11px;
    margin-top: 3px;
}

.gold-line {
    height: 2px;
    background: linear-gradient(90deg,#D4B879,transparent);
    margin: 14px 0 20px 0;
}

.status-pill {
    display: inline-block;
    color: #B8DCC5;
    background: #203D2D;
    border: 1px solid #365D43;
    padding: 5px 10px;
    border-radius: 30px;
    font-size: 10px;
    letter-spacing: 1px;
    font-weight: 700;
}

div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #1C3027 !important;
    color: #F2F0E8 !important;
    border-color: #405548 !important;
}

.stButton button {
    background: #D4B879;
    color: #17231C;
    border: none;
    border-radius: 9px;
    font-weight: 700;
    min-height: 40px;
}

.stButton button:hover {
    background: #E4CC98;
    color: #17231C;
    border: none;
}

div[data-testid="stDownloadButton"] button {
    background: #263C31;
    color: #E9E9DD;
    border: 1px solid #4A6253;
    border-radius: 9px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--border);
    border-radius: 12px;
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


# -------------------- DATA LOADING --------------------

@st.cache_data
def load_products():
    if not EXCEL_FILE.exists():
        return pd.DataFrame()

    try:
        df = pd.read_excel(EXCEL_FILE)
        df.columns = [str(c).strip() for c in df.columns]

        if "Product Code" in df.columns:
            df = df[df["Product Code"].astype(str) != "SUFL7548"]

        return df.fillna("")
    except Exception:
        return pd.DataFrame()


@st.cache_data
def get_pdf_files():
    files = []

    for folder in PDF_DIRS:
        if folder.exists():
            files.extend(folder.glob("*.pdf"))

    return list(set(files))


def find_pdf(product_code):
    if not product_code:
        return None

    code = str(product_code).strip().lower()

    for pdf in get_pdf_files():
        if code in pdf.stem.lower():
            return pdf

    return None


def identify_column(df, possibilities):
    for col in possibilities:
        for actual in df.columns:
            if actual.lower().strip() == col.lower():
                return actual
    return None


def safe_text(value):
    if value is None:
        return "Not available"

    value = str(value).strip()

    if not value or value.lower() == "nan":
        return "Not available"

    return value


# -------------------- LOAD DATABASE --------------------

df = load_products()

name_col = identify_column(
    df,
    ["Product Name", "Name", "Product"]
)

code_col = identify_column(
    df,
    ["Product Code", "Code", "SKU"]
)

origin_col = identify_column(
    df,
    ["Origin", "Country of Origin", "Country"]
)

if "selected_product" not in st.session_state:
    st.session_state.selected_product = ""


# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-mark">S</div>
        <div>
            <div class="brand-name">SAHARA</div>
            <div class="brand-sub">FOOD SCIENCE INTELLIGENCE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        '<div class="eyebrow">WORKSPACE</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Product Library",
            "Product Intelligence",
            "Quality & Compliance",
            "Document Vault"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        '<div class="eyebrow">PRODUCT CATEGORIES</div>',
        unsafe_allow_html=True
    )

    category = st.radio(
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
    <div style="color:#A6B7AB;font-size:11px;line-height:1.8">
        SAHARA UK FOODS LTD<br>
        Product Specification Platform<br>
        <span style="color:#D4B879">INTERNAL WORKSPACE</span>
    </div>
    """, unsafe_allow_html=True)


# -------------------- HEADER --------------------

st.markdown("""
<div class="eyebrow">SAHARA UK FOODS / QUALITY INTELLIGENCE</div>
<div class="hero-title">Food Science Intelligence</div>
<div class="hero-subtitle">
A unified workspace for product specifications, quality parameters
and technical documentation.
</div>
<div class="gold-line"></div>
""", unsafe_allow_html=True)


# -------------------- PRODUCT FILTERING --------------------

filtered = df.copy()

if not df.empty and name_col:

    search_query = st.text_input(
        "⌕  Search product, product code or origin",
        placeholder="Search your product database...",
        label_visibility="collapsed"
    )

    if search_query:
        mask = pd.Series(False, index=filtered.index)

        for col in filtered.columns:
            mask = mask | filtered[col].astype(str).str.contains(
                search_query,
                case=False,
                na=False
            )

        filtered = filtered[mask]

    if category != "All Products":
        category_words = category.lower().split()

        category_mask = filtered[name_col].astype(str).str.lower().apply(
            lambda x: any(word in x for word in category_words)
        )

        filtered = filtered[category_mask]

else:
    search_query = ""


# -------------------- METRICS --------------------

total_products = len(df) if not df.empty else 0
total_pdfs = len(get_pdf_files())

m1, m2, m3, m4 = st.columns(4)

metrics = [
    (m1, "PRODUCT DATABASE", total_products, "Products in workbook"),
    (m2, "PDF DOCUMENTS", total_pdfs, "Files detected"),
    (m3, "CURRENT RESULTS", len(filtered), "Matching products"),
    (m4, "DATA SOURCE", "EXCEL", "Product specification workbook")
]

for col, label, value, note in metrics:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")


# -------------------- OVERVIEW --------------------

if page == "Overview":

    left, right = st.columns([1.55, 1])

    with left:

        st.markdown("""
        <div class="panel">
            <div class="eyebrow">PRODUCT INTELLIGENCE</div>
            <div class="panel-title" style="font-size:21px;margin-top:8px">
                Your product specification workspace
            </div>
            <div class="panel-sub">
                Explore technical data and access original product documentation.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if not df.empty and name_col:

            st.markdown("### Product Database")

            display_cols = [
                c for c in [
                    code_col,
                    name_col,
                    origin_col
                ] if c and c in filtered.columns
            ]

            if display_cols:
                st.dataframe(
                    filtered[display_cols],
                    use_container_width=True,
                    hide_index=True,
                    height=300
                )

        else:
            st.warning(
                "Product database not found. Check Product_Specs_Summary.xlsx."
            )

    with right:

        st.markdown("""
        <div class="panel">
            <div class="eyebrow">QUALITY MANAGEMENT</div>
            <div class="panel-title" style="font-size:20px;margin-top:8px">
                Technical Intelligence
            </div>
            <div class="panel-sub">
                Explore the core areas of product quality analysis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        modules = [
            ("01", "Chemical Analysis", "Aflatoxin, moisture, acidity"),
            ("02", "Physical Parameters", "Size, colour, defects, impurities"),
            ("03", "Microbiology", "Yeast, mould, bacteria"),
            ("04", "Allergen Intelligence", "Contains and may contain"),
            ("05", "Nutrition", "Energy, protein, fats, carbohydrates"),
            ("06", "Compliance", "Certificates and documented evidence")
        ]

        for number, title, description in modules:
            st.markdown(f"""
            <div style="
                background:#1A2B23;
                border:1px solid #30463A;
                border-radius:10px;
                padding:12px 14px;
                margin-bottom:8px;
                display:flex;
                gap:12px;
            ">
                <div style="color:#D4B879;font-weight:800">{number}</div>
                <div>
                    <div style="color:#F2F0E8;font-size:13px;font-weight:700">
                        {title}
                    </div>
                    <div style="color:#A6B7AB;font-size:11px;margin-top:3px">
                        {description}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# -------------------- PRODUCT LIBRARY --------------------

elif page == "Product Library":

    st.markdown("### Product Library")
    st.caption("Browse the available products in your specification workbook.")

    if not filtered.empty and name_col:

        for _, row in filtered.head(100).iterrows():

            product_name = safe_text(row[name_col])
            product_code = safe_text(row[code_col]) if code_col else ""
            origin = safe_text(row[origin_col]) if origin_col else ""

            with st.container(border=True):

                c1, c2, c3 = st.columns([3, 1.2, 1])

                with c1:
                    st.markdown(f"**{product_name}**")
                    st.caption(
                        f"Product Code: {product_code}  |  Origin: {origin}"
                    )

                with c2:
                    pdf = find_pdf(product_code)
                    st.caption(
                        "PDF AVAILABLE" if pdf else "PDF NOT FOUND"
                    )

                with c3:
                    if st.button(
                        "View Product",
                        key=f"view_{product_code}_{_}"
                    ):
                        st.session_state.selected_product = product_code
                        st.session_state.page_request = "Product Intelligence"
                        st.rerun()

    else:
        st.info("No matching products found.")


# -------------------- PRODUCT INTELLIGENCE --------------------

elif page == "Product Intelligence":

    st.markdown("### Product Intelligence")

    if df.empty or not name_col:
        st.warning("Product workbook or product name column is missing.")

    else:

        product_options = {}

        for _, row in df.iterrows():
            name = safe_text(row[name_col])
            code = safe_text(row[code_col]) if code_col else name
            product_options[f"{name} | {code}"] = row

        option_list = list(product_options.keys())

        default_index = 0

        if st.session_state.selected_product:
            for i, option in enumerate(option_list):
                if st.session_state.selected_product in option:
                    default_index = i
                    break

        selected = st.selectbox(
            "Select Product",
            option_list,
            index=default_index
        )

        row = product_options[selected]

        st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

        p1, p2, p3 = st.columns(3)

        with p1:
            st.markdown("**PRODUCT NAME**")
            st.write(safe_text(row[name_col]))

        with p2:
            st.markdown("**PRODUCT CODE**")
            st.write(safe_text(row[code_col]) if code_col else "Not available")

        with p3:
            st.markdown("**COUNTRY OF ORIGIN**")
            st.write(safe_text(row[origin_col]) if origin_col else "Not available")

        st.markdown("### Product Information")

        product_details = pd.DataFrame({
            "Specification Field": list(row.index),
            "Recorded Value": [safe_text(v) for v in row.values]
        })

        st.dataframe(
            product_details,
            use_container_width=True,
            hide_index=True
        )

        product_code = safe_text(row[code_col]) if code_col else ""
        pdf = find_pdf(product_code)

        st.markdown("### Original Specification Document")

        if pdf and pdf.exists():

            with open(pdf, "rb") as file:
                pdf_bytes = file.read()

            st.download_button(
                "Download Original PDF",
                data=pdf_bytes,
                file_name=pdf.name,
                mime="application/pdf"
            )

            encoded = base64.b64encode(pdf_bytes).decode("utf-8")

            st.markdown(
                f"""
                <iframe
                    src="data:application/pdf;base64,{encoded}"
                    width="100%"
                    height="750"
                    style="border:1px solid #30463A;border-radius:12px">
                </iframe>
                """,
                unsafe_allow_html=True
            )

        else:
            st.warning(
                "No matching PDF found for this product. "
                "Check the PDF filename and product code."
            )


# -------------------- QUALITY & COMPLIANCE --------------------

elif page == "Quality & Compliance":

    st.markdown("### Quality & Compliance")

    st.markdown("""
    <div class="panel">
        <div class="eyebrow">TECHNICAL QUALITY MODULES</div>
        <div class="panel-title" style="font-size:22px;margin-top:8px">
            Product Quality Intelligence
        </div>
        <div class="panel-sub">
            A structured workspace for reviewing documented quality parameters.
        </div>
    </div>
    """, unsafe_allow_html=True)

    quality_modules = [
        ("Aflatoxin Analysis", "B1, B2, G1, G2 and Total"),
        ("Chemical Parameters", "Moisture, acidity and other recorded values"),
        ("Physical Parameters", "Size, colour, foreign matter and defects"),
        ("Microbiological Analysis", "Yeast, mould and microbiological results"),
        ("Allergen Declaration", "Contains, may contain, free from and not declared"),
        ("Nutritional Information", "Energy, protein, fats and carbohydrates"),
        ("Certificates & Compliance", "Documented declarations and certificates")
    ]

    for title, description in quality_modules:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.caption(description)

    st.info(
        "This screen is a design workspace. "
        "Verified results will be connected to the original specification documents."
    )


# -------------------- DOCUMENT VAULT --------------------

elif page == "Document Vault":

    st.markdown("### Document Vault")
    st.caption("Original product specification PDF documents.")

    pdf_files = get_pdf_files()

    if pdf_files:

        for pdf in sorted(pdf_files):

            with st.container(border=True):
                c1, c2 = st.columns([4, 1])

                with c1:
                    st.markdown(f"📄 **{pdf.name}**")
                    st.caption("Original PDF document")

                with c2:
                    with open(pdf, "rb") as file:
                        st.download_button(
                            "Download",
                            data=file.read(),
                            file_name=pdf.name,
                            mime="application/pdf",
                            key=f"download_{pdf.name}"
                        )

    else:
        st.info("No PDF documents were detected in the configured folders.")


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown("""
<div style="
    text-align:center;
    color:#7F9487;
    font-size:10px;
    letter-spacing:1.5px;
    padding:12px">
    SAHARA UK FOODS LTD &nbsp; | &nbsp;
    FOOD SCIENCE INTELLIGENCE
</div>
""", unsafe_allow_html=True)
