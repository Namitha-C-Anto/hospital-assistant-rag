import os
from dotenv import load_dotenv 
load_dotenv(override=True)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
DOCS_PATH = os.path.join(BASE_DIR, "docs")
DB_PATH = os.path.join(BASE_DIR, "db", "faiss_index")

# Embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Text splitting
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200

# Retriever
TOP_K = 5
SEARCH_TYPE = "similarity"

# LLM
LLM_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.2

# App
APP_TITLE = "🏥 Conversational Hospital Assistant"
SUB_TITLE = "AI-powered hospital knowledge assistant with memory and retrieval capabilities"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")