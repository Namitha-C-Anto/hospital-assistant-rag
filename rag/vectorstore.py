from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL, DB_PATH

#Create embedding model
def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

#Create Vector Store
def create_vectorstore(documents):
    embeddings = get_embeddings()
    vectorstore =  FAISS.from_documents(documents=documents, embedding=embeddings)
    return vectorstore

#Save Vector Store
def save_vectorstore(vectorstore, path=DB_PATH):
    vectorstore.save_local(path)

def load_vectorstore(path=DB_PATH):
    embeddings = get_embeddings()
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)