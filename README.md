# 📊 Financial Policy Assistant

A GenAI-powered **Financial Policy Assistant** that helps auditors, compliance officers, and financial professionals quickly query complex financial policy documents.  
Built with **Streamlit frontend** and modular `src/` code for embeddings, document loaders, chunking, vector store, and LLM integration.

---

## ✅ 1. Problem Statement

Financial institutions deal with thousands of pages of compliance manuals, regulatory filings, and internal policy documents.  
- Manual searching is slow and error-prone.  
- Misinterpretation can lead to multi-million dollar fines.  
- Staff need instant, accurate, document-grounded answers.  

---

## 🚀 2. Solution

This project provides a **Streamlit-based chatbot** that:  
- Ingests financial policy PDFs and other documents.  
- Converts them into embeddings using **OpenAI embedding models**.  
- Stores them in a **vector store**.  
- Retrieves relevant chunks and passes them to **OpenAI GPT‑4** for grounded answers.  
- Displays answers with citations in a simple UI.

---

## 🏗️ 3. Architecture

```
[User Query] → [Streamlit Frontend] → [src modules]
       ↓                               ↑
   [OpenAI LLM] ← [Relevant Chunks] ← [Vector Store]
       ↑                               ↑
   [Embedding API] ← [Chunked PDFs] ← [Document Loader]
```

### Components
- **Frontend:** `frontend/app.py` (Streamlit UI)  
- **Embeddings:** `src/embeddings.py` (OpenAI embeddings)  
- **Document Loaders:** `src/document_loaders.py` (PDF, DOCX, CSV)  
- **Chunking:** `src/chunking.py` (fixed-size, semantic, table-aware)  
- **Vector Store:** `src/vectorstore.py` (FAISS integration)  
- **LLM Integration:** `src/llm_integration.py` (GPT‑4 Q&A)  
- **Pipeline:** `src/rag_pipeline.py` (optional orchestration)

---

## ⚙️ 4. Installation

### Prerequisites
- Python 3.12+  
- OpenAI API key (set in `.env`)  

### Setup
```bash
git clone <repo-url>
cd financial-policy-assistant
pip install -r requirements.txt
```

Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

---

## 🎨 5. Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

### Features
- Upload financial policy documents (PDF, TXT).  
- Ask compliance questions in natural language.  
- Get citation-backed answers grounded in uploaded documents.  

---

## 📂 6. Project Structure
```bash
financial-policy-assistant/
├── app.py                  # Streamlit frontend UI
│
├── src/                    # Core Backend logic modules
│   ├── __init__.py
│   ├── embeddings.py       # OpenAI embedding functions
│   ├── document_loaders.py # PDF/DOCX/CSV loaders
│   ├── chunking.py         # Chunking strategies
│   ├── vectorstore.py      # FAISS or Pinecone integration
│   ├── rag_pipeline.py     # Orchestration logic (optional)
│   └── llm_integration.py  # GPT-4 query orchestration
│
├── config/
│   └── config.yaml         # Config settings (chunk size, overlap, vector store type)
│
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (OpenAI API key, etc.)
├── .gitignore              # Ignore cache, env, pyc files
│
├── data/
│   └── sample_pdfs/
│       └── .gitkeep        # Placeholder for sample documents
│
├── exploration/
│   └── notebook.ipynb      # Jupyter notebook for experiments
│
├── Project_Preparation/
│   └── README.md           # Documentation / case study notes
│
├── setup.py                # Packaging setup
---

### List of File Created as:
```bash

list_of_files = [
    "src/__init__.py",
    "src/embeddings.py",
    "src/document_loaders.py",
    "src/chunking.py",
    "src/vectorstore.py",
    "src/rag_pipeline.py",
    "src/llm_integration.py",
    "config/config.yaml",
    ".env",
    "setup.py",
    "requirements.txt",
    "app.py",
    "exploration/notebook.ipynb",
    "data/sample_pdfs/.gitkeep",
    "Project_Preparation/README.md",
    ".gitignore",
]
```


## 🌍 7. Impact

- **Compliance Risk Reduction** → grounded answers prevent misinterpretation.  
- **Efficiency Gains** → instant retrieval vs hours of manual searching.  
- **Audit Readiness** → citation-backed responses for regulators.  
- **User Empowerment** → non-technical staff can query complex policies in plain English.  

---

## ✨ 8. Example Queries

- “Summarize RBI circulars on KYC requirements in the last 2 years.”  
- “What is the minimum liquidity coverage ratio under Basel III?”  
- “Compare IFRS vs GAAP treatment of deferred tax assets.”  
- “Highlight conflicting clauses between internal compliance manual and RBI guidelines.”  

---

## 📌 9. Next Steps

- Add support for DOCX, CSV, and HTML loaders.  
- Implement semantic + table-aware chunking.  
- Enhance UI with clause highlighting.  
- Deploy Streamlit app on **Azure Web App**.  
```



## Clone Git Repo
```bash
git clone https://github.com/ajeetkumarAI/Financial-Policy-Assistant-ChatBot.git
```

## Virtual Env
```bash
python -m venv venv
```
##  How to activate virtual env
```bash
venv\Scripts\activate.bat
```

## Create Project Skelton
```bash
python templates.py
```


## Update requirements.txt

## Install the dependency via requirements.txt
```bash
pip install -r requirements.txt
```

## Starts Updating the SRC code asd Backened
```bash
│
├── src/                    # Core Backend logic modules
│   ├── __init__.py
│   ├── embeddings.py       # OpenAI embedding functions
│   ├── document_loaders.py # PDF/DOCX/CSV loaders
│   ├── chunking.py         # Chunking strategies
│   ├── vectorstore.py      # FAISS or Pinecone integration
│   ├── rag_pipeline.py     # Orchestration logic (optional)
│   └── llm_integration.py  # GPT-4 query orchestration
```

## Create Frontend Applications
```bash
app.py
```


## Git Commands
```bash
git status
```

### Track changes 
```bash
git add .
```

### Commit the changes
```bash
git commit -m "Project Skelton Created"
```

### Push changes to Git
```bash
git push origin main
```

### Setup Git Profile
```bash
git config --global user.email "emailid"
git config --global user.name "username"
```

### Push chnages to Git
```bash
git push origin main
```


### Starts Up Command
```bash
streamlit run app.py --server.port=8000 --server.address=0.0.0.0
```
