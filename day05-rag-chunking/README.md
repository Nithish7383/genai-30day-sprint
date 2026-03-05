# Day 5 – Document Chunking for RAG Systems

## Objective

The goal of this exercise is to improve the Retrieval Augmented Generation (RAG) pipeline by introducing **document chunking**.

Instead of storing an entire document as a single block of text, the document is split into smaller sections called **chunks**. Each chunk is embedded and stored separately in the vector database.

This allows the system to retrieve more relevant pieces of information and improves the accuracy of the generated responses.

---

## Technologies Used

* Python
* Ollama (Local LLM runtime)
* ChromaDB (Vector database)
* Llama3 (Generation model)
* Nomic Embed Text (Embedding model)

---

## System Architecture

Large Document
↓
Document Chunking
↓
Convert Each Chunk → Embedding
↓
Store Chunks in Vector Database
↓
User Question
↓
Convert Question → Embedding
↓
Vector Similarity Search
↓
Retrieve Most Relevant Chunks
↓
Inject Retrieved Context into Prompt
↓
LLM Generates Answer Based on Context

---

## What Happens Internally

The system follows these steps:

1. **Document Preparation**

   A large document containing information about artificial intelligence concepts is created.

2. **Chunking Process**

   The document is split into smaller pieces called chunks using a fixed character length.

   Example document:

   ```
   Artificial intelligence is a field of computer science focused on building intelligent machines.
   Machine learning allows computers to learn patterns from data.
   ```

   After chunking:

   ```
   Chunk 1:
   Artificial intelligence is a field of computer science focused on building intelligent machines.

   Chunk 2:
   Machine learning allows computers to learn patterns from data.
   ```

3. **Embedding Generation**

   Each chunk is converted into a numerical vector using the embedding model.

   Example:

   ```
   Machine learning allows computers to learn patterns from data
   ```

   becomes

   ```
   [0.32, -0.18, 0.91, ...]
   ```

4. **Vector Database Storage**

   The chunk embeddings are stored inside ChromaDB so they can be efficiently retrieved during similarity search.

5. **User Query Processing**

   When a user asks a question, the system converts the question into an embedding.

6. **Similarity Search**

   The vector database compares the query embedding with stored chunk embeddings and retrieves the most relevant chunks.

7. **Context Construction**

   The retrieved chunks are combined to form a context block.

8. **Answer Generation**

   The context and user question are passed to the LLM (Llama3), which generates the final response.

---

## Example Run

**Question**

What is machine learning?

**Retrieved Context**

* subset of AI that allows computers to learn patterns from data
* Artificial intelligence is a field of computer science focused on building intelligent machines

**Generated Answer**

Machine learning is a subset of artificial intelligence that allows computers to learn patterns from data.

---

## Observations

During implementation, chunking was performed using a fixed character length. This sometimes causes sentences to be split in the middle.

Example:

```
Machine learning is a
subset of AI that allows computers to learn patterns
```

Despite partial sentences, embedding models are still able to capture the semantic meaning and retrieve relevant chunks.

---

## Key Concepts Learned

* Document chunking in RAG systems
* Chunk-based embedding storage
* Vector similarity search on chunked data
* Context retrieval from relevant document sections
* Improving RAG accuracy using chunking

---

## Next Step

In **Day 6**, conversation memory will be added so the system can maintain context across multiple questions and behave like a real conversational AI assistant.
