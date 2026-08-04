# PDF RAG Chatbot

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)](https://langchain.com)

A powerful **PDF-based Retrieval Augmented Generation (RAG)** chatbot built with FastAPI backend and Streamlit frontend.

## ✨ Features

- 📄 PDF Upload & Processing
- 🔍 Semantic Search with Embeddings
- 💬 Conversational RAG Chat
- 📚 Document Management
- 🎨 Modern Streamlit UI

## 🛠️ Tech Stack

| Layer     | Technologies                          |
|-----------|---------------------------------------|
| Backend   | FastAPI + LangChain + ChromaDB + SQLite |
| Frontend  | Streamlit                             |
| LLM / RAG | LangChain + Embeddings                |

## 📁 Project Structure

```
pdf-rag-chatbot/
├── README.md
├── .gitignore
├── backend/
├── frontend/
└── docs/
```

## 🚀 Quick Start

1. Clone the repository
2. Set up backend & frontend environments
3. Add your API keys
4. Run the services

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
streamlit run app.py
```

## 📄 Documentation

See the `docs/` folder for PRD, Architecture, and more details.

---

Built with ❤️ by [AdnanRaza88](https://github.com/AdnanRaza88)
