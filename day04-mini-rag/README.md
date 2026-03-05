# Day 4 – Mini Retrieval Augmented Generation (RAG)

## Objective

The goal of this exercise is to build a simple **Retrieval Augmented Generation (RAG)** system using a local Large Language Model.

Instead of generating answers directly from the model’s internal knowledge, the system first retrieves relevant information from a document store and then uses that information as context for the model.

This improves answer accuracy and reduces hallucinations.

---

## Technologies Used

* Python
* Ollama (Local LLM runtime)
* ChromaDB (Vector database)
* Llama3 (Generation model)
* Nomic Embed Text (Embedding model)

---

## System Architecture

User Question
↓
Convert Question → Embedding
↓
Vector Database Search
↓
Retrieve Most Relevant Documents
↓
Inject Retrieved Context into Prompt
↓
LLM Generates Answer Based on Context

---

## What Happens Internally

The system follows these steps:

1. **Document Storage**

   A small knowledge base is created containing several documents related to artificial intelligence.

2. **Embedding Generation**

   Each document is converted into a numerical vector using the embedding model.

   Example:

   Text

   ```
   Machine learning allows computers to learn from data
   ```

   becomes

   ```
   [0.21, -0.44, 0.87, ...]
   ```

3. **Vector Database Storage**

   The document embeddings are stored inside ChromaDB, which enables fast similarity search.

4. **User Query Processing**

   When a user asks a question, the system converts the question into an embedding.

5. **Similarity Search**

   The vector database compares the query embedding with stored document embeddings and returns the most relevant documents.

6. **Context Construction**

   The retrieved documents are combined into a context block.

7. **Prompt Injection**

   The context and the user question are inserted into a prompt.

8. **Answer Generation**

   The prompt is sent to the LLM (Llama3), which generates a response using the retrieved context.

---

## Example Run

**Question**

How can we understand complex patterns?

**Retrieved Context**

* Deep learning uses neural networks to model complex patterns
* Machine learning is a subset of artificial intelligence where systems learn patterns from data

**Generated Answer**

Deep learning helps us understand complex patterns by using neural networks to model relationships in data.

---

## Key Concepts Learned

* Retrieval Augmented Generation (RAG)
* Vector similarity search
* Context injection into prompts
* Combining embeddings with LLM responses
* Building local AI systems using Ollama

---

## Next Step

In Day 5 we will improve this system by introducing **document chunking**.
Chunking splits large documents into smaller sections so that retrieval becomes more accurate and efficient.
