import os
import pandas as pd

print("Loading Updated Sahara UK Foods Excel Database...")

excel_path = "Product_Specs_Summary.xlsx"
df_excel = pd.read_excel(excel_path) if os.path.exists(excel_path) else None

print("System Ready! Enter product code or query to search.\n")

if df_excel is not None:
    while True:
        query = input("Enter Product Code / Query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        
        mask = df_excel.astype(str).apply(lambda x: x.str.contains(query, case=False, na=False)).any(axis=1)
        results = df_excel[mask]
        
        if not results.empty:
            for idx, row in results.head(5).iterrows():
                row_vals = list(row.values)
                code = str(row_vals[0])
                prod_name = str(row_vals[1])
                origin = str(row_vals[2]) if len(row_vals) > 2 else "Not Specified"
                
                print("\n----------------------------------")
                print(f"Product: {prod_name}")
                print(f"Code: {code}")
                print(f"Origin: {origin}")
                print("----------------------------------")
        else:
            print("\nNo matching records found.")
