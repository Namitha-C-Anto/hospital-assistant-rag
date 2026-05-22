from config import SEARCH_TYPE, TOP_K

def create_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={"k": TOP_K}
    )