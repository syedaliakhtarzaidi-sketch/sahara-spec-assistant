import os
import streamlit as st
import pandas as pd
from pypdf import PdfReader
import re

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sahara UK Foods - Neural AI Agent Command Center",
    page_icon="⚡",
    layout="wide"
)

# --- 2. CLEAN EXPERT CSS ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #090d16 60%, #030712 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    #MainMenu {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    .stStatusWidget {visibility: hidden !important; display: none !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    #appLoadingSpinner {display: none !important; visibility: hidden !important;}
    div[data-testid="stDecoration"] {visibility: hidden !important; display: none !important;}
    
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    div[data-testid="manage-app-button"] {visibility: hidden !important; display: none !important;}
    
    .vibrant-header {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%);
        padding: 3px;
        border-radius: 22px;
        margin-bottom: 30px;
        box-shadow: 0 20px 50px rgba(139, 92, 246, 0.3);
    }
    .vibrant-header-inner {
        background: #0f172a;
        padding: 30px 35px;
        border-radius: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
    }
    
    .glow-card-green {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(128, 184, 19, 0.4);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(128, 184, 19, 0.15);
        position: relative;
        overflow: hidden;
    }
    .glow-card-green::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 4px; height: 100%;
        background: #80B813;
    }

    .glow-card-blue {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(59, 130, 246, 0.4);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15);
        position: relative;
        overflow: hidden;
    }
    .glow-card-blue::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 4px; height: 100%;
        background: #3b82f6;
    }

    .glow-card-purple {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(168, 85, 247, 0.15);
        position: relative;
        overflow: hidden;
    }
    .glow-card-purple::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 4px; height: 100%;
        background: #a855f7;
    }

    .category-box {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%);
        border: 2px solid #8b5cf6;
        border-radius: 16px;
        padding: 25px 30px;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.25);
        margin-bottom: 25px;
    }

    .stTextInput input {
        background: rgba(15, 23, 42, 0.95) !important;
        color: #ffffff !important;
        border: 2px solid #8b5cf6 !important;
        border-radius: 16px !important;
        padding: 18px 24px !important;
        font-size: 16px !important;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.25) !important;
    }
    .stTextInput input::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }
    .stTextInput input:focus {
        border-color: #80B813 !important;
        box-shadow: 0 0 35px rgba(128, 184, 19, 0.4) !important;
        color: #ffffff !important;
    }

    .stButton button, .stDownloadButton button {
        background: rgba(30, 41, 59, 0.8) !important;
        color: #ffffff !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
        border-radius: 12px !important;
        width: 100% !important;
        text-align: center !important;
        font-weight: 600 !important;
        padding: 10px 15px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton button:hover, .stDownloadButton button:hover {
        background: rgba(139, 92, 246, 0.35) !important;
        border-color: #80B813 !important;
        color: #80B813 !important;
        box-shadow: 0 0 20px rgba(128, 184, 19, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SMART FORMATTED PDF TABLE LAYOUT ---
def format_pdf_to_bullets(raw_text):
    if not raw_text:
        return "<p style='color: #94a3b8;'>No text available.</p>"
    try:
        lines = raw_text.split('\n')
        rows_html = ""
        in_allergen_section = False
        
        exclude_keywords = [
            "Nazia Shamim", "on behalf of SUFL", "on behalf of Customer", 
            "Technical & QAM", "Supplier Name", "Customer Name", 
            "Signature", "Position", "Date"
        ]
        
        for line in lines:
            stripped = line.strip()
            if not stripped or re.match(r'^\d{1,2}$', stripped) or re.match(r'^-\s*\d+\s*-$', stripped):
                continue
            
            if any(exc.lower() in stripped.lower() for exc in exclude_keywords) and len(stripped) < 40:
                continue
                
            if "Allergen Table" in stripped or "2. Allergen" in stripped:
                in_allergen_section = True
                rows_html += "<tr><td colspan='2' style='background: #80B813; color: #000; font-weight: 900; padding: 12px 16px; font-size: 15px;'>2. Allergen Table</td></tr>"
                continue
            
            if "No No No" in line:
                line = line.replace("No No No", " [Contains: No | Processed on Equipment: No | Handled on Site: No]")

            if ":" in stripped:
                parts = stripped.split(":", 1)
                key = parts[0].strip()
                val = parts[1].strip() if len(parts) > 1 else ""
                
                if not in_allergen_section:
                    rows_html += f"""
                    <tr>
                        <td style='padding: 12px 16px; border: 1px solid rgba(128, 184, 19, 0.3); color: #38bdf8; font-weight: 700; width: 35%; background: rgba(15,23,42,0.95); vertical-align: top;'>{key}</td>
                        <td style='padding: 12px 16px; border: 1px solid rgba(128, 184, 19, 0.3); color: #f8fafc; font-weight: 500; width: 65%; background: rgba(15,23,42,0.95); vertical-align: top;'>{val}</td>
                    </tr>
                    """
            else:
                if not in_allergen_section and len(stripped) > 3:
                    rows_html += f"""
                    <tr>
                        <td colspan='2' style='padding: 12px 16px; border: 1px solid rgba(128, 184, 19, 0.3); color: #c084fc; font-weight: 800; background: rgba(128,184,19,0.1);'>{stripped}</td>
                    </tr>
                    """

        pdf_layout = f"""
        <div style='background: #090d16; border: 2px solid #80B813; border-radius: 18px; padding: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.6);'>
            <div style='display: flex; border: 2px solid #80B813; border-radius: 12px; overflow: hidden; margin-bottom: 25px;'>
                <div style='background: #ffffff; padding: 15px; display: flex; align-items: center; justify-content: center; width: 25%;'>
                    <span style='color: #000; font-weight: 900; font-size: 18px;'>Sahara <span style='font-size: 10px;'>UK Foods</span></span>
                </div>
                <div style='background: #dcfce7; color: #166534; padding: 15px 20px; font-weight: 800; font-size: 18px; width: 75%; display: flex; align-items: center;'>
                    Product Specification Document Viewer
                </div>
            </div>
            
            <table style='width: 100%; border-collapse: collapse;'>
                <thead>
                    <tr style='background: #80B813; color: #000;'>
                        <th style='padding: 12px 16px; text-align: left; border: 1px solid #65a30d; width: 35%; font-weight: 900;'>Item</th>
                        <th style='padding: 12px 16px; text-align: left; border: 1px solid #65a30d; width: 65%; font-weight: 900;'>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        """
        return pdf_layout
    except Exception:
        return f"<pre style='color: #f8fafc;'>{raw_text}</pre>"

# --- 3. EXCEL LOADER & EXCLUSION OF SUFL7548 ---
@st.cache_resource
def load_rag_system():
    excel_path = "Product_Specs_Summary.xlsx"
    if os.path.exists(excel_path):
        try:
            df = pd.read_excel(excel_path)
            if 'Product Code' in df.columns and 'Country of Origin' in df.columns:
                df.loc[df['Product Code'] == 'SUFL7390', 'Country of Origin'] = 'Algeria / Tunisia'
            
            if 'Product Code' in df.columns:
                df = df[df['Product Code'] != 'SUFL7548']

            if 'Product Name' in df.columns:
                df = df.sort_values(by='Product Name', ascending=True).reset_index(drop=True)
            return df
        except Exception:
            return None
    return None

df_excel = load_rag_system()

# --- ULTRA FAST CACHED PDF FILE MAPPER ---
@st.cache_resource
def get_pdf_mapping():
    search_dirs = ["pdfs", ".", "PDFs", "pdf"]
    pdf_map = {}
    for directory in search_dirs:
        if os.path.exists(directory):
            try:
                for f in os.listdir(directory):
                    if f.lower().endswith(".pdf") and not f.startswith("~$"):
                        f_lower = f.lower()
                        for idx, row in df_excel.iterrows():
                            p_code = str(row.get('Product Code', '')).strip().lower()
                            if p_code and p_code in f_lower:
                                pdf_map[p_code.upper()] = os.path.join(directory, f)
            except Exception:
                pass
    return pdf_map

pdf_file_map = get_pdf_mapping() if df_excel is not None else {}

def get_pdf_spec_content(p_code):
    clean_p_code = str(p_code).strip().upper()
    pdf_path = pdf_file_map.get(clean_p_code)
    
    if pdf_path and os.path.exists(pdf_path):
        try:
            reader = PdfReader(pdf_path)
            raw_text = "".join([page.extract_text() + "\n" for page in reader.pages if page.extract_text()])
            return pdf_path, format_pdf_to_bullets(raw_text), raw_text
        except Exception:
            pass
    return None, "<p style='color: #f87171;'>No detailed text extracted for this product specification.</p>", ""

# --- 4. HEADER ---
st.markdown("""
    <div class="vibrant-header">
        <div class="vibrant-header-inner">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="background: linear-gradient(135deg, #80B813 0%, #3b82f6 100%); width: 70px; height: 70px; border-radius: 18px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 30px rgba(128,184,19,0.5); flex-shrink: 0;">
                    <span style="font-size: 40px; font-weight: 900; color: #000; font-family: serif;">S</span>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
                        <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 900;">Sahara UK Foods</h1>
                        <span style="background: linear-gradient(90deg, #80B813, #38bdf8); color: #000; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 900;">✨AI Agent v4.0</span>
                    </div>
                    <p style="margin: 0; color: #cbd5e1; font-size: 13px;">Eat Sahara Live Healthy</p>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. METRIC CARDS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="glow-card-green">
            <span style="color: #94a3b8; font-size: 11px; font-weight: 800; text-transform: uppercase;">VERIFIED SPEC INDEX</span>
            <h2 style="color: #ffffff; margin: 8px 0 4px 0; font-size: 2rem; font-weight: 900;">250+ Active PDFs</h2>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="glow-card-blue">
            <span style="color: #94a3b8; font-size: 11px; font-weight: 800; text-transform: uppercase;">QUALITY PARAMETERS</span>
            <h2 style="color: #ffffff; margin: 8px 0 4px 0; font-size: 2rem; font-weight: 900;">Physical & Chemical</h2>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="glow-card-purple">
            <span style="color: #94a3b8; font-size: 11px; font-weight: 800; text-transform: uppercase;">COMPLIANCE & AUDIT</span>
            <h2 style="color: #c084fc; margin: 8px 0 4px 0; font-size: 2rem; font-weight: 900;">BRCGS & HACCP</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 6. SESSION STATE INITIALIZATION ---
if 'selected_product_code' not in st.session_state:
    st.session_state.selected_product_code = None
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "dates"
if 'last_query' not in st.session_state:
    st.session_state.last_query = ""

# --- 7. SEARCH & UNIFIED CATEGORY BOX ---
st.markdown("### 💬 Search your product here")
query = st.text_input("", placeholder="🔍 Search exact product (e.g., Chopped Dates, SUFL7218)...", key="main_search_input")

if query != st.session_state.last_query:
    st.session_state.selected_product_code = None
    st.session_state.last_query = query

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="category-box">', unsafe_allow_html=True)
st.markdown("<h3 style='margin-top: 0; margin-bottom: 20px; color: #ffffff; font-size: 18px; font-weight: 800;'>🗂️ Browse by Major Category</h3>", unsafe_allow_html=True)

cat_r1_c1, cat_r1_c2, cat_r1_c3, cat_r1_c4 = st.columns(4)
with cat_r1_c1:
    if st.button("🌴 Dates", key="cat_dates_btn"):
        st.session_state.selected_category = "dates"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r1_c2:
    if st.button("🍇 Dried Fruits", key="cat_dried_btn"):
        st.session_state.selected_category = "dried fruits"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r1_c3:
    if st.button("🥜 Nuts", key="cat_nuts_btn"):
        st.session_state.selected_category = "nuts"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r1_c4:
    if st.button("🌾 Seeds & Oils", key="cat_seeds_btn"):
        st.session_state.selected_category = "seeds & oils"
        st.session_state.selected_product_code = None
        st.rerun()

st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)

cat_r2_c1, cat_r2_c2, cat_r2_c3, cat_r2_c4 = st.columns(4)
with cat_r2_c1:
    if st.button("🌶️ Spices & Herbs", key="cat_spices_btn"):
        st.session_state.selected_category = "spices"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r2_c2:
    if st.button("🫘 Pulses & Flours", key="cat_pulses_btn"):
        st.session_state.selected_category = "pulses"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r2_c3:
    if st.button("🌟 All Products", key="cat_all_btn"):
        st.session_state.selected_category = "all"
        st.session_state.selected_product_code = None
        st.rerun()
with cat_r2_c4:
    st.markdown("", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

def render_bulletproof_table(df, limit=50, prefix="tbl"):
    if df is None or df.empty:
        st.info("No records to display.")
        return
    
    display_df = df.head(limit) if limit else df
    
    header_cols = st.columns([1.5, 3.5, 2.0, 1.5, 1.5])
    with header_cols[0]:
        st.markdown("<p style='color: #c084fc; font-weight: 800; font-size: 14px;'>Product Code</p>", unsafe_allow_html=True)
    with header_cols[1]:
        st.markdown("<p style='color: #c084fc; font-weight: 800; font-size: 14px;'>Product Name</p>", unsafe_allow_html=True)
    with header_cols[2]:
        st.markdown("<p style='color: #c084fc; font-weight: 800; font-size: 14px;'>Country of Origin</p>", unsafe_allow_html=True)
    with header_cols[3]:
        st.markdown("<p style='color: #c084fc; font-weight: 800; font-size: 14px;'>View Spec</p>", unsafe_allow_html=True)
    with header_cols[4]:
        st.markdown("<p style='color: #c084fc; font-weight: 800; font-size: 14px;'>Download Spec</p>", unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 5px 0 15px 0; border-color: rgba(139, 92, 246, 0.4);'>", unsafe_allow_html=True)
    
    for idx, row in display_df.iterrows():
        p_code = str(row.get('Product Code', '')).strip()
        p_name = str(row.get('Product Name', '')).strip()
        p_origin = str(row.get('Country of Origin', '')).strip()
        
        if not p_code or p_code.lower() == 'nan' or p_code == 'SUFL7548':
            continue
            
        row_cols = st.columns([1.5, 3.5, 2.0, 1.5, 1.5])
        with row_cols[0]:
            st.markdown(f"<p style='color: #38bdf8; font-weight: 600; padding-top: 8px;'>{p_code}</p>", unsafe_allow_html=True)
        with row_cols[1]:
            st.markdown(f"<p style='color: #f8fafc; font-weight: 600; padding-top: 8px;'>{p_name}</p>", unsafe_allow_html=True)
        with row_cols[2]:
            st.markdown(f"<p style='color: #80B813; font-weight: 600; padding-top: 8px;'>{p_origin}</p>", unsafe_allow_html=True)
        with row_cols[3]:
            if st.button("👁️ View", key=f"{prefix}_view_btn_{idx}_{p_code}"):
                st.session_state.selected_product_code = p_code
                st.rerun()
        with row_cols[4]:
            pdf_path = pdf_file_map.get(p_code.upper())
            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button("📥 Download", data=pdf_file.read(), file_name=os.path.basename(pdf_path), mime="application/pdf", key=f"{prefix}_dl_btn_{idx}_{p_code}")
            else:
                st.button("❌ N/A", key=f"{prefix}_no_pdf_{idx}_{p_code}", disabled=True)

# --- ISOLATED & EXACT SINGLE VALUE AI SEARCH AGENT ---
def ask_product_pdf_agent(raw_text, question):
    if not question:
        return "Please enter a valid question."
    
    q_lower = question.lower()
    stop_words = {'does', 'do', 'contain', 'have', 'is', 'in', 'the', 'a', 'an', 'and', 'to', 'our', 'with', 'or', 'its', 'this', 'product', 'what', 'whats', 'quantity', 'value', 'of'}
    keywords = [kw for kw in q_lower.split() if kw not in stop_words and len(kw) > 1]
    
    if not keywords:
        keywords = [q_lower]
        
    segments = []
    for line in raw_text.split('\n'):
        parts = re.split(r'[•|,;]', line)
        for p in parts:
            if p.strip():
                segments.append(p.strip())
                
    exact_matches = []
    for seg in segments:
        seg_lower = seg.lower()
        if any(kw in seg_lower for kw in keywords):
            exact_matches.append(seg.strip())
            
    if exact_matches:
        unique_match = exact_matches[0]
        return f"• {unique_match}"
        
    return f"🤖 No specific information found for '{question}' in this specification document."

def render_product_intelligence_card(p_data):
    st.markdown("<br>", unsafe_allow_html=True)
    p_code = str(p_data.get('Product Code', 'N/A')).strip()
    p_name = str(p_data.get('Product Name', 'N/A')).strip()
    p_origin = str(p_data.get('Country of Origin', 'N/A')).strip()
    
    pdf_path, formatted_text, raw_text = get_pdf_spec_content(p_code)

    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.2) 50%, rgba(236, 72, 153, 0.15) 100%); padding: 3px; border-radius: 20px;">
            <div style="background: linear-gradient(145deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.95) 100%); padding: 30px; border-radius: 18px;">
    """, unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: #c084fc; font-weight: 800; font-size: 15px; margin-bottom: 8px;'>💬 Ask AI Intelligence about {p_code} ({p_name})</p>", unsafe_allow_html=True)
    spec_query = st.text_input("", placeholder="e.g., Fat, Fructose, Lupin, yeast, moisture...", key=f"spec_agent_query_{p_code}")
    
    if spec_query:
        answer = ask_product_pdf_agent(raw_text, spec_query)
        st.markdown(f"""
            <div style="background: rgba(139, 92, 246, 0.15); border: 1px solid rgba(139, 92, 246, 0.4); padding: 18px; border-radius: 14px; margin: 15px 0; color: #f1f5f9;">
                <strong style="color: #38bdf8;">✨ AI Intelligence Answer:</strong><br><br>{answer}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr style='border-color: rgba(255,255,255,0.15); margin: 20px 0;'>", unsafe_allow_html=True)

    top_col1, top_col2 = st.columns([1.5, 1.5])
    with top_col1:
        st.markdown("<h3 style='color: #ffffff; margin: 0;'>🔬 Selected Product Details</h3>", unsafe_allow_html=True)
    with top_col2:
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                st.download_button("📥 Download Official PDF", data=pdf_file.read(), file_name=os.path.basename(pdf_path), mime="application/pdf", key=f"dl_{p_code}")
        else:
            st.error("❌ PDF not found.")
            
    st.markdown(f"""
        <div style="margin-top: 20px;">
            <p style="color: #ffffff;"><strong>Product Code:</strong> <span style="color: #38bdf8;">{p_code}</span></p>
            <p style="color: #ffffff;"><strong>Product Name:</strong> <span style="color: #f1f5f9;">{p_name}</span></p>
            <p style="color: #ffffff;"><strong>Country of Origin:</strong> <span style="color: #80B813;">{p_origin}</span></p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.15); margin: 20px 0;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #c084fc;'>📄 Structured PDF Specification Document Viewer</h4>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="max-height: 600px; overflow-y: auto;">
    """, unsafe_allow_html=True)
    
    # FIXED: Using st.html() to render raw HTML strings cleanly without markdown code-box wrapping
    st.html(formatted_text)
    
    st.markdown("""
        </div>
    </div>
</div>
    """, unsafe_allow_html=True)

# --- MAIN DISPLAY & ROUTING LOGIC ---
if st.session_state.selected_product_code and df_excel is not None:
    sel_row = df_excel[df_excel['Product Code'] == st.session_state.selected_product_code]
    if not sel_row.empty:
        if st.button("🔄 Back to Category / List", key="back_to_list_btn"):
            st.session_state.selected_product_code = None
            st.rerun()
        render_product_intelligence_card(sel_row.iloc[0])
else:
    if query and df_excel is not None:
        q_raw = query.strip().lower()
        q_tokens = [t.rstrip('s') for t in q_raw.split() if len(t) > 1]
        if not q_tokens:
            q_tokens = [q_raw]
            
        def match_row(row: pd.Series) -> bool:
            row_str = " ".join([str(val).lower() for val in row.values])
            return all(token in row_str or token.rstrip('s') in row_str for token in q_tokens)

        res_df = df_excel[df_excel.apply(match_row, axis=1)].reset_index(drop=True)
        
        if not res_df.empty:
            st.markdown(f"### 🔍 Search Results ({len(res_df)} items)")
            render_bulletproof_table(res_df, limit=50, prefix="search")
        else:
            st.info("No records found.")
    elif df_excel is not None:
        cat = st.session_state.selected_category
        if cat == "dates":
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains("date", na=False)).any(axis=1)]
        elif cat == "dried fruits":
            keywords = ["raisin", "apricot", "fig", "mango", "mulberry", "plum", "prune", "cranberry"]
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains('|'.join(keywords), na=False)).any(axis=1)]
        elif cat == "nuts":
            keywords = ["pistachio", "cashew", "almond", "walnut", "peanut", "hazelnut", "pecan"]
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains('|'.join(keywords), na=False)).any(axis=1)]
        elif cat == "seeds & oils":
            keywords = ["seed", "oil", "flaxseed", "pumpkin", "sunflower", "sesame", "chia"]
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains('|'.join(keywords), na=False)).any(axis=1)]
        elif cat == "spices":
            keywords = ["spice", "pepper", "cumin", "turmeric", "cinnamon", "cardamom", "clove", "chilli"]
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains('|'.join(keywords), na=False)).any(axis=1)]
        elif cat == "pulses":
            keywords = ["pulse", "flour", "lentil", "bean", "pea", "chickpea", "gram", "rice"]
            filtered_df = df_excel[df_excel.astype(str).apply(lambda col: col.str.lower().str.contains('|'.join(keywords), na=False)).any(axis=1)]
        else:  # "all"
            filtered_df = df_excel

        if 'Product Name' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='Product Name', ascending=True).reset_index(drop=True)
        else:
            filtered_df = filtered_df.reset_index(drop=True)

        st.markdown(f"### 📋 Category: {cat.title()} ({len(filtered_df)} items - Alphabetical Order)")
        render_bulletproof_table(filtered_df, limit=50, prefix="cat")
