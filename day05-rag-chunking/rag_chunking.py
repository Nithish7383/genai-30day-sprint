import chromadb
import ollama

# --------------------------------
# Step 1: Start vector database
# --------------------------------
client = chromadb.Client()

collection = client.create_collection(name="chunked_docs")

# --------------------------------
# Step 2: Large document
# --------------------------------
document = """
Artificial intelligence is a field of computer science focused on building intelligent machines.
Machine learning is a subset of AI that allows computers to learn patterns from data.
Deep learning uses neural networks with many layers to model complex relationships.
Python is one of the most widely used programming languages in AI development.
"""

# --------------------------------
# Step 3: Chunking function
# --------------------------------
def chunk_text(text, chunk_size=120):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

chunks = chunk_text(document)

print("Created Chunks:\n")
for c in chunks:
    print(c)
    print("------")

# --------------------------------
# Step 4: Embedding function
# --------------------------------
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    
    return response["embedding"]

# --------------------------------
# Step 5: Store chunks
# --------------------------------
embeddings = [get_embedding(chunk) for chunk in chunks]

collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(chunks))]
)

print("\nChunks stored in vector database.")

# --------------------------------
# Step 6: Ask question
# --------------------------------
query = input("\nAsk a question: ")

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

retrieved_chunks = results["documents"][0]

print("\nRetrieved Chunks:\n")

for chunk in retrieved_chunks:
    print("-", chunk)

# --------------------------------
# Step 7: Build context
# --------------------------------
context = "\n".join(retrieved_chunks)

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

# --------------------------------
# Step 8: Generate answer
# --------------------------------
response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAI Response:\n")
print(response["message"]["content"])