import chromadb
import ollama

# -----------------------------
# Step 1: Start Vector Database
# -----------------------------
client = chromadb.Client()

collection = client.create_collection(name="rag_documents")

# -----------------------------
# Step 2: Knowledge Base
# -----------------------------
documents = [
    "Artificial intelligence enables machines to perform tasks that normally require human intelligence.",
    "Machine learning is a subset of artificial intelligence where systems learn patterns from data.",
    "Deep learning uses neural networks to model complex patterns.",
    "Python is one of the most popular programming languages for AI development."
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
# Step 4: Convert documents into embeddings
# -----------------------------
embeddings = [get_embedding(doc) for doc in documents]

# Store them
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

print("Knowledge base stored.")

# -----------------------------
# Step 5: User Question
# -----------------------------
query = input("\nAsk a question: ")

query_embedding = get_embedding(query)

# -----------------------------
# Step 6: Retrieve relevant docs
# -----------------------------
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

retrieved_docs = results["documents"][0]

print("\nRetrieved Context:")
for doc in retrieved_docs:
    print("-", doc)

# -----------------------------
# Step 7: Build Prompt
# -----------------------------
context = "\n".join(retrieved_docs)

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

# -----------------------------
# Step 8: Generate Answer
# -----------------------------
response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nAI Response:\n")
print(response["message"]["content"])