import os
import re
import warnings
import logging
import openpyxl
from pypdf import PdfReader

warnings.filterwarnings("ignore")
logging.getLogger("pypdf").setLevel(logging.ERROR)

pdf_folder = r"C:\Users\syeda\Desktop\Specs"
excel_output = os.path.join(pdf_folder, "Product_Specs_Summary.xlsx")

data = []

print("PDFs se data aur Country of Origin smart-detect ho raha hai...")

def detect_country(prod_name, text):
    combined = (str(prod_name) + " " + str(text)).lower()
    
    # Smart Keyword Mapping
    if any(k in combined for k in ['iran', 'iranian']):
        return 'Iran'
    if any(k in combined for k in ['china', 'chinese', 'yunnan']):
        return 'China'
    if any(k in combined for k in ['california', 'californian', 'usa', 'america']):
        return 'USA'
    if any(k in combined for k in ['pakistan', 'aseel']):
        return 'Pakistan'
    if any(k in combined for k in ['turkey', 'turkish']):
        return 'Turkey'
    if any(k in combined for k in ['india', 'indian']):
        return 'India'
    if any(k in combined for k in ['sri lanka', 'ceylon']):
        return 'Sri Lanka'
    if any(k in combined for k in ['vietnam']):
        return 'Vietnam'
    if any(k in combined for k in ['poland']):
        return 'Poland'
    if any(k in combined for k in ['peru']):
        return 'Peru'
    if any(k in combined for k in ['australia']):
        return 'Australia'
    
    # Search via regex inside PDF text for Country of Origin
    origin_match = re.search(r'(?:Country of Origin|Origin|Made in)\s*[:\-]?\s*([A-Za-z\s,]+)', text, re.IGNORECASE)
    if origin_match:
        found = origin_match.group(1).strip()
        lines = [l.strip() for l in found.split('\n') if l.strip()]
        if lines:
            candidate = lines[0][:50]
            # Ignore boilerplate text
            boilerplate = ['al specification', 'gm status', 'of the material', 'available upon', 'prior', 'request']
            if not any(b in candidate.lower() for b in boilerplate):
                return candidate
                
    return 'N/A'

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        file_path = os.path.join(pdf_folder, filename)
        name_without_ext, _ = os.path.splitext(filename)
        
        # 1. Product Code (SUFL code)
        code_match = re.search(r'(SUFL\s*\d+)', name_without_ext, re.IGNORECASE)
        product_code = code_match.group(1).replace(" ", "").upper() if code_match else "N/A"
        
        # 2. Product Name
        prod_name = name_without_ext
        if code_match:
            prod_name = prod_name.replace(code_match.group(1), "")
        prod_name = re.sub(r'^[-–—_.,()]+|[-–—_.,()]+$', '', prod_name).strip()
        product_name = " ".join(prod_name.split())
        
        # 3. Read PDF text
        full_text = ""
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
        except Exception as e:
            pass
            
        # 4. Get Country of Origin
        country_of_origin = detect_country(product_name, full_text)
            
        data.append({
            "Product Code": product_code,
            "Product Name": product_name,
            "Country of Origin": country_of_origin
        })

# Excel Workbook Creation
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Product Specs"

ws.append(["Product Code", "Product Name", "Country of Origin"])

for item in data:
    ws.append([item["Product Code"], item["Product Name"], item["Country of Origin"]])

wb.save(excel_output)
print(f"\nTask Complete! Updated Excel sheet save ho gayi hai:\n{excel_output}")