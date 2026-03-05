# Day 6 – Adding Conversation Memory to RAG

## Objective

The goal of this exercise is to enhance the Retrieval Augmented Generation (RAG) system by introducing **conversation memory**.

Instead of answering each question independently, the system now remembers previous interactions and uses them to provide contextual responses.

This allows the AI assistant to handle **multi-turn conversations**.

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
Retrieve Relevant Documents
↓
Conversation Memory
↓
Inject Context + Memory into Prompt
↓
LLM Generates Contextual Answer

---

## What Happens Internally

1. **Document Storage**

   A small knowledge base containing AI-related documents is stored in the vector database.

2. **Embedding Generation**

   Each document is converted into numerical vectors using the embedding model.

3. **User Query Processing**

   When the user asks a question, the system converts the query into an embedding.

4. **Similarity Search**

   The vector database retrieves the most relevant documents based on vector similarity.

5. **Conversation Memory**

   Previous user messages and AI responses are stored in a conversation history list.

6. **Prompt Construction**

   The retrieved context and conversation history are included in the prompt sent to the LLM.

7. **Answer Generation**

   The LLM generates a response using both the retrieved context and conversation history.

---

## Prompt Enhancement

Initially, the prompt was simple:

```
Use the context and conversation history to answer the question.
```

This sometimes produced responses such as:

```
AI: A new question!
```

or unnecessary explanations.

To improve response quality and prevent hallucination, the prompt was enhanced with **structured rules**.

Improved prompt:

```
You are an AI assistant.

Use the provided context and conversation history to answer the question.

Rules:
1. Prefer information from the context.
2. Use conversation history if the question refers to previous messages.
3. If the answer is not in the context, respond with:
   "I could not find the answer in the provided documents."
4. Keep the answer clear and concise.
```

This ensures the model behaves like a **controlled assistant rather than a creative chatbot**.

---

## Example Test Run

User:

What is football?

AI:

I could not find the answer to the question "what is football" in the provided context or conversation history.

This demonstrates **hallucination prevention**, since the knowledge base does not contain information about football.

---

User:

Then explain about AI

AI:

Artificial intelligence (AI) is a field of computer science that enables machines to perform tasks that normally require human intelligence.

This shows that the assistant correctly retrieves relevant information from the document context.

---

## Key Concepts Learned

* Conversation memory for multi-turn interactions
* Combining RAG retrieval with conversational context
* Prompt engineering for response control
* Preventing hallucinations in AI assistants

---

## Next Step

In **Day 7**, the project will be refactored into a **modular architecture** by separating components such as embeddings, retrieval, memory management, and response generation into individual modules.
