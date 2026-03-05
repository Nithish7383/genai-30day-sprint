import chromadb
import ollama

# Start chroma client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="knowledge_base")

documents = [
    "Python is widely used in artificial intelligence",
    "Machine learning allows computers to learn patterns from data",
    "Artificial intelligence is transforming industries",
    "Basketball is played using a ball and hoop",
    "Football is the most popular sport in the world"
]

def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]

embeddings = [get_embedding(doc) for doc in documents]

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

print("Documents stored successfully!")

query = "How do machines learn?"

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("\nQuery:", query)
print("\nTop results:")

for doc in results["documents"][0]:
    print("-", doc)