import streamlit as st
import fitz  # PyMuPDF
import requests

API_KEY = ""
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_ID = "llama-3.3-70b-versatile"

def extract_pdf_text(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text[:5000]  # limit length to avoid token limit

st.title("Talk to PDF ")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
question = st.text_input("Ask a question about the PDF")

if uploaded_file and question:
    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_pdf_text(uploaded_file)

    prompt = f"Context:\n{extracted_text}\n\nQuestion: {question}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
    }

    with st.spinner("Getting answer from Groq LLaMA..."):
        response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        st.subheader("Answer:")
        st.write(answer)
    else:
        st.error(f"Error {response.status_code}: {response.text}")
