# 🏥 Conversational Hospital Assistant RAG

AI-powered Hospital Assistant built using Retrieval-Augmented Generation (RAG) for hospital knowledge retrieval from PDF documents with conversational memory support.

The application allows users to ask hospital-related questions and receive context-aware answers generated using retrieved document information and conversation history.

---

## 🚀 Features

✅ PDF document ingestion  
✅ PDF chunking using Recursive Character Text Splitter  
✅ Embeddings generation using HuggingFace Embeddings  
✅ FAISS Vector Database for semantic search  
✅ Conversational Retrieval-Augmented Generation (RAG)  
✅ Chat memory for follow-up questions  
✅ Streamlit chat interface  
✅ Retrieved context visibility for debugging and transparency  
✅ Modular project structure for scalability  

---

## 🏗️ Architecture

```

PDF Documents
↓
Loader
↓
Text Splitter
↓
Embeddings
(HuggingFace)

↓

FAISS Vector Store
↓
Retriever
↓
Retrieved Context

Chat Memory
↓
Prompt Template
(Context + Memory + Question)
↓
LLM
↓
Response

---

##📂 Project Structure

```

Hospital_Assistant/

├── app.py
├── build_db.py
├── config.py
├── requirements.txt
├── README.md
│
├── docs/
│ ├── infection_control.pdf
│ ├── meningitis_diagnosis.pdf
│ └── standard_treatment_guidelines.pdf
│
├── db/
│ └── faiss_index/
│
├── rag/
│ ├── loader.py
│ ├── splitter.py
│ ├── vectorstore.py
│ └── retriever.py
│
├── llm/
│ └── llm.py
│
├── memory/
│ └── session_memory.py
│
└── prompts/
└── prompt_template.py

## ⚙️ Technologies Used
Python
LangChain
HuggingFace Embeddings
FAISS
Streamlit
Retrieval-Augmented Generation (RAG)
Conversational Memory

## 🧠 Current Memory Implementation

Current implementation uses session-based conversational memory:

Stores previous questions and answers
Supports follow-up questions
Maintains conversation continuity

Example:


User: What is meningitis?

Assistant: ...

User: What are its symptoms?

Assistant understands "its" → meningitis

## 🔧 Installation

Clone repository:

git clone <your_repo_url>

cd conversational-hospital-assistant-rag

Create virtual environment:

python -m venv .venv

Activate environment:

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## 📚 Build Vector Database

Before running application:

python build_db.py

This will:

Load PDF documents
Split documents into chunks
Generate embeddings
Create and save FAISS vector database

## ▶️ Run Application
streamlit run app.py

## 🎯 Example Questions
What is meningitis?
What are symptoms of anal fissure?
Explain infection control measures.
What are standard treatment guidelines?

## 🔮 Future Improvements

Planned enhancements:

Buffer window memory (last N conversations)
Conversation summarization
Hybrid retrieval (Semantic + Keyword Search)
History-aware retrieval
SQL + PDF Router RAG
Advanced memory retrieval systems
Deployment optimization

## 👩‍💻 Author

Namitha C Anto

SQL Backend Developer transitioning into AI Engineering with focus on:

Retrieval-Augmented Generation (RAG)
Conversational AI
Agentic AI Systems
LLM Application Engineering

## ⭐ Project Goal

Build AI systems from foundational concepts instead of relying only on abstractions and frameworks, with focus on understanding retrieval systems, memory, orchestration, and production-oriented AI engineering.


This README shows:
- Current implementation clearly
- Future roadmap
- Engineering thinking
- Your transition story without overselling

It is strong for GitHub + recruiter viewing.
