# Import necessary libraries
import streamlit as st
import tempfile
from src.rag_pipeline import build_rag_chain

st.set_page_config(page_title="Financial Policy Copilot", layout="wide")

st.title("GenAI Powered Financial Policy Copilot 🤖")

uploaded_file = st.file_uploader("Upload a Financial Policy Document (PDF)", type=["pdf"])

use_prompt = st.checkbox("Strictly document only answers", value=True)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
    st.success("File uploaded successfully!")

    @st.cache_resource
    def load_chain(path):
        return build_rag_chain(pdf_path=path, use_prompt=use_prompt)

    qa_chain = load_chain(temp_pdf_path)

query = st.text_input("Enter your question about the document:")

ask_clicked = st.button("Ask",key="ask_button")

if ask_clicked:
    if not uploaded_file:
       st.warning("Please upload a PDF document first.")
    elif not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching Relevant Document and Generating Answer ..."):
            result = qa_chain.invoke({"query": query})
            st.subheader("✅ Answer:")
            st.write(result["result"])
