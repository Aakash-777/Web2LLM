# 🚀 Web2LLM – Crawl the Web, Ask the LLM  
**A Local RAG-Powered Assistant for Website Documentation**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-%23007ACC?logo=langchain)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA3.2-brightgreen)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple)
![Status](https://img.shields.io/badge/Status-Completed-green)

---

## 🌐 Overview

**Web2LLM** is a streamlined pipeline for building a **local Retrieval-Augmented Generation (RAG)** system from entire websites using **LLMs**. It crawls websites, processes the data, stores semantically rich embeddings, and delivers accurate responses to user queries — all from your machine!

> ⚙️ From website → markdown → LLM-ready knowledge base.

---

## ✨ Features

- 🔎 **Automated Website Crawling** via `sitemap.xml` using Crawl4AI.
- 📄 **Markdown Collection** for structured page content.
- 🧠 **Local Language Modeling** with Ollama (LLaMA3.2) and `mxbai-embed-large`.
- 🧬 **Semantic Embeddings** stored in **ChromaDB**.
- 🖥️ **Streamlit UI** for an interactive Q&A experience. (Yet to be updated)

---

## 🛠️ Tech Stack

| Component      | Tool / Library            |
|----------------|----------------------------|
| Language Model | Ollama – LLaMA3.2         |
| Embeddings     | mxbai-embed-large         |
| Crawling       | Crawl4AI                  |
| RAG Framework  | LangChain                 |
| Vector Store   | ChromaDB                  |
| UI             | Streamlit                 |
| Language       | Python 3.10+              |

---

## 🔧 How It Works

1. **Web Crawl**  
   Crawl websites using `Crawl4AI`, save each page in markdown format.

2. **Preprocessing**  
   Merge markdown files into a single `.txt` file for ingestion.

3. **Chunk & Embed**  
   Use LangChain with `mxbai-embed-large` to chunk and embed text.

4. **Store Embeddings**  
   Save them to **ChromaDB** for fast vector retrieval.

5. **Query via UI**  
   Use the Streamlit app to interact with your local RAG system. (Not Yet Updated)

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/web2llm.git
cd web2llm

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py

```

## 💡 Use Cases

- Build offline assistants for tech documentation.
- Power internal knowledge bots for engineering teams.
- Enable semantic search across any static site or wiki.

---

## 🧠 Learnings

- End-to-end implementation of a local RAG pipeline.
- Integration of multiple components: crawling, embedding, storage, UI.
- Hands-on with LLM operations on private, domain-specific data.
