import chromadb
import ollama

# -----------------------------
# Step 1: Start Vector Database
# -----------------------------
client = chromadb.Client()

collection = client.create_collection(name="memory_docs")

# -----------------------------
# Step 2: Knowledge Base
# -----------------------------
documents = [
    "Artificial intelligence enables machines to perform tasks that normally require human intelligence.",
    "Machine learning is a subset of artificial intelligence where systems learn patterns from data.",
    "Deep learning uses neural networks with multiple layers to learn complex patterns.",
    "Python is widely used for building AI and machine learning applications."
]

# -----------------------------
# Step 3: Embedding Function
# -----------------------------
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]

# -----------------------------
# Step 4: Store Documents
# -----------------------------
embeddings = [get_embedding(doc) for doc in documents]

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

print("Knowledge base loaded.\n")

# -----------------------------
# Step 5: Conversation Memory
# -----------------------------
conversation_history = []

# -----------------------------
# Step 6: Chat Loop
# -----------------------------
while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    # Convert query to embedding
    query_embedding = get_embedding(query)

    # Retrieve relevant documents
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    retrieved_docs = results["documents"][0]
    context = "\n".join(retrieved_docs)

    # Add user message to memory
    conversation_history.append({"role": "user", "content": query})

    # Build prompt with memory
    prompt = f"""
You are an AI assistant.

Use the provided context and conversation history to answer the question.

Rules:
1. Prefer information from the context.
2. Use conversation history if the question refers to previous messages.
3. If the answer is not in the context, respond with:
"I could not find the answer in the provided documents."
4. Keep the answer clear and concise.

Context:
{context}

Conversation History:
{conversation_history}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    print("\nAI:", answer, "\n")

    # Store AI response in memory
    conversation_history.append({"role": "assistant", "content": answer})