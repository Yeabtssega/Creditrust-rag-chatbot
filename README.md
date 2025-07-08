# 🤖 CrediTrust RAG Chatbot

An interactive Retrieval-Augmented Generation (RAG) assistant for answering financial complaint-related questions using real consumer complaint data.

## 🔍 Project Overview

This project demonstrates a complete RAG pipeline that allows users to ask questions about customer complaints submitted to financial institutions. It retrieves relevant complaint excerpts using semantic search (FAISS) and generates concise answers using a fine-tuned language model (Flan-T5).

The project was developed as part of an AI assistant challenge and supports:

- Free-text user questions
- Dynamic answer generation
- Transparent complaint source display
- A simple, intuitive web interface via Gradio

---

## 🧱 RAG Architecture

| Component      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Retriever**  | Uses `all-MiniLM-L6-v2` sentence transformer to embed complaints into FAISS |
| **Generator**  | Uses `google/flan-t5-base` to generate answers from retrieved context       |
| **Prompt**     | Designed to avoid hallucination and use only the retrieved complaints       |
| **Interface**  | Built using Gradio for easy use by non-technical users                      |

---

## 💻 How to Run the App

### ✅ Prerequisites

- Python 3.8 or later
- Install required packages:


pip install -r requirements.txt
🚀 Run the app

python app.py
Then open your browser to:

http://127.0.0.1:7860
🧠 Sample Questions to Try
What are the most common issues with Buy Now Pay Later?

What do customers complain about with credit card payments?

Are there complaints about personal loan customer service?

What problems are common with savings accounts?

📸 Screenshots
Ask a question	See answers and sources

📂 Folder Structure

creditrust-rag-chatbot/
│
├── app.py                  # Gradio interface for user input/output
├── rag_pipeline.py         # RAG pipeline logic: retrieval + generation
├── vector_store/
│   ├── index.faiss         # Vector database of embedded complaints
│   └── index.pkl           # Metadata for retrieved chunks
├── screenshots/            # Screenshots of the running app
├── task3_report.md         # Evaluation and analysis of the RAG system
├── task4_report.md         # Description and UI documentation
├── requirements.txt        # Python dependencies
└── README.md               # Project overview (this file)
🛠 Features
✅ RAG pipeline using FAISS and Hugging Face Transformers

✅ Prompt template for reliable answers

✅ Gradio UI for non-technical users

✅ Source complaints displayed for transparency

✅ Works locally with a single Python script

📜 License
This project is licensed under the MIT License.

🙋‍♀️ Author
Yeabtsega Tilahun
