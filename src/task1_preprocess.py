# src/task1_preprocess_large.py

import pandas as pd
import re
import os
import csv

# Step 0: Setup
input_path = "data/complaints.csv"
output_path = "data/filtered_complaints.csv"
target_products = {
    "Credit card",
    "Personal loan",
    "Buy Now, Pay Later (BNPL)",
    "Savings account",
    "Money transfers"
}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Prepare output CSV with headers
os.makedirs("data", exist_ok=True)
with open(output_path, mode='w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(["Product", "Consumer complaint narrative", "cleaned_narrative"])

# Step 1: Process in chunks
chunk_size = 100000
chunk_num = 0
filtered_rows = 0

print("🔄 Processing file in chunks...")

for chunk in pd.read_csv(input_path, chunksize=chunk_size, low_memory=False):
    chunk_num += 1
    print(f"👉 Processing chunk #{chunk_num} ({len(chunk)} rows)")

    # Filter relevant products and non-empty narratives
    chunk = chunk[chunk["Product"].isin(target_products)]
    chunk = chunk.dropna(subset=["Consumer complaint narrative"])

    # Clean narrative text
    chunk["cleaned_narrative"] = chunk["Consumer complaint narrative"].apply(clean_text)

    # Append filtered & cleaned chunk to output
    chunk[["Product", "Consumer complaint narrative", "cleaned_narrative"]].to_csv(
        output_path,
        mode='a',
        header=False,
        index=False
    )

    filtered_rows += len(chunk)
    print(f"✅ Added {len(chunk)} rows to filtered_complaints.csv")

print(f"\n✅ DONE. Total filtered & cleaned rows saved: {filtered_rows}")
