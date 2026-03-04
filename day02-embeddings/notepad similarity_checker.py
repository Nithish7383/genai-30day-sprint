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
emb2 = get_embedding(text2)
emb3 = get_embedding(text3)

# Calculate similarity
print("AI similarity:", cosine_similarity(emb1, emb2))
print("AI vs Pizza similarity:", cosine_similarity(emb1, emb3))