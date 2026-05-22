from rag.loader import load_documents_from_folder
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore, save_vectorstore
from config import DOCS_PATH

# Step 1: Load documents
documents = load_documents_from_folder(DOCS_PATH)

# Step 2: Split into chunks
docs_chunk = split_documents(documents)

# Step 3: Create vector store
vectorstore = create_vectorstore(docs_chunk)

# Step 4: Save vector DB
save_vectorstore(vectorstore)

print("✅ Vector database created and saved!")