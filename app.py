import os
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sahara UK Foods AI Command Center", layout="wide")

st.title("Sahara UK Foods - AI Command Center")

# 1. Load Excel Summary
excel_path = "Product_Specs_Summary.xlsx"
df_excel = pd.read_excel(excel_path) if os.path.exists(excel_path) else None

if df_excel is not None:
    st.success("Excel Database Loaded Successfully!")
    
    # Search bar
    query = st.text_input("Search exact product (e.g., Chopped Dates, SUFL7218):")
    
    if query:
        mask = df_excel.astype(str).apply(lambda x: x.str.contains(query, case=False, na=False)).any(axis=1)
        results = df_excel[mask]
        st.dataframe(results)
    else:
        st.dataframe(df_excel.head(20))
else:
    st.error("Product_Specs_Summary.xlsx not found in root directory!")
