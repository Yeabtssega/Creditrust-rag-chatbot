# src/task2_embed_index.py

import pandas as pd
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle
from tqdm import tqdm

# Step 1: Load cleaned data
df = pd.read_csv("data/filtered_complaints.csv")
print(f"Loaded {len(df)} complaints")

# Step 2: Chunking Setup
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " "],
    length_function=len
)

# Step 3: Prepare all text chunks and metadata
texts = []
metadatas = []

print("🔄 Chunking complaints...")
for i, row in tqdm(df.iterrows(), total=len(df)):
    chunks = text_splitter.split_text(row["cleaned_narrative"])
    for chunk in chunks:
        texts.append(chunk)
        metadatas.append({
            "complaint_index": i,
            "product": row["Product"],
            "original_text": row["Consumer complaint narrative"][:300]
        })

print(f"✅ Total chunks: {len(texts)}")

# Step 4: Load embedding model
print("🔗 Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 5: Embed chunks
print("🔍 Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

# Step 6: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Step 7: Save FAISS index and metadata
os.makedirs("vector_store", exist_ok=True)
faiss.write_index(index, "vector_store/index.faiss")
with open("vector_store/index.pkl", "wb") as f:
    pickle.dump(metadatas, f)

print("✅ Vector store saved to 'vector_store/'")
