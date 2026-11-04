import base64
import re
from pathlib import Path
from urllib.parse import quote

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# SAHARA UK FOODS - SIGNATURE INTELLIGENCE
# Product database + original PDF viewer
# ============================================================

st.set_page_config(
    page_title="Sahara UK Foods | Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent
EXCEL_FILE = ROOT / "Product_Specs_Summary.xlsx"
EXCLUDED_CODES = {"SUFL7548"}

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

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #081b15; color: #edf5ee; }
[data-testid="stSidebar"] { background: #102b21; border-right: 1px solid #244537; }
[data-testid="stSidebar"] * { color: #e8f1e9; }
.brand { font-size:25px; font-weight:800; color:#d5ed9b; letter-spacing:1px; padding:10px 0 2px; }
.brand-sub { color:#9bb8a5; font-size:11px; letter-spacing:3px; margin-bottom:35px; }
.hero { background:linear-gradient(115deg,#173c2c,#102a20 70%,#1d422d); border:1px solid #31543d; border-radius:22px; padding:36px; margin:12px 0 28px; }
.hero h1 { color:#f2f7ed; font-size:42px; line-height:1.15; margin:12px 0; }
.hero p { color:#b9cbbb; font-size:15px; max-width:700px; }
.hero-tag { display:inline-block; color:#d9ef9e; background:#294b35; border:1px solid #56744a; padding:7px 13px; border-radius:30px; font-size:10px; letter-spacing:2px; }
div[data-testid="stImage"] img { width:100%; height:215px; object-fit:cover; border-radius:12px; }
div[data-testid="stVerticalBlockBorderWrapper"] { background:#10291f; border:1px solid #294737; border-radius:16px; }
.metric-card { background:#102b21; border:1px solid #294737; border-radius:14px; padding:18px; }
.metric-label { color:#9db5a4; font-size:12px; }
.metric-value { color:#d9edaa; font-size:25px; font-weight:800; margin-top:5px; }
div.stButton > button, div.stDownloadButton > button { background:#c9e58f; color:#10291e; border:none; border-radius:9px; font-weight:700; padding:10px 18px; }
div.stButton > button:hover, div.stDownloadButton > button:hover { background:#d9efaa; color:#10291e; }
.stTextInput input, [data-baseweb="select"] { background:#102b21; color:#edf5e9; border:1px solid #355442; border-radius:9px; }
/* Search field label and placeholder visibility */
[data-testid="stTextInput"] label,
[data-testid="stTextInput"] label p { color:#ffffff !important; }
[data-testid="stTextInput"] input::placeholder { color:#ffffff !important; opacity:1 !important; }
[data-testid="stTextInput"] input { color:#ffffff !important; }

/* Keep category selector text clearly visible on the dark theme */
[data-testid="stSelectbox"] label { color:#ffffff !important; }
[data-testid="stSelectbox"] [data-baseweb="select"] * { color:#ffffff !important; }
[data-testid="stSelectbox"] [role="option"] { color:#ffffff !important; }
[data-testid="stSelectbox"] [data-baseweb="select"] { background:#102b21 !important; }

hr { border-color:#294737; }
.footer { color:#789282; font-size:11px; text-align:center; padding:25px 0; }
.muted { color:#a9c0ae; font-size:12px; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_products():
    if not EXCEL_FILE.exists():
        return pd.DataFrame()
    try:
        frame = pd.read_excel(EXCEL_FILE)
        frame.columns = [str(column).strip() for column in frame.columns]
        required = ["Product Code", "Product Name", "Country of Origin"]
        if not all(column in frame.columns for column in required):
            return pd.DataFrame()
        frame = frame[required].copy()
        frame["Product Code"] = frame["Product Code"].astype(str).str.strip().str.upper()
        frame = frame[~frame["Product Code"].isin(EXCLUDED_CODES)]
        frame = frame[frame["Product Code"].ne("") & frame["Product Code"].ne("NAN")]
        frame.loc[frame["Product Code"].eq("SUFL7390"), "Country of Origin"] = "Algeria / Tunisia"
        return frame.sort_values("Product Name", kind="stable").reset_index(drop=True)
    except Exception as error:
        st.error(f"Product database could not be read: {error}")
        return pd.DataFrame()


@st.cache_data
def discover_pdfs():
    files = []
    ignored = {".git", ".venv", "__pycache__", ".streamlit"}
    for path in ROOT.rglob("*.pdf"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file() and not path.name.startswith("~$"):
            files.append(path)
    return sorted(files, key=lambda item: item.name.casefold())


def find_product_pdf(product_code, pdf_files):
    code = str(product_code).strip().casefold()
    if not code:
        return None
    candidates = [file for file in pdf_files if code in file.stem.casefold()]
    if not candidates:
        return None
    candidates.sort(
        key=lambda file: (
            not file.stem.casefold().startswith(code),
            len(file.name),
            file.name.casefold(),
        )
    )
    return candidates[0]


def render_original_pdf(pdf_path):
    """Display the supplier's original PDF with Streamlit's native PDF viewer."""
    try:
        pdf_bytes = pdf_path.read_bytes()

        # Native Streamlit PDF viewer avoids Chrome blocking a data-URL iframe.
        if not hasattr(st, "pdf"):
            st.error("The PDF viewer requires a newer Streamlit version. Please refresh the app after deployment.")
        else:
            # Use the full available content width and a taller reading area.
            st.markdown(
                """
                <style>
                [data-testid="stPdf"],
                [data-testid="stPdf"] iframe {
                    width: 100% !important;
                    max-width: 100% !important;
                    border: 0 !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    display: block !important;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )
            st.pdf(pdf_bytes, height=1100)

        st.download_button(
            "Download Original PDF",
            data=pdf_bytes,
            file_name=pdf_path.name,
            mime="application/pdf",
            key=f"download_{pdf_path.name}",
        )
        st.caption("Original supplier PDF — source layout, tables, values and signatures are preserved.")
    except Exception as error:
        st.error(f"Unable to display this PDF: {error}")



@st.cache_data(show_spinner=False)
def extract_pdf_pages(pdf_path, modified_time):
    """Extract searchable text page-by-page from the original supplier PDF."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        pages = []
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            pages.append({"page": page_number, "text": text})
        return pages, None
    except Exception as error:
        return [], str(error)


def find_specification_evidence(question, pages):
    """Return verbatim PDF lines ranked by relevance; never generate missing values."""
    query = question.casefold()
    aliases = {
        "aflatoxin": ["aflatoxin", "aflatoxins"],
        "b1": ["b1", "aflatoxin b1"],
        "b2": ["b2", "aflatoxin b2"],
        "g1": ["g1", "aflatoxin g1"],
        "g2": ["g2", "aflatoxin g2"],
        "total": ["total", "sum"],
        "pesticide": ["pesticide", "pesticides", "residue", "residues"],
        "microbiology": ["microbiological", "microbiology", "yeast", "mould", "mold", "salmonella", "e. coli", "coliform"],
        "allergen": ["allergen", "allergens", "allergy"],
        "nutrition": ["nutrition", "nutritional", "energy", "protein", "fat", "carbohydrate"],
        "moisture": ["moisture", "water content"],
        "so2": ["so2", "sulphur dioxide", "sulfur dioxide"],
    }
    search_terms = set(re.findall(r"[a-z0-9.]+", query))
    expanded_terms = set(search_terms)
    for key, values in aliases.items():
        if key in query:
            expanded_terms.update(values)

    stop_words = {"what", "is", "the", "in", "for", "of", "on", "show", "find", "give", "me", "please", "product", "specification", "value", "level", "result"}
    expanded_terms = {term for term in expanded_terms if term not in stop_words and len(term) > 1}
    if not expanded_terms:
        return []

    evidence = []
    for page in pages:
        lines = [re.sub(r"\\s+", " ", line).strip() for line in page["text"].splitlines()]
        lines = [line for line in lines if line]
        for index, line in enumerate(lines):
            lowered = line.casefold()
            hits = [term for term in expanded_terms if term in lowered]
            if not hits:
                continue
            score = len(hits)
            if "aflatoxin" in query and "aflatoxin" in lowered:
                score += 5
            if any(term in query for term in ["b1", "b2", "g1", "g2"]) and re.search(r"\\b(b1|b2|g1|g2)\\b", lowered):
                score += 4
            evidence.append({
                "page": page["page"],
                "text": line,
                "score": score,
                "context": " ".join(lines[max(0, index - 1):min(len(lines), index + 2)]),
            })

    evidence.sort(key=lambda item: (-item["score"], item["page"]))
    # Keep distinct source lines and cap output to a readable evidence set.
    unique = []
    seen = set()
    for item in evidence:
        key = (item["page"], item["text"].casefold())
        if key not in seen:
            unique.append(item)
            seen.add(key)
    return unique[:15]

def category_for_product(product_name):
    name = str(product_name).casefold()
    if any(word in name for word in ["date", "deglet", "medjool", "sayer", "aseel"]):
        return "Dates"
    if any(word in name for word in ["apricot", "raisin", "fig", "prune", "mango", "mulberry", "cranberry"]):
        return "Dried Fruits"
    if any(word in name for word in ["almond", "cashew", "pistachio", "walnut", "hazelnut", "peanut", "nut"]):
        return "Nuts"
    if any(word in name for word in ["seed", "oil"]):
        return "Seeds & Oils"
    if any(word in name for word in ["spice", "saffron", "pepper", "cinnamon"]):
        return "Spices & Herbs"
    if any(word in name for word in ["lentil", "chickpea", "flour", "pulse"]):
        return "Pulses & Flours"
    return "Other"


products = load_products()
pdf_files = discover_pdfs()
pdf_lookup = {
    str(row["Product Code"]): find_product_pdf(row["Product Code"], pdf_files)
    for _, row in products.iterrows()
}

with st.sidebar:
    st.markdown('<div class="brand">SAHARA</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand-sub">UK FOODS</div>', unsafe_allow_html=True)
    st.markdown("### INTELLIGENCE")
    page = st.radio(
        "Navigation",
        ["Overview", "Product Intelligence", "AI Assistant", "Compliance Centre"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("SAHARA UK FOODS LTD")
    st.caption("Specification Intelligence")
    st.caption("Premium Food Ingredients")

st.markdown("""
<div class="hero">
  <span class="hero-tag">SAHARA AI INTELLIGENCE</span>
  <h1>Intelligence behind<br>every ingredient.</h1>
  <p>Your central intelligence workspace for product specifications,
  quality information, ingredient data and compliance documentation.</p>
</div>
""", unsafe_allow_html=True)

matched_pdf_count = sum(path is not None for path in pdf_lookup.values())

if page == "Overview":
    st.markdown("### Welcome to Sahara Intelligence")
    st.caption("Your ingredient portfolio at a glance.")
    col1, col2, col3 = st.columns(3)
    for col, label, value in [
        (col1, "PRODUCT RECORDS", str(len(products))),
        (col2, "PDF SPECIFICATIONS", str(len(pdf_files))),
        (col3, "PRODUCTS WITH MATCHED PDF", str(matched_pdf_count)),
    ]:
        with col:
            st.markdown(
                f'<div class="metric-card"><div class="metric-label">{label}</div>'
                f'<div class="metric-value">{value}</div></div>',
                unsafe_allow_html=True,
            )
    st.markdown("---")
    st.markdown("### Our Ingredient World")
    st.caption("Explore the premium ingredients supplied by Sahara UK Foods.")
    col1, col2, col3 = st.columns(3, gap="large")
    for col, image, name, description in [
        (col1, DATES_IMAGE, "Dates", "Medjool · Deglet Noor · Pitted Dates"),
        (col2, NUTS_IMAGE, "Nuts", "Almonds · Cashews · Pistachios · Walnuts"),
        (col3, DRIED_FRUITS_IMAGE, "Dried Fruits", "Apricots · Raisins · Figs · Prunes"),
    ]:
        with col:
            with st.container(border=True):
                st.image(image, use_container_width=True)
                st.markdown(f"**{name}**")
                st.caption(description)

elif page == "Product Intelligence":
    heading = "Product Intelligence"
    st.markdown(f"### {heading}")
    st.markdown('<p style="color:#ffffff !important; opacity:1; font-weight:500;">Search the live product database and open the matching original supplier PDF.</p>', unsafe_allow_html=True)
    if products.empty:
        st.error("Product database not found or its required columns are missing. Check Product_Specs_Summary.xlsx in the repository root.")
    else:
        search = st.text_input(
            "Search product code, product name or origin",
            placeholder="Example: SUFL7334 or Dried Apricots",
            key=f"search_{page}",
        )
        categories = ["All Products", "Dates", "Dried Fruits", "Nuts", "Seeds & Oils", "Spices & Herbs", "Pulses & Flours", "Other"]
        selected_category = st.selectbox("Category", categories, key=f"category_{page}")
        view = products.copy()
        view["Category"] = view["Product Name"].apply(category_for_product)
        if selected_category != "All Products":
            view = view[view["Category"].eq(selected_category)]
        if search.strip():
            term = search.strip()
            mask = (
                view["Product Code"].str.contains(term, case=False, na=False)
                | view["Product Name"].str.contains(term, case=False, na=False)
                | view["Country of Origin"].astype(str).str.contains(term, case=False, na=False)
            )
            view = view[mask]
        selected_path = st.session_state.get("selected_pdf_path")
        selected_product = st.session_state.get("selected_pdf_product")

        if selected_path:
            selected_pdf = Path(selected_path)
            st.markdown("### Selected Product")
            st.markdown(f"**{selected_product or selected_pdf.name}**")
            if st.button("← Back to Product Search", key="back_to_product_search"):
                st.session_state.pop("selected_pdf_path", None)
                st.session_state.pop("selected_pdf_product", None)
                st.rerun()
            if selected_pdf.exists():
                render_original_pdf(selected_pdf)
            else:
                st.error("The selected PDF is not available in the deployed repository. Please check the file in GitHub.")
        else:
            st.caption(f"{len(view)} matching product(s) · {matched_pdf_count} product records have a matching PDF")
            for index, row in view.head(150).iterrows():
                product_code = str(row["Product Code"])
                pdf_path = pdf_lookup.get(product_code)
                with st.container(border=True):
                    left, middle, right = st.columns([1.15, 3.6, 1.55])
                    left.markdown(f"**{product_code}**")
                    middle.markdown(f"**{row['Product Name']}**")
                    middle.caption(f"Origin: {row['Country of Origin']} · {category_for_product(row['Product Name'])}")
                    if pdf_path:
                        if right.button("View Spec", key=f"view_{page}_{index}", use_container_width=True):
                            st.session_state["selected_pdf_path"] = str(pdf_path)
                            st.session_state["selected_pdf_product"] = f"{product_code} — {row['Product Name']}"
                            st.rerun()
                    else:
                        right.button("PDF Not Found", key=f"missing_{page}_{index}", disabled=True, use_container_width=True)

elif page == "AI Assistant":
    st.markdown("### Sahara AI Assistant")
    st.caption("Ask questions about a product. Answers are extracted from its original supplier PDF, with page references.")
    if products.empty:
        st.error("Product database is unavailable. Check Product_Specs_Summary.xlsx.")
    else:
        available_products = products[
            products["Product Code"].map(lambda code: pdf_lookup.get(str(code)) is not None)
        ].copy()
        if available_products.empty:
            st.error("No product PDFs were found in the repository.")
        else:
            product_options = {
                f"{row['Product Code']} — {row['Product Name']} ({row['Country of Origin']})": str(row["Product Code"])
                for _, row in available_products.iterrows()
            }
            chosen_label = st.selectbox("Select product", list(product_options.keys()), key="assistant_product")
            chosen_code = product_options[chosen_label]
            chosen_pdf = pdf_lookup.get(chosen_code)

            st.markdown(
                '<div class="metric-card"><div class="metric-label">SOURCE DOCUMENT</div>'
                f'<div class="metric-value" style="font-size:17px">{chosen_pdf.name if chosen_pdf else "PDF not found"}</div></div>',
                unsafe_allow_html=True,
            )

            with st.form("specification_question_form"):
                question = st.text_input(
                    "Ask a specification question",
                    placeholder="e.g. What are the Aflatoxin B1, B2, G1, G2 and Total values?",
                )
                submitted = st.form_submit_button("Find Answer", use_container_width=True)

            if submitted:
                if not question.strip():
                    st.warning("Please enter a question.")
                elif not chosen_pdf or not chosen_pdf.exists():
                    st.error("The original supplier PDF could not be found for this product.")
                else:
                    with st.spinner("Searching the original supplier PDF..."):
                        pages, extraction_error = extract_pdf_pages(
                            str(chosen_pdf), chosen_pdf.stat().st_mtime
                        )
                    if extraction_error:
                        st.error(f"Could not read this PDF: {extraction_error}")
                    elif not any(page["text"].strip() for page in pages):
                        st.warning("No searchable text was extracted. This PDF may be scanned or image-only; no values have been assumed.")
                    else:
                        matches = find_specification_evidence(question, pages)
                        if matches:
                            st.markdown("#### Evidence found in supplier specification")
                            st.caption("The following are source excerpts, not generated or calculated values. Check the cited page in the original PDF.")
                            for item in matches:
                                with st.container(border=True):
                                    st.markdown(f"**PDF page {item['page']}**")
                                    st.write(item["context"])
                        else:
                            st.warning("Not found in the searchable text of this supplier PDF. No value has been assumed.")
            with st.expander("Open original supplier PDF"):
                render_original_pdf(chosen_pdf)

elif page == "Compliance Centre":
    st.markdown("### Compliance Centre")
    st.caption("Open the source specification before relying on any quality or compliance value.")
    for topic in [
        "Aflatoxin B1 / B2 / G1 / G2 / Total",
        "Pesticide Residues",
        "Microbiological Analysis",
        "Allergen Information",
        "Nutrition Information",
        "Country of Origin",
        "Certificates & Documentation",
    ]:
        with st.container(border=True):
            st.markdown(f"**{topic}**")
            st.caption("Verify values against the original product specification PDF.")

st.markdown("---")
st.markdown(
    '<div class="footer">SAHARA UK FOODS LTD · SPECIFICATION INTELLIGENCE</div>',
    unsafe_allow_html=True,
)
