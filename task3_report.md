# 📊 Task 3: RAG Core Logic and Evaluation Report 
 
## ✅ Overview 
 
In this task, we built a Retrieval-Augmented Generation (RAG) pipeline to answer user questions about customer complaints using a vector database and a language model. The goal is to evaluate how well the system retrieves relevant complaint data and generates appropriate responses. 
 
--- 
 
## 🧠 RAG Pipeline Components 
 
### 1. Retriever 
- Embedding model: `all-MiniLM-L6-v2` from SentenceTransformers 
- Vector store: FAISS index (`vector_store/index.faiss`) 
- Metadata: Python pickle file (`index.pkl`) 
- Top `k=5` chunks retrieved per question using cosine similarity 
 
### 2. Prompt Template 
```text 
You are a financial analyst assistant for CrediTrust. 
Your task is to answer questions about customer complaints. 
Use the following retrieved complaint excerpts to formulate your answer. 
If the context doesn't contain the answer, state that you don’t have enough information. 
 
Context: 
{context} 
 
Question: {question} 
Answer: 
 

3. Generator 

Language model: google/flan-t5-base 

Method: Hugging Face pipeline("text2text-generation", ...) 

Output: Short, focused response based on complaint excerpts 

 

🔎 Evaluation Questions 

We tested the system using 5 representative questions covering different financial products and services. 

 

📋 Evaluation Table 

No. 

Question 

Generated Answer 

Retrieved Sources (2 examples) 

Quality Score (1-5) 

Comments 

1 

What are the most common issues with Buy Now Pay Later? 

I don’t have enough information. 

- Care Credit confusion 
 - Citi Double Cash Card balance issue 

2 

Retrieved complaints were finance-related but not BNPL-specific. Needs filtering by product type. 

2 

How do customers describe their experience with money transfers? 

I don’t have enough information. 

- Sending money to prison 
 - Bank account closed unexpectedly 

3 

Partially relevant, but model didn’t generate a summary. Suggest improving context coverage. 

3 

What problems are common with savings accounts? 

I don’t have enough information. 

- Credit card debt resolution 
 - Application denied for fraud 

2 

Retrieved complaints don’t relate to savings accounts. Retrieval can be improved by product tag filtering. 

4 

Are there complaints about customer service with personal loans? 

Yes 

- Delay in Self Lender payout 
 - Airline charge confusion 

4 

Accurate short answer. Retrieved context is relevant to service complaints. 

5 

Do people complain about late fees on credit cards? 

Yes 

- Synchrony Bank late fees 
 - Spirit Airlines card delay issues 

5 

Excellent retrieval and answer quality. Model used the context properly. 

 

✅ Summary of Results 

Score 

Count 

5 

1 

4 

1 

3 

1 

2 

2 

 

📈 Observations 

Strengths: 

The RAG system successfully avoids hallucination and clearly says "I don’t have enough information" when necessary. 

High-quality answers for well-represented complaint topics like credit cards and customer service issues. 

Prompt template is respected and well-structured. 

Weaknesses: 

Some irrelevant chunks are retrieved due to lack of filtering by product. 

Coverage of niche topics like "Buy Now Pay Later" and "savings accounts" is low. 

Model occasionally outputs “I don’t have enough information” even when partial data is available. 

 

🔧 Recommendations 

Apply filtering on the product field before doing FAISS retrieval to narrow down relevant complaints. 

Fine-tune a smaller LLM on complaint-style text to improve accuracy and coherence. 

Add reranking step using cosine similarity or BM25 to improve result ordering. 

 

📂 Deliverables 

✅ rag_pipeline.py: Core RAG logic including retriever, prompt, and generator 

✅ vector_store/index.faiss, index.pkl: Prebuilt FAISS index and complaint metadata 

✅ task3_report.md: Evaluation summary and observations 

 

Prepared by: Yeabtsega Tilahun 
 Project: CFPB Complaints RAG Assistant 
 Date: July 2025 