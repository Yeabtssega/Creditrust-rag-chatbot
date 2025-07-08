Task 4 Report: Creating an Interactive Chat Interface for CrediTrust RAG System
Overview
In Task 4, I developed an interactive web interface that allows non-technical users to interact easily with the Retrieval-Augmented Generation (RAG) pipeline built in Task 3. The interface supports free-text questions about customer financial complaints and returns AI-generated answers along with the complaint sources used to produce those answers.

Features Implemented
Text Input Box: Users can type any question about financial complaints.

Submit Button: Sends the question to the backend RAG system and generates a response.

Answer Display: Shows the AI-generated answer in a clear, readable format.

Source Display: Below the answer, displays the retrieved complaint excerpts with complaint ID, product name, and text preview for transparency and trust.

Clear Button: Resets the input and output fields to start a new query.

Error Handling: Handles cases where no relevant complaints are found or errors occur gracefully.

Technical Details
Built using Gradio, a Python library for creating simple, intuitive web UIs.

Integrated with the rag_pipeline.py that handles retrieval (via FAISS) and generation (using Hugging Face’s flan-t5-base model).

Retrieval returns top 8 relevant complaint chunks with metadata, truncated to keep prompt within token limits.

Generation uses sampling with temperature 0.85 for natural responses, max length 350 tokens.

Sources formatted neatly for UI display showing complaint ID, product, and text excerpt.

Usage
Run the app locally:

bash
Copy
Edit
python app.py
Open your browser at http://127.0.0.1:7860 (or the link provided by Gradio).

Type a question related to financial complaints in the input box.

Click Submit to get an AI-generated answer and relevant complaint excerpts displayed below.

Use Clear to reset and ask another question.

Screenshots / Demo
(Insert your screenshots or embed GIF here showing the app UI, question input, AI answer, and displayed sources)

Limitations and Future Improvements
Streaming response: Currently the full answer is shown after generation completes; adding token-by-token streaming would improve user experience.

Filtering: More advanced filtering of complaints by product or issue category could improve relevance.

UI enhancements: Adding pagination for sources, better formatting, and loading spinners can improve usability.

Deployment: The app is currently local; deploying to a cloud service with a public URL is recommended for wider accessibility.

Conclusion
The interactive chat interface successfully meets the requirements of Task 4 by providing an easy-to-use web UI that connects to the RAG system, supports question answering about financial complaints, and enhances trust through transparent source display.