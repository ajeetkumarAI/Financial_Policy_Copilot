
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="gpt-5-nano-2025-08-07",
        temperature=0,
        streaming=True,
        verbose=True,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
