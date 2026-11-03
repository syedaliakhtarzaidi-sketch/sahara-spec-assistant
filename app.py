import os
import re
import base64
import html
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pypdf import PdfReader

# =========================================================
# SAHARA UK FOODS | AI SPECIFICATION AGENT
# Phase 1: Branded interface refresh (English-only)
# =========================================================

st.set_page_config(
    page_title="Sahara UK Foods | Specification Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sahara-inspired palette: navy, gold and green
NAVY = "#07162D"
NAVY_2 = "#0B2142"
GOLD = "#D8AA45"
GREEN = "#168342"
BLUE = "#1677D2"
TEXT = "#F4F7FC"
MUTED = "#A9B8CC"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --sahara-navy: #07162D;
        --sahara-panel: #0B2142;
        --sahara-gold: #D8AA45;
        --sahara-green: #168342;
        --sahara-blue: #1677D2;
        --sahara-text: #F4F7FC;
        --sahara-muted: #A9B8CC;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 8% 0%, rgba(22,119,210,.18), transparent 34%),
            radial-gradient(ellipse at 95% 8%, rgba(216,170,69,.10), transparent 28%),
            linear-gradient(145deg, #061329 0%, #081A34 55%, #061329 100%);
        color: var(--sahara-text);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #06152C 0%, #0A2343 100%);
        border-right: 1px solid rgba(216,170,69,.35);
    }

    [data-testid="stSidebar"] * { color: #F4F7FC; }

    .block-container {
        padding-top: 1.35rem;
        padding-bottom: 2.5rem;
        max-width: 1800px;
    }

    h1, h2, h3, h4 { color: #FFFFFF !important; }
    p, label, span { color: inherit; }

    .brand-wordmark {
        text-align: center;
        padding: 12px 8px 18px;
        border-bottom: 1px solid rgba(216,170,69,.28);
        margin-bottom: 18px;
    }
    .brand-wordmark .leaf {
        color: var(--sahara-green);
        font-size: 27px;
        line-height: 1;
    }
    .brand-wordmark .brand {
        color: var(--sahara-gold);
        font-family: Georgia, serif;
        font-size: 34px;
        font-weight: 700;
        letter-spacing: .4px;
        line-height: 1.05;
    }
    .brand-wordmark .sub {
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: .5px;
    }
    .brand-wordmark .tagline {
        color: var(--sahara-gold);
        font-size: 10px;
        margin-top: 7px;
        letter-spacing: .7px;
    }

    .hero {
        border: 1px solid rgba(216,170,69,.55);
        border-radius: 20px;
        padding: 22px 26px;
        margin-bottom: 18px;
        background:
            linear-gradient(105deg, rgba(5,20,43,.98) 0%, rgba(10,39,73,.95) 62%, rgba(16,65,53,.78) 100%);
        box-shadow: 0 12px 38px rgba(0,0,0,.25);
        position: relative;
        overflow: hidden;
    }
    .hero:after {
        content: "";
        position: absolute;
        width: 340px; height: 340px;
        right: -120px; top: -220px;
        border: 1px solid rgba(216,170,69,.32);
        border-radius: 50%;
        box-shadow: 0 0 0 28px rgba(216,170,69,.035), 0 0 0 58px rgba(216,170,69,.025);
    }
    .hero-kicker {
        color: var(--sahara-gold);
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 10px;
        font-weight: 800;
        margin-bottom: 7px;
    }
    .hero-title {
        color: #FFFFFF;
        font-size: clamp(23px, 3vw, 34px);
        font-weight: 800;
        line-height: 1.15;
        margin: 0;
    }
    .hero-subtitle {
        color: #D5E0EF;
        font-size: 13px;
        margin-top: 8px;
    }
    .hero-tagline {
        color: var(--sahara-gold);
        font-family: Georgia, serif;
        font-style: italic;
        font-size: 16px;
        margin-top: 10px;
    }

    .metric-card {
        background: linear-gradient(145deg, rgba(13,39,72,.96), rgba(7,23,46,.96));
        border: 1px solid rgba(69,126,184,.42);
        border-radius: 16px;
        padding: 17px 18px;
        min-height: 104px;
        box-shadow: 0 8px 24px rgba(0,0,0,.18);
    }
    .metric-label {
        color: #B8C8DA;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 10px;
        font-weight: 700;
    }
    .metric-value {
        color: #FFFFFF;
        font-size: 25px;
        font-weight: 800;
        margin-top: 8px;
        line-height: 1.15;
    }
    .metric-note {
        color: var(--sahara-gold);
        font-size: 11px;
        margin-top: 4px;
    }

    .panel {
        background: linear-gradient(160deg, rgba(12,35,66,.97), rgba(6,22,44,.98));
        border: 1px solid rgba(80,137,190,.42);
        border-radius: 17px;
        padding: 17px;
        box-shadow: 0 9px 26px rgba(0,0,0,.18);
        margin-bottom: 14px;
    }
    .panel-gold { border-color: rgba(216,170,69,.55); }
    .panel-title {
        color: #FFFFFF;
        font-size: 15px;
        font-weight: 800;
        margin-bottom: 4px;
    }
    .panel-caption {
        color: var(--sahara-muted);
        font-size: 11px;
        margin-bottom: 13px;
    }
    .pill {
        display: inline-block;
        background: rgba(22,131,66,.18);
        border: 1px solid rgba(61,190,111,.45);
        color: #8DE0A9;
        border-radius: 30px;
        padding: 5px 10px;
        font-size: 10px;
        font-weight: 700;
    }
    .gold-text { color: var(--sahara-gold); }
    .small-muted { color: var(--sahara-muted); font-size: 11px; }

    .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
        background: #081B35 !important;
        color: #FFFFFF !important;
        border-color: rgba(100,155,205,.55) !important;
        border-radius: 10px !important;
    }
    .stTextInput input::placeholder { color: #91A5BE !important; }
    .stButton button, .stDownloadButton button {
        border-radius: 10px !important;
        border: 1px solid rgba(216,170,69,.55) !important;
        background: linear-gradient(110deg, #123D67, #0D2A4D) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        min-height: 40px;
    }
    .stButton button:hover, .stDownloadButton button:hover {
        border-color: var(--sahara-gold) !important;
        background: linear-gradient(110deg, #1A527F, #14543A) !important;
        color: #FFFFFF !important;
    }
    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(80,137,190,.35);
        border-radius: 12px;
        overflow: hidden;
    }
    hr { border-color: rgba(140,170,205,.2) !important; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------- DATA ----------------------

@st.cache_data(show_spinner=False)
def load_products():
    path = "Product_Specs_Summary.xlsx"
    if not os.path.exists(path):
        return None
    df = pd.read_excel(path)
    if "Product Code" in df.columns:
        df["Product Code"] = df["Product Code"].astype(str).str.strip()
        df = df[df["Product Code"].str.upper() != "SUFL7548"].copy()
    if "Country of Origin" in df.columns and "Product Code" in df.columns:
        df.loc[df["Product Code"].str.upper() == "SUFL7390", "Country of Origin"] = "Algeria / Tunisia"
    if "Product Name" in df.columns:
        df = df.sort_values("Product Name", kind="stable").reset_index(drop=True)
    return df

df_products = load_products()

@st.cache_data(show_spinner=False)
def build_pdf_map(product_codes):
    mapping = {}
    codes = [str(c).strip().upper() for c in product_codes if str(c).strip() and str(c).lower() != "nan"]
    for folder in ("pdfs", ".", "PDFs", "pdf"):
        if not os.path.isdir(folder):
            continue
        try:
            for filename in os.listdir(folder):
                if filename.lower().endswith(".pdf") and not filename.startswith("~$"):
                    lower_name = filename.lower()
                    for code in codes:
                        if code.lower() in lower_name and code not in mapping:
                            mapping[code] = os.path.join(folder, filename)
        except OSError:
            continue
    return mapping

if df_products is not None and "Product Code" in df_products.columns:
    pdf_file_map = build_pdf_map(tuple(df_products["Product Code"].dropna().astype(str)))
else:
    pdf_file_map = {}

@st.cache_data(show_spinner=False)
def read_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    page_texts = []
    for page_no, page in enumerate(reader.pages, start=1):
        try:
            page_texts.append((page_no, page.extract_text() or ""))
        except Exception:
            page_texts.append((page_no, ""))
    raw_text = "\n".join(text for _, text in page_texts)
    return page_texts, raw_text

def clean_text(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "Not listed"
    return str(value).strip()

def get_product_row(code):
    if df_products is None or "Product Code" not in df_products.columns:
        return None
    rows = df_products[df_products["Product Code"].astype(str).str.upper() == str(code).upper()]
    return None if rows.empty else rows.iloc[0]

def format_spec_text(raw_text):
    if not raw_text.strip():
        return "No selectable text was found in this PDF. It may be a scanned document."
    lines = []
    for line in raw_text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    return "\n\n".join(lines)

def render_pdf_viewer(pdf_path, height=690):
    """Embed the original PDF bytes in the page; this is not extracted text."""
    with open(pdf_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    pdf_html = f"""
    <div style="height:{height}px;border:1px solid #31577d;border-radius:12px;overflow:hidden;background:#10233d;">
      <iframe
        src="data:application/pdf;base64,{encoded}"
        width="100%" height="100%"
        style="border:0;background:#fff;"
        type="application/pdf">
      </iframe>
    </div>
    """
    components.html(pdf_html, height=height + 8, scrolling=False)

def basic_spec_lookup(raw_text, question):
    """Current lightweight lookup retained for this visual-only phase.
    It is not represented as full AI reasoning.
    """
    if not question.strip():
        return "Enter a specification question."
    terms = [t.lower() for t in re.findall(r"[A-Za-z0-9µ%./-]+", question) if len(t) > 2]
    stop = {"what", "does", "this", "that", "the", "for", "with", "from", "product", "show", "give", "tell", "about", "value", "level"}
    terms = [t for t in terms if t not in stop]
    if not terms:
        terms = [question.lower().strip()]
    hits = []
    for page_no, line in enumerate(raw_text.splitlines(), start=1):
        low = line.lower()
        score = sum(term in low for term in terms)
        if score:
            hits.append((score, page_no, line.strip()))
    hits.sort(key=lambda item: (-item[0], item[1]))
    if not hits:
        return "No matching information was found in the extracted text. Please check the original PDF."
    return "\n".join(f"• {line}  (text match {i})" for i, (_, _, line) in enumerate(hits[:5], start=1))

# ---------------------- SIDEBAR ----------------------

with st.sidebar:
    logo_path = next((p for p in ("sahara_logo.png", "logo.png", "sahara-logo.png") if os.path.exists(p)), None)
    if logo_path:
        st.image(logo_path, use_container_width=True)
    else:
        st.markdown(
            """
            <div class="brand-wordmark">
              <div class="leaf">✦</div>
              <div class="brand">Sahara</div>
              <div class="sub">UK FOODS LTD</div>
              <div class="tagline">QUALITY YOU CAN TRUST</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("**NAVIGATION**")
    page = st.radio(
        "Navigation",
        ["Dashboard", "Browse Products", "Specification Viewer", "AI Assistant", "About"],
        label_visibility="collapsed",
        key="main_navigation",
    )
    st.markdown("---")
    st.markdown('<span class="pill">● SYSTEM READY</span>', unsafe_allow_html=True)
    st.markdown("<div class='small-muted' style='margin-top:12px'>Sahara UK Foods<br>Specification Intelligence</div>", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------

st.markdown(
    """
    <div class="hero">
      <div class="hero-kicker">SAHARA UK FOODS LTD · QUALITY & PRODUCT INTELLIGENCE</div>
      <div class="hero-title">AI Specification Agent</div>
      <div class="hero-subtitle">Product specifications, document access and evidence-led information in one workspace.</div>
      <div class="hero-tagline">Nature’s Goodness, Our Promise</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if df_products is None:
    st.error("Product_Specs_Summary.xlsx was not found or could not be read. Please check that it is in the repository root.")
    st.stop()

total_products = len(df_products)
available_pdfs = sum(1 for code in df_products["Product Code"].astype(str) if code.upper() in pdf_file_map)
category_count = 0
for col in ("Category", "Product Category", "Product Type"):
    if col in df_products.columns:
        category_count = int(df_products[col].nunique(dropna=True))
        break

m1, m2, m3, m4 = st.columns(4)
for col, label, value, note in [
    (m1, "PRODUCTS IN INDEX", f"{total_products:,}", "From product summary"),
    (m2, "PDF SPECIFICATIONS", f"{available_pdfs:,}", "Matching files found"),
    (m3, "PRODUCT CATEGORIES", str(category_count or "—"), "As listed in workbook"),
    (m4, "DOCUMENT ACCESS", "READY" if available_pdfs else "CHECK", "Original PDF viewer"),
]:
    with col:
        st.markdown(
            f"""<div class="metric-card">
              <div class="metric-label">{label}</div>
              <div class="metric-value">{value}</div>
              <div class="metric-note">{note}</div>
            </div>""",
            unsafe_allow_html=True,
        )

st.write("")

# ---------------------- PRODUCT FILTERS ----------------------

category_col = None
for candidate in ("Category", "Product Category", "Product Type"):
    if candidate in df_products.columns:
        category_col = candidate
        break

left_filter, right_filter = st.columns([2.2, 1])
with left_filter:
    search = st.text_input("Search products", placeholder="Search by product name or product code...")
with right_filter:
    if category_col:
        categories = ["All categories"] + sorted(df_products[category_col].dropna().astype(str).unique().tolist())
        selected_category = st.selectbox("Category", categories)
    else:
        selected_category = "All categories"

filtered = df_products.copy()
if search.strip():
    search_text = search.strip().lower()
    searchable = filtered.astype(str).agg(" ".join, axis=1).str.lower()
    filtered = filtered[searchable.str.contains(re.escape(search_text), na=False)]
if category_col and selected_category != "All categories":
    filtered = filtered[filtered[category_col].astype(str) == selected_category]

# Maintain existing category-style browse where workbook has no category column.
if not category_col and page == "Browse Products":
    browse_category = st.selectbox(
        "Browse by product group",
        ["All products", "Dates", "Dried fruits", "Nuts", "Seeds & oils", "Spices & herbs", "Pulses & flours"],
    )
    category_keywords = {
        "Dates": ["date"],
        "Dried fruits": ["raisin", "apricot", "fig", "mango", "mulberry", "plum", "prune", "cranberry"],
        "Nuts": ["pistachio", "cashew", "almond", "walnut", "peanut", "hazelnut", "pecan"],
        "Seeds & oils": ["seed", "oil", "flaxseed", "pumpkin", "sunflower", "sesame", "chia"],
        "Spices & herbs": ["spice", "pepper", "cumin", "turmeric", "cinnamon", "cardamom", "clove", "chilli"],
        "Pulses & flours": ["pulse", "flour", "lentil", "bean", "pea", "chickpea", "gram", "rice"],
    }
    if browse_category != "All products":
        pattern = "|".join(category_keywords[browse_category])
        mask = filtered.astype(str).apply(lambda c: c.str.lower().str.contains(pattern, na=False)).any(axis=1)
        filtered = filtered[mask]

# Product selection is shared across dashboard pages.
codes = filtered["Product Code"].astype(str).tolist() if "Product Code" in filtered.columns else []
code_to_label = {}
for _, row in filtered.iterrows():
    code = clean_text(row.get("Product Code"))
    name = clean_text(row.get("Product Name"))
    code_to_label[code] = f"{name} · {code}"

if "selected_product_code" not in st.session_state:
    st.session_state.selected_product_code = codes[0] if codes else None
if st.session_state.selected_product_code not in codes and codes:
    st.session_state.selected_product_code = codes[0]

# ---------------------- MAIN WORKSPACE ----------------------

if page == "About":
    st.markdown('<div class="panel panel-gold">', unsafe_allow_html=True)
    st.markdown("### About Sahara Specification Intelligence")
    st.write("A product-document workspace for browsing the Sahara UK Foods product index and viewing original specification PDFs.")
    st.write("This phase refreshes the interface while retaining the existing spreadsheet and PDF sources.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Browse Products":
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### Product Catalogue")
    st.markdown(f"<div class='panel-caption'>{len(filtered):,} matching products</div>", unsafe_allow_html=True)
    display_cols = [c for c in ["Product Code", "Product Name", "Country of Origin"] if c in filtered.columns]
    if display_cols:
        st.dataframe(filtered[display_cols], use_container_width=True, hide_index=True)
    if codes:
        chosen = st.selectbox("Open product specification", codes, format_func=lambda c: code_to_label.get(c, c), key="browse_product_select")
        if st.button("View selected specification", key="browse_open_spec", use_container_width=True):
            st.session_state.selected_product_code = chosen
            st.session_state.main_navigation = "Specification Viewer"
            st.rerun()
    else:
        st.info("No products match the current filters.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Dashboard":
    st.markdown("### Product Intelligence Workspace")
    st.markdown('<div class="panel panel-gold">', unsafe_allow_html=True)
    st.markdown("**Explore your product specifications**")
    st.markdown("<div class='panel-caption'>Select a product to open its original PDF and inspect its available product information.</div>", unsafe_allow_html=True)
    if codes:
        current = st.session_state.selected_product_code or codes[0]
        selected = st.selectbox(
            "Select product",
            codes,
            index=codes.index(current) if current in codes else 0,
            format_func=lambda c: code_to_label.get(c, c),
            key="dashboard_product_select",
        )
        st.session_state.selected_product_code = selected
        if st.button("Open Product Workspace", key="dashboard_open_product", use_container_width=True):
            st.session_state.main_navigation = "Specification Viewer"
            st.rerun()
    else:
        st.info("No products found. Try changing the search or category filter.")
    st.markdown("</div>", unsafe_allow_html=True)

    quick1, quick2, quick3 = st.columns(3)
    with quick1:
        st.markdown('<div class="panel"><div class="panel-title">Original PDF Access</div><div class="panel-caption">Open the source specification document, not extracted text.</div></div>', unsafe_allow_html=True)
    with quick2:
        st.markdown('<div class="panel"><div class="panel-title">Product Information</div><div class="panel-caption">Review product code, name and country of origin.</div></div>', unsafe_allow_html=True)
    with quick3:
        st.markdown('<div class="panel"><div class="panel-title">Specification Lookup</div><div class="panel-caption">Search extracted text while the advanced AI upgrade is planned.</div></div>', unsafe_allow_html=True)

elif page in ("Specification Viewer", "AI Assistant"):
    if not codes:
        st.warning("No products are available under the current filters.")
        st.stop()

    current = st.session_state.selected_product_code or codes[0]
    if current not in codes:
        current = codes[0]
    selected_code = st.selectbox(
        "Select product",
        codes,
        index=codes.index(current),
        format_func=lambda c: code_to_label.get(c, c),
        key="spec_product_select",
    )
    st.session_state.selected_product_code = selected_code
    product = get_product_row(selected_code)
    pdf_path = pdf_file_map.get(str(selected_code).upper())

    if product is not None:
        p_name = clean_text(product.get("Product Name"))
        p_origin = clean_text(product.get("Country of Origin"))
        st.markdown(
            f"""<div class="panel panel-gold">
              <div class="panel-title">{html.escape(p_name)}</div>
              <div class="panel-caption">Product Code: <b>{html.escape(str(selected_code))}</b> &nbsp; · &nbsp; Country of Origin: <b>{html.escape(p_origin)}</b></div>
            </div>""",
            unsafe_allow_html=True,
        )

    pdf_col, info_col = st.columns([1.45, 1], gap="large")
    with pdf_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### Original Product Specification")
        st.markdown('<div class="panel-caption">The original PDF file is embedded below.</div>', unsafe_allow_html=True)
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()
            st.download_button(
                "Download Official PDF",
                data=pdf_bytes,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf",
                key=f"download_{selected_code}",
                use_container_width=True,
            )
            render_pdf_viewer(pdf_path, height=720)
        else:
            st.error("The matching PDF file could not be found for this product.")
        st.markdown("</div>", unsafe_allow_html=True)

    with info_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("### Product Details")
        if product is not None:
            preferred = ["Product Code", "Product Name", "Country of Origin", "Ingredients", "Product Description", "Quality", "Unit Size", "Packing", "Storage"]
            shown = [c for c in preferred if c in product.index]
            for field in shown:
                st.markdown(
                    f"<div style='padding:8px 0;border-bottom:1px solid rgba(140,170,205,.16)'><span style='color:#A9B8CC;font-size:11px'>{html.escape(str(field))}</span><br><b style='color:#FFFFFF'>{html.escape(clean_text(product.get(field)))}</b></div>",
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="panel panel-gold">', unsafe_allow_html=True)
        st.markdown("### Specification Lookup")
        st.markdown('<div class="panel-caption">Current basic text matching. Advanced evidence-based AI is a separate next phase.</div>', unsafe_allow_html=True)
        question = st.text_input(
            "Ask about this product",
            placeholder="e.g. What is the Aflatoxin B1 value?",
            key=f"question_{selected_code}",
        )
        if st.button("Search specification", key=f"ask_{selected_code}", use_container_width=True):
            if not pdf_path or not os.path.exists(pdf_path):
                st.error("The product PDF is unavailable.")
            elif not question.strip():
                st.warning("Please enter a question.")
            else:
                try:
                    _, raw_text = read_pdf(pdf_path)
                    result = basic_spec_lookup(raw_text, question)
                    st.markdown("**Matching text from the specification**")
                    st.info(result)
                    st.caption("This is keyword-based lookup, not a verified AI answer. Check the original PDF before relying on a value.")
                except Exception as exc:
                    st.error(f"Could not read the specification: {exc}")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Choose a section from the navigation sidebar.")

st.markdown(
    """
    <div style="text-align:center;color:#8194AC;font-size:10px;padding:22px 0 4px;border-top:1px solid rgba(216,170,69,.18);margin-top:22px;">
      SAHARA UK FOODS LTD · SPECIFICATION INTELLIGENCE · ENGLISH INTERFACE
    </div>
    """,
    unsafe_allow_html=True,
)
'''

