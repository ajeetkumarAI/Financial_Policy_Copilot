from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks, embeddings):
    # Create FAISS index directly from documents
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    return vectorstore


# def create_vectorstore(chunks, embeddings, persist_dir="./chroma_db"):
#     return Chroma.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#         persist_directory=persist_dir
#     )