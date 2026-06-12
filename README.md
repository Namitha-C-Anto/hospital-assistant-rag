---

title: Hospital Assistant RAG
emoji: 🚀
colorFrom: red
colorTo: red
sdk: streamlit
app_file: app.py
pinned: false
short_description: AI-powered Hospital Assistant using RAG and FAISS vector search
---


# 🏥 Conversational Hospital Assistant RAG

An AI-powered Hospital Assistant built using Retrieval-Augmented Generation (RAG) to answer hospital-related queries from PDF-based knowledge sources. The application combines semantic search, conversational memory, and Large Language Models (LLMs) to provide accurate, context-aware responses.

Users can interact with the assistant through a Streamlit-based chat interface and receive answers grounded in hospital documents while maintaining conversational continuity across follow-up questions.

---

## 🚀 Features

* PDF document ingestion and processing
* Text chunking using Recursive Character Text Splitter
* Embedding generation using HuggingFace Embeddings
* FAISS Vector Database for semantic similarity search
* Conversational Retrieval-Augmented Generation (RAG)
* Session-based chat memory for follow-up questions
* Streamlit chat interface
* Retrieved context visibility for transparency and debugging
* Modular and scalable project architecture

---

## 🏗️ Architecture

```text
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
```

---

## 📂 Project Structure

```text
Hospital_Assistant/

├── app.py
├── build_db.py
├── config.py
├── requirements.txt
├── README.md
│
├── docs/
│   ├── admission_and_discharge_process.pdf
│   ├── appointment_booking_guide.pdf
│   ├── department_directory.pdf
│   ├── diagnostic_imaging_guide.pdf
│   ├── hospital_services_brochure.pdf
│   ├── infection_prevention_for_patients_and_visitors.pdf
│   ├── laboratory_services_guide.pdf
│   ├── patient_registration_guide.pdf
│   ├── patient_rights_and_responsibilities.pdf
│   ├── sunrise_multi_specialty_hospital.pdf
│   └── visitor_guidelines.pdf
│
├── db/
│   └── faiss_index/
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── vectorstore.py
│   └── retriever.py
│
├── llm/
│   └── llm.py
│
├── memory/
│   └── session_memory.py
│
└── prompts/
    └── prompt_template.py
```

---

## ⚙️ Technologies Used

* Python
* LangChain
* OpenAI GPT-4o Mini
* HuggingFace Embeddings
* FAISS Vector Database
* Streamlit
* Retrieval-Augmented Generation (RAG)
* Conversational Memory

---

## 🧠 Current Memory Implementation

The application currently uses session-based conversational memory to maintain context throughout a user session.

### Capabilities

* Stores previous user questions and assistant responses
* Supports follow-up questions using conversation history
* Maintains conversational continuity across interactions

---

## 🔧 Installation

### Clone the Repository

```bash
git clone <your_repo_url>
cd conversational-hospital-assistant-rag
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

The vector database will be automatically created if it does not already exist.

```bash
streamlit run app.py
```

---

## 🎯 Example Questions

* How do I book an appointment at the hospital?
* What documents are required for patient registration?
* What services are available in the Radiology Department?
* What laboratory services does the hospital provide?
* What are the patient rights and responsibilities?
* What are the hospital's visitor guidelines?
* What infection prevention measures should patients and visitors follow?
* What is the admission and discharge process?
* Which departments are available in the hospital?
* What diagnostic imaging services are offered?
* Tell me about Sunrise Multi-Specialty Hospital.
* What should I bring when visiting the hospital?

---

## 🔮 Future Improvements

Planned enhancements include:

* Buffer window memory (last N conversations)
* Conversation summarization
* Hybrid retrieval (Semantic Search + Keyword Search)
* History-aware retrieval
* SQL + PDF Router RAG
* Advanced memory retrieval systems
* Agent-based retrieval workflows
* Deployment optimization

---

## 👩‍💻 Author

**Namitha C Anto**

SQL Backend Developer transitioning into AI Engineering, with a focus on:

* Retrieval-Augmented Generation (RAG)
* Conversational AI
* Agentic AI Systems
* LLM Application Engineering

---

## ⭐ Project Goal

The goal of this project is to build AI systems from foundational concepts rather than relying solely on high-level abstractions and frameworks. The focus is on developing a deep understanding of retrieval systems, conversational memory, orchestration, and production-oriented AI engineering practices.
