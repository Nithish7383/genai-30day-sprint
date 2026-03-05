# Day 3 – Vector Database & Semantic Search

## Objective

The goal of this exercise is to implement a simple semantic search system using text embeddings and a vector database.

This forms the foundation of modern Retrieval-Augmented Generation (RAG) systems used in many AI applications.

---

## Technologies Used

- Python
- Ollama
- ChromaDB
- Nomic Embed Text Model

---

## System Architecture

Documents
↓
Embedding Model (Ollama)
↓
Vector Database (ChromaDB)
↓
User Query → Embedding
↓
Similarity Search
↓
Top Relevant Documents

---

## Implementation Steps

1. Create a vector database using ChromaDB.
2. Store a collection of documents.
3. Convert each document into an embedding using the `nomic-embed-text` model.
4. Store the embeddings inside the vector database.
5. Convert the user query into an embedding.
6. Perform a similarity search to retrieve the most relevant documents.

---

## Example Query

Query:

How do machines learn?

Results:

Machine learning allows computers to learn patterns from data  
Artificial intelligence is transforming industries

---

## Key Learning Points

- Embeddings convert text into numerical vectors.
- Vector databases store embeddings efficiently.
- Semantic search retrieves documents based on meaning rather than exact keyword matches.
- This technique is the foundation of Retrieval-Augmented Generation (RAG) systems.

---

## Next Step

Day 4 will extend this system by integrating a Large Language Model to generate responses using retrieved documents.

This will form the first version of a RAG pipeline.