from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from src.document_loaders import load_pdf
from src.chunking import chunk_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore
from src.llm_integration import get_llm


def build_rag_chain(
    pdf_path: str,
    use_prompt: bool = True,
    k: int = 10
):
    #1. Load Documents
    documents = load_pdf(pdf_path)

    #2. Chunk Documents
    chunks = chunk_documents(documents)

    #3. Get Embeddings Model
    embeddings = get_embeddings()

    #4. Create Vectorstore
    vectorstore = create_vectorstore(chunks, embeddings)

    # 5. Get LLM
    llm = get_llm()

    # 6. Create RetrievalQA Chain
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})

    # 6. RAG Chain
    if use_prompt:
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
You are a helpful assistant answering strictly from the uploaded Document.

Context:
{context}

Question:
{question}

Answer:
"""
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=False
        )
    else:
        qa_chain = RetrievalQA.from_llm(llm, retriever=retriever)

    return qa_chain
