import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
import pandas as pd

# Step 1: Read the text document
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Step 2: Split the text into smaller chunks
def split_text(text, chunk_size=500, chunk_overlap=50):
    text_splitter = CharacterTextSplitter(
        separator="\n",  # Split at paragraph breaks or new lines
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(text)

# Step 3: Convert text chunks into LangChain Documents
def create_documents_from_chunks(chunks):
    return [Document(page_content=chunk) for chunk in chunks]

# Step 4: Embed the documents using Ollama embeddings
def create_vector_store(documents, db_location="./website_chromadb"):
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    
    # Check if Chroma DB already exists
    add_documents = not os.path.exists(db_location)
    
    vector_store = Chroma(
        collection_name="crawl4ai_docs",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    
    if add_documents:
        vector_store.add_documents(documents=documents)
    
    return vector_store

# Step 5: Get the retriever for searching the vector store
def get_retriever(vector_store, k=5):
    return vector_store.as_retriever(search_kwargs={"k": k})

