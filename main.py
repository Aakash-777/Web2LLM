from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import read_text_file, split_text, create_documents_from_chunks, create_vector_store, get_retriever

# Step 1: Read and process the text document
text_file_path = "scraped_output.txt"
text = read_text_file(text_file_path)

# Step 2: Split the text into manageable chunks
chunks = split_text(text)

# Step 3: Convert chunks into LangChain Documents
documents = create_documents_from_chunks(chunks)

# Step 4: Create the vector store and embed the documents
vector_store = create_vector_store(documents)

# Step 5: Retrieve relevant documents based on a question
retriever = get_retriever(vector_store)

# Step 6: Set up the LLM for generating answers
model = OllamaLLM(model="llama3.2")

# Step 7: Prepare the prompt template
template = """
This is some information about the website incase you find it useful

{reviews}

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Step 8: Interactive loop for question answering
while True:
    question = input("\nAsk your question (q to quit): ")
    if question.lower() == "q":
        break
    # Retrieve the most relevant paragraphs based on the question
    relevant_reviews = retriever.invoke(question)
    reviews_text = "\n\n".join(doc.page_content for doc in relevant_reviews)
    
    # Generate the answer using the LLM
    answer = chain.invoke({"reviews": reviews_text, "question": question})
    
    print(f"Answer: {answer}")
