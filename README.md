# 🧾 Talk to PDF

**Talk to PDF** is a simple Streamlit app that allows you to upload a PDF file, ask questions about its content, and get intelligent answers using the **LLaMA 3.3 70B** model via the Groq API.

---
## ScreenShot 

![Image](https://github.com/user-attachments/assets/43f14938-0eed-484b-b32c-3765c3eb10d1)

---

## 🚀 Features

- 📄 Upload any PDF file.
- 🤖 Ask questions based on the PDF content.
- 💡 Receive contextual answers powered by the **LLaMA 3.3 70B** model.
- ⚡ Fast and easy to use Streamlit interface.

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – for PDF text extraction
- [Groq API](https://console.groq.com/) – for interacting with the LLaMA 3 model

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/talk-to-pdf.git
cd talk-to-pdf
```
###  2.Add Your Groq API Key
Open the `app.py` file and replace the placeholder with your actual Groq API key:

```python
API_KEY = "your-groq-api-key-here"
```
### 3.How to Run the App

```python
streamlit run app.py

```
Then open the provided local URL in your browser (usually http://localhost:8501).


### 🔍 How It Works

1. 📤 The user uploads a PDF file.
2. 🧾 The app extracts the first 5000 characters of text using **PyMuPDF**.
3. ❓ The user inputs a question related to the document.
4. 📡 The app sends a prompt (**context + question**) to **Groq’s LLaMA model**.
5. 🤖 The model returns a contextual answer based on the extracted content.

