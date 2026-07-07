Note: This project intentionally avoids LangChain and LangGraph. The objective was to understand the internals of Retrieval-Augmented Generation by building the complete pipeline manually.


# AI Code Assistant (V1)

An AI-powered repository understanding assistant built with FastAPI, React, ChromaDB, and Gemini/OpenAI compatible APIs.

The goal of this project is to understand how Retrieval-Augmented Generation (RAG) works from scratch by implementing every major component manually instead of relying on frameworks like LangChain.

---

## Features

- Repository indexing
- Automatic code chunking
- Embedding generation
- ChromaDB vector search
- AI-powered codebase Q&A
- Source attribution
- Repository explorer
- File viewer
- Syntax highlighting
- Highlight relevant retrieved code
- Add repositories from local machine

---

## Tech Stack

### Frontend

- React
- Axios
- React Syntax Highlighter

### Backend

- FastAPI
- SQLAlchemy
- SQLite
- ChromaDB

### AI

- Embedding Model
- Gemini/OpenAI Compatible API

---

## Architecture

User

↓

React Frontend

↓

FastAPI

↓

Retrieval Service

↓

ChromaDB

↓

Prompt Builder

↓

LLM

↓

Answer + Sources


---

## Project Structure


backend/

    app/

        api/

        services/

        database/

        models/

frontend/

    src/

    components/

    pages/

    services/





---

## Current Workflow

1. Add a repository.
2. Index source code.
3. Split files into chunks.
4. Generate embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve relevant chunks.
7. Build contextual prompt.
8. Generate AI response.
9. Display answer with clickable sources.
10. Open original source file with highlighted context.

---

## Screenshots

![alt text](<img/Screenshot 2026-07-07 202726.png>)

![alt text](<img/Screenshot 2026-07-07 202828.png>)

![alt text](<img/Screenshot 2026-07-07 203652.png>)

![alt text](<img/Screenshot 2026-07-07 203705.png>)

![alt text](<img/Screenshot 2026-07-07 203741.png>)



---

## Future Improvements

- Conversation memory
- Hybrid Retrieval
- Better chunking strategies
- Re-ranking
- LangChain integration
- LangGraph agents
- Repository-wide search
- Multi-repository support
- Code generation
- Deployment

---

## Learning Goals

This project focuses on understanding:

- Embeddings
- Vector Databases
- RAG
- Prompt Engineering
- Semantic Search
- Repository Indexing
- AI-assisted Code Understanding

instead of relying on high-level frameworks.

---

## Status

Version: **1.0**

This repository represents the first implementation of the AI Code Assistant. Development of advanced features such as LangChain, LangGraph, agent memory, and multi-step reasoning will continue in Version 2.
