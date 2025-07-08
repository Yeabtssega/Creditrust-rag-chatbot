import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline, AutoTokenizer

# Load embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Load tokenizer for input length management
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

# Load vector store + metadata
with open("vector_store/index.pkl", "rb") as f:
    data = pickle.load(f)

if isinstance(data, dict):
    texts = data["texts"]
    metadata = data.get("metadata", [])
else:
    texts = data
    metadata = []

index = faiss.read_index("vector_store/index.faiss")

# Load generator model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def retrieve(question, k=8):
    question_embedding = embedder.encode([question])
    _, indices = index.search(np.array(question_embedding), k)

    # Return metadata dict if available, else fallback to text dict
    sources = []
    for i in indices[0]:
        if metadata and i < len(metadata):
            sources.append(metadata[i])
        else:
            # fallback
            if isinstance(texts[i], dict):
                sources.append(texts[i])
            else:
                sources.append({"text": texts[i]})
    return sources

def truncate_context(chunks, max_tokens=450):
    total_tokens = 0
    selected_chunks = []
    for chunk in chunks:
        text = chunk.get("original_text") or chunk.get("text", "")
        if len(text) < 30:  # skip very short chunks
            continue
        tokens = tokenizer.tokenize(text)
        chunk_token_len = len(tokens)
        if total_tokens + chunk_token_len > max_tokens:
            break
        selected_chunks.append(chunk)
        total_tokens += chunk_token_len
    return selected_chunks

def format_prompt(question, context_chunks):
    context_texts = [c.get("original_text") or c.get("text", "") for c in context_chunks]
    context = "\n".join(context_texts)
    return f"""
You are a financial analyst assistant for CrediTrust.
Your task is to answer questions about customer complaints in detail.
Use the following retrieved complaint excerpts to formulate a comprehensive answer.
If the context doesn't contain the answer, state that you don’t have enough information.

Context:
{context}

Question: {question}
Answer:
"""

def answer_question(question):
    try:
        top_chunks = retrieve(question)
        if not top_chunks:
            return "No relevant complaints found.", []

        truncated_chunks = truncate_context(top_chunks)

        prompt = format_prompt(question, truncated_chunks)
        result = generator(
            prompt,
            max_length=350,
            do_sample=True,
            temperature=0.85
        )[0]["generated_text"]

        return result.strip(), truncated_chunks

    except Exception as e:
        print("❌ ERROR in answer_question:", e)
        return "An error occurred while generating the response.", []
