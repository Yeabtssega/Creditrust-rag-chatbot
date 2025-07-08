import gradio as gr
from rag_pipeline import answer_question

def format_sources(sources):
    formatted = []
    for s in sources:
        idx = s.get("complaint_index", "N/A")
        product = s.get("product", "Unknown product")
        text = s.get("original_text") or s.get("text", "")
        preview = text[:400].strip()
        if len(text) > 400:
            preview += "..."
        formatted.append(f"Complaint #{idx} — Product: {product}\n\"{preview}\"")
    return "\n\n---\n\n".join(formatted)

def rag_chat(user_question):
    answer, sources = answer_question(user_question)
    sources_text = format_sources(sources) if sources else "No sources found."
    return answer, sources_text

with gr.Blocks() as demo:
    gr.Markdown("# CrediTrust RAG Assistant")
    user_input = gr.Textbox(label="Ask questions about financial complaints")
    answer_output = gr.Textbox(label="AI Answer")
    sources_output = gr.Textbox(label="Retrieved Complaint Sources", lines=10)
    submit_btn = gr.Button("Submit")
    clear_btn = gr.Button("Clear")

    submit_btn.click(rag_chat, inputs=user_input, outputs=[answer_output, sources_output])
    clear_btn.click(lambda: ("", ""), inputs=None, outputs=[answer_output, sources_output])

demo.launch()
