import os
import pandas as pd
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load Excel Summary
excel_path = "Product_Specs_Summary.xlsx" # Apne file ka path yahan adjust kar sakte hain agar zaroorat ho
if os.path.exists(excel_path):
    df_excel = pd.read_excel(excel_path)
    print(f"Loaded Excel Summary with {len(df_excel)} rows.")

# 2. Extract Text from 400+ PDFs folder (e.g., 'pdfs' folder)
pdf_folder = "pdfs" # Apne PDFs wale folder ka name yahan dein
documents = []

if os.path.exists(pdf_folder):
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(pdf_folder, file))
            text = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
            documents.append({"source": file, "content": text})
    print(f"Successfully loaded {len(documents)} PDF specification files.")
else:
    print(f"Directory '{pdf_folder}' not found. Please place your PDFs in a folder named 'pdfs'.")

# 3. Create Embeddings & Search Index
if documents:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = [doc["content"] for doc in documents]
    embeddings = model.encode(texts)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    print("RAG Vector Database successfully built and ready for queries!")