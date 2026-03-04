import ollama
import numpy as np

# Function to generate embedding
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return np.array(response["embedding"])

# Cosine similarity calculation
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Sentences to test
text1 = "I love learning artificial intelligence"
text2 = "I enjoy studying machine learning"
text3 = "Pizza tastes amazing"

# Generate embeddings
emb1 = get_embedding(text1)
print("Embedding length:", len(emb1))
emb2 = get_embedding(text2)
emb3 = get_embedding(text3)

# Calculate similarity
print("AI similarity:", cosine_similarity(emb1, emb2))
print("AI vs Pizza similarity:", cosine_similarity(emb1, emb3))


# Query search
query = "How to learn chest workout"

documents = [
    "Machine learning tutorials",
    "Artificial intelligence course",
    "Best pizza recipe",
    "Workout plan for muscle gain"
]

query_emb = get_embedding(query)

print("\nQuery Similarity Results:\n")

best_doc = None
best_score = -1

for doc in documents:

    score = cosine_similarity(query_emb, get_embedding(doc))

    print(doc, "→", round(score, 3))

    if score > best_score:
        best_score = score
        best_doc = doc


print("\nMost relevant document:")
print(best_doc, "with score", round(best_score,3))