# 🚀 RAGNova

## A Domain-Specific Retrieval-Augmented Generation System for Intelligent PDF Question Answering

> **Ask Your Documents. Get Grounded Answers.**

RAGNova is a Domain-Specific Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions about their content using natural language.

Instead of manually searching through large documents, RAGNova extracts the document content, divides it into smaller chunks, converts those chunks into embeddings, retrieves the most relevant information, and uses a Large Language Model (LLM) to generate a grounded answer.

The system provides answers based on the uploaded document context and displays the source document and page number whenever available.

---

## 📌 1. Project Objective

Large PDF documents can contain hundreds of pages, making it difficult and time-consuming to manually find specific information.

RAGNova addresses this problem by providing a conversational interface where users can:

- Upload PDF documents
- Process document content automatically
- Ask questions in natural language
- Retrieve relevant information from documents
- Generate answers using retrieved document context
- View the source document and page number

The main objective is to understand and implement the complete Retrieval-Augmented Generation workflow.

---

## 🎯 2. Key Objectives

- Understand the complete RAG workflow
- Extract and process text from PDF documents
- Preserve document and page metadata
- Split large documents into smaller chunks
- Generate numerical embeddings for document chunks
- Store embeddings using FAISS
- Retrieve relevant document chunks for user questions
- Generate answers using retrieved document context
- Reduce unsupported answers and hallucinations
- Display source document and page information
- Provide an easy-to-use Streamlit interface

---

## 🧠 3. What is RAG?

Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with Large Language Models.

Instead of directly asking an LLM to answer a question from its general knowledge, RAGNova first searches the uploaded documents for relevant information.

The retrieved information is then provided to the LLM as context for generating the answer.

### RAG Workflow

```text
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
User Question
      ↓
Question Embedding
      ↓
Relevant Chunk Retrieval
      ↓
Context + Question
      ↓
Large Language Model
      ↓
Grounded Answer
      ↓
Source Document + Page
