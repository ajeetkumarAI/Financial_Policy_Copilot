# Import library
import streamlit as st
import tempfile

from src.rag_pipeline import build_rag_chain

st.set_page_config(page_title="PDF RAG Assistant", layout="wide")
st.title("📄 RAG Powered Financial Policy Assistant")

uploaded_pdf = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

use_prompt = st.sidebar.checkbox("Strict document-only answers", value=True)

qa_chain = None

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        pdf_path = tmp.name

    st.success("PDF uploaded successfully")

    @st.cache_resource
    def load_chain(path):
        return build_rag_chain(
            pdf_path=path,
            use_prompt=use_prompt
        )

    qa_chain = load_chain(pdf_path)

query = st.text_input(
    "Ask a question from the PDF",
    placeholder="e.g. List all procurement quote requirements by purchase value"
)

ask_clicked = st.button("Ask", key="ask_button")

if ask_clicked:
    if not uploaded_pdf:
        st.warning("Please upload a PDF first.")
    elif not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching Relevant Documents and Generating Answer..."):
            result = qa_chain.invoke({"query": query})
            st.subheader("Answer")
            st.write(result["result"])
