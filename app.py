import base64
import re
import html
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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#17271f; --muted:#718078; --forest:#173d2d; --forest2:#214b37; --gold:#b99a60; --lime:#d5e7a3; --paper:#f5f4ee; --white:#fffefa; --line:#e5e7df; }
html, body, [class*="css"] { font-family:'Manrope','DM Sans',sans-serif; }
.stApp { background:var(--paper); color:var(--ink); }
[data-testid="stAppViewContainer"] > .main { background:var(--paper); }
[data-testid="stMainBlockContainer"] { max-width:1500px; padding:2.2rem 3.2rem 3rem; }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#123326 0%,#0d281e 100%); border-right:1px solid #294b3b; }
[data-testid="stSidebar"] * { color:#edf4ec; }
[data-testid="stSidebar"] > div:first-child { padding:1.5rem 1.1rem; }
[data-testid="stSidebar"] [data-testid="stImage"] { display:flex; justify-content:center; margin:8px auto 10px; }
[data-testid="stSidebar"] [data-testid="stImage"] img { width:100%!important; max-width:205px!important; height:auto!important; max-height:none!important; object-fit:contain!important; border-radius:0!important; }
.brand-logo { width:100%; max-width:205px; display:block; margin:4px auto 8px; }
.brand-sub { color:#c8d99e; font-size:9px; font-weight:700; letter-spacing:2.4px; text-align:center; margin:0 0 34px; }
[data-testid="stSidebar"] h3 { color:#d6e6b0; font-size:10px; letter-spacing:2.5px; font-weight:800; margin:22px 0 12px; }
[data-testid="stSidebar"] [data-testid="stRadio"] { margin-top:8px; }
[data-testid="stSidebar"] [data-testid="stRadio"] > label { color:#8fa99a!important; font-size:9px!important; font-weight:800!important; letter-spacing:2px!important; text-transform:uppercase; margin-bottom:12px!important; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] { gap:8px!important; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label { width:100%; min-height:46px; box-sizing:border-box; display:flex; align-items:center; padding:11px 14px!important; margin:0!important; border:1px solid transparent; border-radius:11px; background:rgba(255,255,255,.035); transition:all .18s ease; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:hover { background:rgba(255,255,255,.09); border-color:#486b54; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) { background:#d5e7a3!important; border-color:#d5e7a3!important; box-shadow:0 5px 18px rgba(0,0,0,.12); }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) p { color:#183627!important; font-weight:800!important; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label p { color:#e4eee5!important; font-size:12px!important; font-weight:650!important; }
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label > div:first-child { display:none!important; }
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color:#90a99a!important; }
[data-testid="stSidebar"] hr { border-color:#31513f; }
.hero { position:relative; overflow:hidden; background:linear-gradient(112deg,#173e2e 0%,#1d4935 58%,#294d37 100%); border:1px solid #315a43; border-radius:22px; padding:34px 42px 31px; margin:4px 0 34px; box-shadow:0 18px 45px rgba(21,54,39,.10); }
.hero:after { content:""; position:absolute; width:390px; height:390px; right:-120px; top:-210px; border:1px solid rgba(215,231,171,.18); border-radius:50%; box-shadow:0 0 0 35px rgba(215,231,171,.035),0 0 0 75px rgba(215,231,171,.025); pointer-events:none; }
.hero-brand { display:flex; justify-content:flex-start; align-items:center; width:100%; margin:0 0 22px; position:relative; z-index:1; }
.hero-logo { display:block; width:235px!important; max-width:55%!important; height:auto!important; max-height:none!important; object-fit:contain!important; border-radius:0!important; background:transparent; margin:0; }
.hero-tag { display:inline-block; color:#dcebb9; background:rgba(218,235,180,.09); border:1px solid rgba(218,235,180,.28); padding:7px 12px; border-radius:4px; font-size:9px; font-weight:800; letter-spacing:2.2px; position:relative; z-index:1; }
.hero h1 { color:#fffdf5; font-size:clamp(32px,4vw,48px); line-height:1.08; letter-spacing:-1.8px; font-weight:800; margin:17px 0 12px; position:relative; z-index:1; }
.hero p { color:#d0ddd1; font-size:13px; line-height:1.8; max-width:680px; margin:0; position:relative; z-index:1; }
.hero-divider { height:1px; background:rgba(221,235,197,.22); margin:22px 0 14px; opacity:1; }
.hero-tag + h1 + p + .hero-divider + p { color:#d9e8b7!important; font-size:9px!important; letter-spacing:2.2px; font-weight:800; }
h1,h2,h3 { color:#1b3025; letter-spacing:-.6px; }
h2 { font-weight:800; }
h3 { font-weight:750; }
p, .stMarkdown { color:var(--ink); }
[data-testid="stCaptionContainer"] { color:var(--muted)!important; }
[data-testid="stVerticalBlockBorderWrapper"] { background:var(--white); border:1px solid var(--line); border-radius:15px; box-shadow:0 5px 18px rgba(27,48,37,.035); }
.metric-card { background:var(--white); border:1px solid var(--line); border-radius:15px; padding:21px 22px; box-shadow:0 6px 20px rgba(27,48,37,.035); position:relative; overflow:hidden; }
.metric-card:before { content:""; position:absolute; left:0; top:0; bottom:0; width:3px; background:var(--gold); }
.metric-label { color:#75847a; font-size:9px; font-weight:800; letter-spacing:1.7px; }
.metric-value { color:var(--forest); font-size:29px; line-height:1.2; font-weight:800; margin-top:9px; letter-spacing:-.8px; }
div.stButton > button, div.stDownloadButton > button, [data-testid="stFormSubmitButton"] button { background:var(--forest)!important; color:#fff!important; border:1px solid var(--forest)!important; border-radius:8px!important; font-weight:750!important; padding:10px 18px!important; transition:all .18s ease; }
div.stButton > button:hover, div.stDownloadButton > button:hover, [data-testid="stFormSubmitButton"] button:hover { background:#28563e!important; border-color:#28563e!important; transform:translateY(-1px); box-shadow:0 5px 14px rgba(23,61,45,.16); }
div.stButton > button p, div.stDownloadButton > button p, [data-testid="stFormSubmitButton"] button p { color:#fff!important; font-weight:750!important; }
.stTextInput input, [data-baseweb="select"] { background:#fffefa!important; color:#203329!important; border:1px solid #d8ded4!important; border-radius:8px!important; }
[data-testid="stTextInput"] label, [data-testid="stTextInput"] label p, [data-testid="stSelectbox"] label { color:#344b3d!important; font-weight:700!important; }
[data-testid="stTextInput"] input::placeholder { color:#9aa59d!important; opacity:1!important; }
[data-testid="stSelectbox"] [data-baseweb="select"] * { color:#203329!important; }
[data-testid="stSelectbox"] [role="option"] { color:#203329!important; }
[data-testid="stSelectbox"] [data-baseweb="select"] { background:#fffefa!important; }
[data-testid="stForm"] { background:#fffefa; border:1px solid var(--line); border-radius:14px; padding:18px; }
hr { border-color:#e1e5dc; }
.footer { color:#829087; font-size:9px; font-weight:700; letter-spacing:1.8px; text-align:center; padding:30px 0 12px; }
.muted { color:#718078; font-size:12px; }
div[data-testid="stImage"] img { width:100%; height:215px; object-fit:cover; border-radius:12px; }
/* Our Ingredient World: consistent image frames */
.ingredient-image-frame {
    width: 100%;
    height: 215px;
    overflow: hidden;
    border-radius: 12px;
}
.ingredient-image-frame img {
    display: block;
    width: 100%;
    height: 215px;
    object-fit: cover;
    object-position: center center;
    border-radius: 12px;
}
.answer-heading { padding:4px 0 18px; border-bottom:1px solid #e5e7df; margin-bottom:16px; }
.answer-kicker { color:#a18148; font-size:9px; font-weight:800; letter-spacing:2px; margin-bottom:7px; }
.answer-title { color:#183b2b; font-size:25px; line-height:1.25; font-weight:800; letter-spacing:-.6px; }
.answer-subtitle { color:#718078; font-size:12px; margin-top:5px; }
.answer-table-wrap { width:100%; overflow-x:auto; border:1px solid #e2e6dd; border-radius:12px; background:#fffefa; }
.answer-table { width:100%; border-collapse:collapse; table-layout:fixed; color:#24362b; font-size:13px; }
.answer-table th { background:#183d2c; color:#e2edc9; text-align:left; font-size:9px; font-weight:800; letter-spacing:1.2px; padding:14px 16px; border-bottom:1px solid #315641; }
.answer-table th:nth-child(1) { width:25%; }
.answer-table th:nth-child(2) { width:60%; }
.answer-table th:nth-child(3) { width:15%; text-align:center; }
.answer-table td { padding:15px 16px; border-bottom:1px solid #edf0e9; vertical-align:top; line-height:1.55; overflow-wrap:anywhere; }
.answer-table tbody tr:last-child td { border-bottom:0; }
.answer-table tbody tr:nth-child(even) { background:#f7f8f3; }
.answer-parameter { color:#315b3f; font-weight:800; }
.answer-result { color:#26392e; }
.answer-page { color:#718078; text-align:center; font-variant-numeric:tabular-nums; }
.answer-source { color:#78877d; font-size:9px; font-weight:800; letter-spacing:1.2px; margin-top:12px; }
@media (max-width:900px) { [data-testid="stMainBlockContainer"] { padding:1.5rem 1.5rem 2.5rem; } }
@media (max-width:640px) {
 [data-testid="stMainBlockContainer"] { padding:1rem .8rem 2rem; }
 .hero { padding:25px 22px; border-radius:16px; }
 .hero-logo { width:190px!important; max-width:75%!important; }
 .hero h1 { font-size:32px; letter-spacing:-1px; }
 .answer-table { min-width:560px; }
}
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
        lines = [re.sub(r"\s+", " ", line).strip() for line in page["text"].splitlines()]
        lines = [line for line in lines if line]
        for index, line in enumerate(lines):
            lowered = line.casefold()
            hits = [term for term in expanded_terms if term in lowered]
            if not hits:
                continue
            score = len(hits)
            if "aflatoxin" in query and "aflatoxin" in lowered:
                score += 5
            if any(term in query for term in ["b1", "b2", "g1", "g2"]) and re.search(r"\b(b1|b2|g1|g2)\b", lowered):
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



def classify_spec_question(question):
    q = question.casefold()
    if any(x in q for x in ["insect damage", "insect-damage", "damage by insect", "insect infestation"]):
        return "insect_damage"
    if any(x in q for x in ["peroxide value", "peroxide-value", "peroxide number"]):
        return "peroxide_value"
    if any(x in q for x in ["aflatoxin", "b1", "b2", "g1", "g2"]):
        return "aflatoxin"
    if any(x in q for x in ["ingredient", "composition", "made of", "contains"]):
        return "ingredients"
    if any(x in q for x in ["allergen", "allergy"]):
        return "allergen"
    if any(x in q for x in ["pesticide", "residue"]):
        return "pesticide"
    if any(x in q for x in ["microbiology", "microbiological", "salmonella", "yeast", "mould", "mold", "e. coli", "coliform"]):
        return "microbiology"
    if any(x in q for x in ["nutrition", "nutritional", "energy", "protein", "carbohydrate", "fat"]):
        return "nutrition"
    if any(x in q for x in ["water activity", "water-activity", "aw value", " aw "]):
        return "water_activity"
    if any(x in q for x in ["moisture", "water content"]):
        return "moisture"
    if any(x in q for x in ["sulphur dioxide", "sulfur dioxide", "so2"]):
        return "so2"
    if any(x in q for x in ["shelf life", "best before", "storage", "storing"]):
        return "storage"
    if any(x in q for x in ["origin", "country of origin", "where is it from"]):
        return "origin"
    return "general"


def build_structured_answer(question, pages):
    """Create concise, field-based answers using only text present in the supplier PDF."""
    kind = classify_spec_question(question)
    lines = []
    for page in pages:
        for raw in page["text"].splitlines():
            line = re.sub(r"\s+", " ", raw).strip()
            if line:
                lines.append((page["page"], line))

    def matching(patterns):
        found = []
        for page_no, line in lines:
            if any(re.search(pattern, line, re.I) for pattern in patterns):
                found.append((page_no, line))
        return found

    if kind == "microbiology":
        tests = [
            ("Yeast & Mould", [r"yeasts?\s*(?:&|and)\s*mou?lds?"]),
            ("Total Coliforms", [r"total\s+coliforms?"]),
            ("Salmonella", [r"salmonella"]),
            ("E. coli", [r"e\.?\s*coli"]),
        ]
        results = []
        for label, patterns in tests:
            hits = matching(patterns)
            useful = [(p, t) for p, t in hits if re.search(
                r"(\d+(?:[.,]\d+)?\s*(?:cfu|m|g|kg|ppm|ppb)|absent|not detected|negative|positive|nd\b|<|>|≤|≥)",
                t, re.I
            )]
            if useful:
                results.append((label, useful[0]))
        return {"kind": kind, "rows": results}

    if kind == "insect_damage":
        for index, (page_no, line) in enumerate(lines):
            if re.search(r"insect\s+damage|damage\s+by\s+insects?|insect\s+infestation", line, re.I):
                label_pattern = r"insect\s+damage|damage\s+by\s+insects?|insect\s+infestation"
                result = re.sub(label_pattern, "", line, count=1, flags=re.I)
                result = re.sub(r"^[\s:：=|–-]+", "", result).strip()
                if not re.search(r"(\d+(?:[.,]\d+)?\s*%?|not detected|absent|nil|none|<|>)", result, re.I):
                    for next_page, next_line in lines[index + 1:index + 3]:
                        if next_page == page_no and re.search(r"(\d+(?:[.,]\d+)?\s*%?|not detected|absent|nil|none|<|>)", next_line, re.I):
                            page_no, result = next_page, next_line.strip()
                            break
                result = re.sub(r"^[^:：=|]*[:：=|]\s*", "", result).strip()
                return {"kind": kind, "rows": [("Insect Damage", (page_no, result or line))]}
        return {"kind": kind, "rows": []}

    if kind == "peroxide_value":
        label_pattern = r"\bperoxide\s*value\b|\bperoxide\s*number\b"
        value_pattern = r"(\d+(?:[.,]\d+)?|not detected|nd\b|<|>|≤|≥)"
        for index, (page_no, line) in enumerate(lines):
            if re.search(label_pattern, line, re.I):
                result = re.sub(label_pattern, "", line, count=1, flags=re.I)
                result = re.sub(r"^[\s:：=|–-]+", "", result).strip()
                if not re.search(value_pattern, result, re.I):
                    for next_page, next_line in lines[index + 1:index + 3]:
                        if next_page == page_no and re.search(value_pattern, next_line, re.I):
                            result = next_line.strip()
                            break
                result = re.sub(r"^[\s:：=|()\-–]+", "", result).strip()
                if result:
                    return {"kind": kind, "rows": [("Peroxide Value", (page_no, result))]}
                return {"kind": kind, "rows": []}
        return {"kind": kind, "rows": []}

    if kind == "aflatoxin":
        fields = [
            ("Aflatoxin B1", [r"\baflatoxin\s*[-:]?\s*b1\b", r"\bB1\b"]),
            ("Aflatoxin B2", [r"\baflatoxin\s*[-:]?\s*b2\b", r"\bB2\b"]),
            ("Aflatoxin G1", [r"\baflatoxin\s*[-:]?\s*g1\b", r"\bG1\b"]),
            ("Aflatoxin G2", [r"\baflatoxin\s*[-:]?\s*g2\b", r"\bG2\b"]),
            ("Total Aflatoxin", [r"\btotal\s+aflatoxins?\b", r"\baflatoxins?\s+total\b"]),
        ]
        results = []
        for label, patterns in fields:
            hits = matching(patterns)
            # Avoid treating a bare B1/G1 mention as a result unless a value or unit is present.
            useful = [(p, t) for p, t in hits if re.search(r"(\d+(?:[.,]\d+)?|nd|not detected|<|≤|mg/kg|µg/kg|ug/kg|ppb)", t, re.I)]
            results.append((label, useful[0] if useful else None))
        return {"kind": kind, "rows": results}

    pattern_map = {
        "ingredients": [r"\bingredients?\b", r"\bcomposition\b"],
        "allergen": [r"\ballergen", r"\bcontains?\s:", r"\bmay contain\b"],
        "pesticide": [r"\bpesticide", r"\bresidue"],
        "microbiology": [r"\bmicrobiolog", r"\bsalmonella\b", r"\byeast\b", r"\bmould\b", r"\bmold\b", r"\be\.?\s*coli\b", r"\bcoliform"],
        "nutrition": [r"\bnutrition", r"\benergy\b", r"\bprotein\b", r"\bcarbohydrate\b", r"\bfat\b"],
        "water_activity": [r"water\s*activity", r"\baw\b"],
        "moisture": [r"\bmoisture\b", r"\bwater content\b"],
        "so2": [r"\bso2\b", r"\bsulphur dioxide\b", r"\bsulfur dioxide\b"],
        "storage": [r"\bshelf life\b", r"\bbest before\b", r"\bstorage\b"],
        "origin": [r"\bcountry of origin\b", r"\borigin\b"],
    }
    if kind in pattern_map:
        hits = matching(pattern_map[kind])
        # Prefer the most informative, concise source line rather than returning every keyword hit.
        hits.sort(key=lambda x: (len(x[1]) < 20, len(x[1])))
        return {"kind": kind, "hits": hits[:5]}
    evidence = find_specification_evidence(question, pages)[:5]
    return {"kind": "general", "hits": [(item["page"], item["text"]) for item in evidence]}


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
    st.image("https://i.ibb.co/j9ZyXR3R/1536x768.png", use_container_width=True)
    st.markdown('<div class="brand-sub">EAT SAHARA LIVE HEALTHY</div>', unsafe_allow_html=True)
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
  <div class="hero-brand"><img class="hero-logo" src="https://i.ibb.co/j9ZyXR3R/1536x768.png" alt="Sahara UK Foods — Eat Sahara Live Healthy"></div>
  <span class="hero-tag">SAHARA AI INTELLIGENCE</span>
  <h1>Intelligence behind<br>every ingredient.</h1>
  <p>Your central intelligence workspace for product specifications,
  quality information, ingredient data and compliance documentation.</p>
  <div class="hero-divider"></div>
  <p style="margin:0; color:#d9edaa; font-size:11px; letter-spacing:2px; font-weight:700;">EAT SAHARA LIVE HEALTHY</p>
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
                st.markdown(
                    f'<div class="ingredient-image-frame">'
                    f'<img src="{html.escape(image, quote=True)}" '
                    f'alt="{html.escape(name, quote=True)}">'
                    f'</div>',
                    unsafe_allow_html=True,
                )
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
            chosen_label = st.selectbox(
                "Select product",
                list(product_options.keys()),
                index=None,
                placeholder="Choose a product...",
                key="assistant_product",
            )
            chosen_code = product_options.get(chosen_label) if chosen_label else None
            chosen_pdf = pdf_lookup.get(chosen_code) if chosen_code else None

            st.markdown(
                '<div class="metric-card"><div class="metric-label">SOURCE DOCUMENT</div>'
                f'<div class="metric-value" style="font-size:17px">{chosen_pdf.name if chosen_pdf else "No product selected"}</div></div>',
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
                        answer = build_structured_answer(question, pages)
                        with st.container(border=True):
                            st.markdown(
                                """
                                <div class="answer-heading">
                                    <div class="answer-kicker">SAHARA UK FOODS · PRODUCT INTELLIGENCE</div>
                                    <div class="answer-title">Specification Answer</div>
                                    <div class="answer-subtitle">Extracted directly from the selected supplier specification</div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )
                            result_rows = []
                            source_pages = set()

                            if answer["kind"] == "aflatoxin":
                                for label, hit in answer["rows"]:
                                    if hit:
                                        page_no, source_line = hit
                                        source_pages.add(page_no)
                                        result_rows.append({
                                            "Parameter": label,
                                            "Supplier Result": source_line,
                                            "PDF Page": page_no,
                                        })
                                    else:
                                        result_rows.append({
                                            "Parameter": label,
                                            "Supplier Result": "Not found in specification",
                                            "PDF Page": "—",
                                        })

                            elif answer["kind"] == "insect_damage":
                                for label, hit in answer.get("rows", []):
                                    page_no, source_result = hit
                                    source_pages.add(page_no)
                                    result_rows.append({
                                        "Parameter": label,
                                        "Supplier Result": source_result,
                                        "PDF Page": page_no,
                                    })

                            elif answer["kind"] == "peroxide_value":
                                for label, hit in answer.get("rows", []):
                                    page_no, source_result = hit
                                    source_pages.add(page_no)
                                    result_rows.append({
                                        "Parameter": label,
                                        "Supplier Result": source_result,
                                        "PDF Page": page_no,
                                    })

                            elif answer["kind"] == "microbiology":
                                for label, hit in answer.get("rows", []):
                                    page_no, source_line = hit
                                    source_pages.add(page_no)
                                    label_pattern = {
                                        "Yeast & Mould": r"yeasts?\s*(?:&|and)\s*mou?lds?",
                                        "Total Coliforms": r"(?:total\s+)?coliforms?",
                                        "Salmonella": r"salmonella(?:\s+spp\.?)?",
                                        "E. coli": r"e\.?\s*coli",
                                    }[label]
                                    result = re.sub(label_pattern, "", source_line, count=1, flags=re.I)
                                    result = re.sub(r"^[\s:：(),\-–]+", "", result).strip()
                                    result = re.sub(r"\s*\)", "", result).strip()
                                    result_rows.append({
                                        "Parameter": label,
                                        "Supplier Result": result or "See source PDF",
                                        "PDF Page": page_no,
                                    })

                            else:
                                for page_no, source_line in answer.get("hits", [])[:5]:
                                    source_pages.add(page_no)
                                    result_rows.append({
                                        "Parameter": "Supplier specification",
                                        "Supplier Result": source_line,
                                        "PDF Page": page_no,
                                    })

                            if result_rows:
                                table_rows = []
                                for row in result_rows:
                                    parameter = html.escape(str(row.get("Parameter", "—")))
                                    supplier_result = html.escape(str(row.get("Supplier Result", "—")))
                                    pdf_page = html.escape(str(row.get("PDF Page", "—")))
                                    table_rows.append(
                                        "<tr>"
                                        f"<td class='answer-parameter'>{parameter}</td>"
                                        f"<td class='answer-result'>{supplier_result}</td>"
                                        f"<td class='answer-page'>{pdf_page}</td>"
                                        "</tr>"
                                    )
                                answer_table = (
                                    "<div class='answer-table-wrap'><table class='answer-table'>"
                                    "<thead><tr><th>TEST PARAMETER</th><th>SUPPLIER RESULT</th><th>PDF PAGE</th></tr></thead>"
                                    "<tbody>" + "".join(table_rows) + "</tbody></table></div>"
                                )
                                st.markdown(answer_table, unsafe_allow_html=True)
                                if source_pages:
                                    st.markdown(
                                        "<div class='answer-source'>SOURCE PDF PAGE(S): "
                                        + html.escape(", ".join(map(str, sorted(source_pages))))
                                        + "</div>",
                                        unsafe_allow_html=True,
                                    )
                            else:
                                st.warning("Information not found in this supplier specification.")
            if chosen_pdf:
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
