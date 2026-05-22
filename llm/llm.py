from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY

def get_llm():
        
    llm = ChatOpenAI(
        model= "gpt-4o-mini",
        api_key= OPENAI_API_KEY,
        temperature=0
    )
    return llm