# Day 2 – Embeddings Similarity Engine

This project demonstrates how semantic similarity works using embeddings and cosine similarity.

The system converts text into numerical vectors (embeddings) and measures how close two sentences are in meaning.

---

## Concepts Learned

- Text Embeddings
- Vector Representation
- Cosine Similarity
- Semantic Search
- Query Matching

---

## How It Works

The system follows this pipeline:

Text  
↓  
Embedding Model  
↓  
Vector Representation  
↓  
Cosine Similarity  
↓  
Similarity Score

Higher similarity score = more related meaning.

---

## Technologies Used

- Python
- Ollama
- Numpy
- nomic-embed-text embedding model

---

## Example Sentences Tested

```
"I love learning artificial intelligence"
"I enjoy studying machine learning"
"Pizza tastes amazing"
```

The first two sentences have a high similarity score because they share similar meaning.

The third sentence is unrelated and produces a low similarity score.

---

## Query Semantic Search

The system also supports query matching.

Example query:

```
How to learn chest workout
```

Documents:

```
Machine learning tutorials
Artificial intelligence course
Best pizza recipe
Workout plan for muscle gain
```

The system calculates similarity between the query and each document and returns the most relevant result.

---

## Example Output

```
Embedding length: 768

AI similarity: 0.82
AI vs Pizza similarity: 0.21

Query Similarity Results:

Machine learning tutorials → 0.31
Artificial intelligence course → 0.28
Best pizza recipe → 0.14
Workout plan for muscle gain → 0.79

Most relevant document:
Workout plan for muscle gain
```

---

## Key Learning

Embeddings convert text into vectors that capture semantic meaning.

Cosine similarity measures how similar two vectors are.

This concept forms the foundation of modern AI systems such as:

- Semantic Search
- Recommendation Systems
- Retrieval Augmented Generation (RAG)

---

## Next Step

Day 3 will extend this system by storing embeddings inside a vector database using **ChromaDB**, allowing the system to search through large document collections.