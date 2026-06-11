import os 
from langchain_community.document_loaders import PyPDFLoader
 
def load_documents_from_folder(folder_path):
    documents = []
    for doc in os.listdir(folder_path):
        if doc.endswith(".pdf"):
            file_path = os.path.join(folder_path, doc)

            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
            
    return documents

