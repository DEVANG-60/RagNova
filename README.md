# 🚀 RAGNova

## A Domain-Specific Retrieval-Augmented Generation System for Intelligent PDF Question Answering

> **Ask Your Documents. Get Grounded Answers.**

RAGNova is a Domain-Specific Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions about their content using natural language.

Instead of manually searching through large documents, RAGNova extracts the document content, divides it into smaller chunks, converts those chunks into embeddings, retrieves the most relevant information, and uses a Large Language Model (LLM) to generate a grounded answer.

The system is designed to answer questions **only using information retrieved from the uploaded documents** and provides the corresponding document name and page number whenever available.

---

# 📌 1. Project Objective

Large PDF documents can contain hundreds of pages, making it difficult and time-consuming to manually find specific information.

RAGNova addresses this problem by providing a conversational interface where users can:

- Upload PDF documents
- Process their content automatically
- Ask questions in natural language
- Retrieve relevant information from the documents
- Generate answers based on the retrieved content
- View the source document and page number

The main objective is to understand and implement the complete **Retrieval-Augmented Generation workflow**.

---

# 🎯 2. Key Objectives

The project focuses on the following objectives:

- Understand the complete RAG workflow.
- Extract and process text from PDF documents.
- Preserve document and page metadata.
- Split large documents into smaller meaningful chunks.
- Generate numerical embeddings for document chunks.
- Store embeddings using FAISS.
- Retrieve relevant document chunks for user questions.
- Generate answers using retrieved document context.
- Prevent unsupported answers and hallucination as far as possible.
- Display source document and page information.
- Provide an easy-to-use Streamlit interface.

---

# 🧠 3. What is RAG?

**Retrieval-Augmented Generation (RAG)** is an approach that combines information retrieval with Large Language Models.

Instead of directly asking an LLM to answer a question from its general knowledge, RAGNova first searches the uploaded documents for relevant information.

The retrieved information is then provided to the LLM as context.

### Basic RAG flow

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




🔍 4. Problem Statement

Large documents are difficult to search manually.

A user may need to read many pages to find one specific answer. Traditional keyword-based searching may also fail when the question and document use different wording.

RAGNova solves this problem by allowing users to upload documents and ask questions about their content using natural language.

The system retrieves semantically relevant passages before generating an answer.

💡 5. Proposed Solution

RAGNova follows a multi-stage Retrieval-Augmented Generation pipeline.

Workflow
User uploads one or more PDF files.
Text is extracted from every readable page.
Document text is divided into smaller overlapping chunks.
Each chunk is converted into a numerical embedding.
Embeddings are stored in a FAISS vector index.
The user's question is converted into an embedding.
FAISS searches for the most relevant document chunks.
The retrieved chunks are provided to the LLM as context.
The LLM generates an answer using the supplied context.
The application displays the answer along with document and page information.
⚙️ 6. Technology Stack
Component	Technology
Programming Language	Python
PDF Processing	pypdf
Text Splitting	LangChain Text Splitters
Embeddings	Sentence Transformers
Embedding Model	all-MiniLM-L6-v2
Vector Database	FAISS
Language Model API	Groq
Language Model	openai/gpt-oss-20b
RAG Components	LangChain
User Interface	Streamlit
Environment Variables	python-dotenv
Version Control	Git & GitHub
🏗️ 7. System Architecture
                  ┌──────────────────────┐
                  │     PDF Documents    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Text Extraction   │
                  │        pypdf         │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    Text Chunking     │
                  │  LangChain Splitter  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │      Embeddings      │
                  │ Sentence Transformers│
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    FAISS Vector      │
                  │       Store          │
                  └──────────┬───────────┘
                             │
                      User Question
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Query Embedding    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Relevant Chunk       │
                  │ Retrieval            │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  Context + Question  │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │      Groq LLM        │
                  │   GPT-OSS-20B        │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Grounded Answer +    │
                  │ Source & Page        │
                  └──────────────────────┘
📂 8. Project Structure
RAGNova/
│
├── app.py
├── rag_pipeline.py
├── document_loader.py
├── vector_store.py
├── prompt.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── documents/
│   └── sample.pdf
│
├── vector_store/
│   └── saved_index/
│
└── tests/
    └── test_questions.csv
File Description
File	Purpose
app.py	Streamlit user interface
rag_pipeline.py	Main RAG processing pipeline
document_loader.py	PDF text extraction
vector_store.py	Embedding generation and FAISS search
prompt.py	Grounded-answer prompt
requirements.txt	Python dependencies
.env	API key configuration
.gitignore	Prevents sensitive/unnecessary files from Git
README.md	Project documentation
🧩 9. Main Project Modules
Module 1 — Document Upload

The Streamlit interface allows users to upload one or multiple PDF files.

Features
PDF file upload
Multiple PDF support
Display uploaded filenames
Process Documents button
Clear Chat functionality
Module 2 — Text Extraction

RAGNova uses pypdf to read the uploaded PDF files.

For every readable page, the system stores:

Extracted text
Page number
Source document name

Empty pages are skipped safely.

Example Metadata
Source: sample.pdf
Page: 4
Text: Extracted content from page 4...
Module 3 — Text Chunking

Large PDF text is divided into smaller sections using:

RecursiveCharacterTextSplitter
Current Settings
Chunk Size: 800 characters
Chunk Overlap: 120 characters

The overlap helps preserve connected information between neighboring chunks.

Module 4 — Embeddings and Vector Store

Each document chunk is converted into a numerical representation called an embedding.

RAGNova uses:

all-MiniLM-L6-v2

The generated embeddings are stored and searched using:

FAISS

FAISS allows the system to perform similarity-based retrieval of relevant document chunks.

Module 5 — Retrieval

When the user asks a question:

The question is converted into an embedding.
FAISS searches the vector index.
The most relevant chunks are retrieved.
Source document and page metadata are preserved.

RAGNova retrieves up to 5 relevant chunks for each question.

Module 6 — Answer Generation

The retrieved chunks are combined into a context.

The question and retrieved context are then sent to the Groq-hosted language model.

The prompt instructs the model to:

Answer only from the supplied context
Avoid inventing facts
Mention source information when available
Return a fallback response when the information cannot be found
Fallback Response
I could not find this information in the uploaded documents.

This ensures that the chatbot has a defined response when the required information is not available in the retrieved document context.

Module 7 — Streamlit Interface

The application provides:

PDF uploader
Uploaded file display
Process Documents button
Chat interface
Chat history
Source information
Page numbers
Clear Chat button
Processing status
🖥️ 10. Application Workflow
Step 1 — Upload

Upload one or more PDF documents using the sidebar.

Step 2 — Process

Click:

⚡ Process Documents

RAGNova extracts, chunks, embeds, and indexes the document content.

Step 3 — Ask

After processing is complete, the chat interface becomes available.

Example:

What is the main objective of this document?
Step 4 — Retrieve

The system searches FAISS for the most relevant document chunks.

Step 5 — Generate

The retrieved context is passed to the language model.

Step 6 — Display

The application displays:

Generated answer
Source document
Page number
🛠️ 11. Installation
Prerequisites

Make sure the following are installed:

Python 3.10 or later
pip
Git
Groq API key
Clone the Repository
git clone https://github.com/DEVANG-60/RAGNova.git

Move into the project directory:

cd RAGNova
Create a Virtual Environment

For Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
🔐 12. API Key Configuration

Create a file named:

.env

Add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

Replace:

your_groq_api_key_here

with your actual API key.

Security Warning

Never upload your .env file or API key to GitHub.

The .gitignore file should contain:

.env
__pycache__/
*.pyc
.streamlit/
vector_store/
▶️ 13. Running the Application

After installing dependencies and configuring the API key, run:

streamlit run app.py

The application will open in your browser.

Usually:

http://localhost:8501
📚 14. Example Usage
Example Question
What is the main objective of the document?
Example Answer
The main objective is to provide information about...
Source
📄 sample.pdf | 📖 Page 3

If the requested information is not available:

I could not find this information in the uploaded documents.
🧪 15. Testing and Evaluation

RAGNova should be tested using different types of questions.

The evaluation focuses on:

1. Retrieval Accuracy

Did the system retrieve the correct document and page?

2. Answer Correctness

Is the generated answer supported by the retrieved context?

3. Groundedness

Does the answer avoid unsupported information?

4. Refusal Quality

Does the chatbot correctly respond when the answer is absent from the documents?

5. Source Quality

Does the system provide useful document and page references?

6. Response Time

Does the chatbot respond within a reasonable amount of time?

📋 16. Testing Sheet

The final project testing sheet should contain at least 15 questions.

Suggested format:

No.	Question	Expected Source	Retrieved Source	Correct?
1	What is the main objective?	sample.pdf, Page X		
2	What are the key features?	sample.pdf, Page X		
3	What is the definition of...?	sample.pdf, Page X		
4	What process is described?	sample.pdf, Page X		
5	What are the advantages?	sample.pdf, Page X		
6	What are the limitations?	sample.pdf, Page X		
7	Who is mentioned in the document?	sample.pdf, Page X		
8	What is the purpose of...?	sample.pdf, Page X		
9	What steps are described?	sample.pdf, Page X		
10	What conclusion is given?	sample.pdf, Page X		
11	Question using different wording	sample.pdf, Page X		
12	Question requiring retrieval	sample.pdf, Page X		
13	Question about another section	sample.pdf, Page X		
14	Unavailable question	Not available		
15	Unrelated question	Not available		
🛡️ 17. Responsible AI and Security

RAGNova follows basic responsible-AI and security practices.

API Key Protection

API keys are stored in .env and should not be exposed in source code or GitHub.

Document Privacy

Users should not upload confidential documents without appropriate permission.

Answer Verification

Generated answers should not automatically be assumed to be correct.

Important or high-stakes information should be independently verified.

Document Instructions

Instructions contained inside uploaded documents should not override the chatbot's intended behavior.

File Restrictions

The application accepts PDF documents as the supported document format.

🚧 18. Current Limitations

The current version has some limitations:

Scanned PDFs requiring OCR are not currently processed.
Retrieval depends on the quality of extracted PDF text.
Answers depend on the quality of retrieved chunks.
The vector store is created during document processing.
Very large document collections may require optimization.
Generated answers should still be verified for important information.
The current interface is designed primarily for document-based question answering.
🔮 19. Future Enhancements

Future versions of RAGNova can include:

Multiple document collections
Document filtering
Persistent vector stores
Conversation memory
OCR support for scanned PDFs
FastAPI backend
User authentication
Document access control
Answer feedback buttons
Docker deployment
Prepared question-answer evaluation datasets
Improved retrieval strategies
Advanced document management
📈 20. Advantages

RAGNova provides:

Natural-language document search
Faster information retrieval
Semantic similarity-based retrieval
Source-aware answers
Page-level references
Multiple PDF support
Reduced need for manual document searching
Conversational interaction
Context-based answer generation
A simple and accessible user interface
🎓 21. Learning Outcomes

Through this project, the following concepts are demonstrated:

Python application development
PDF text extraction
Text preprocessing
Text chunking
Embeddings
Semantic similarity
Vector databases
FAISS
Retrieval-Augmented Generation
Prompt engineering
LLM integration
Streamlit development
Git and GitHub
Testing and evaluation
Responsible AI practices
❓ 22. Viva Questions
1. What is RAG?

RAG stands for Retrieval-Augmented Generation. It retrieves relevant information from a knowledge source and provides that information as context to an LLM before generating an answer.

2. Why do we split documents into chunks?

Large documents are divided into smaller chunks so that relevant sections can be retrieved more effectively.

3. What is an embedding?

An embedding is a numerical representation of text that captures semantic information and allows similar pieces of text to be compared.

4. What does FAISS do?

FAISS provides efficient similarity search over the vector representations of document chunks.

5. How does similarity help retrieval?

The user's question is converted into an embedding and compared with stored document embeddings. The closest vectors represent potentially relevant document content.

6. Why can a RAG chatbot still produce an incorrect answer?

Incorrect answers can result from poor text extraction, inappropriate chunking, incorrect retrieval, insufficient context, or errors during LLM generation.

7. How do you test retrieval?

Retrieval can be tested by checking whether the expected document and page are returned for a set of known questions.

8. What happens when the answer is not present?

RAGNova uses a fallback response:

I could not find this information in the uploaded documents.
📦 23. Final Deliverables

The project deliverables include:

 Working Streamlit application
 Complete source code
 Sample PDF documents
 requirements.txt
 README with setup and usage instructions
 Architecture/workflow diagram
 Testing sheet with at least 15 questions
 GitHub repository
 Short project report
 Demonstration video
👨‍💻 24. Project Information

Project Name: RAGNova

Full Project Title:

RAGNova: A Domain-Specific Retrieval-Augmented Generation System for Intelligent PDF Question Answering

Project Type: Student Major Project

Domain:

Artificial Intelligence | Generative AI | Natural Language Processing

Programming Language: Python

Framework: Streamlit

Vector Store: FAISS

Embedding Model: all-MiniLM-L6-v2

LLM Provider: Groq

LLM: openai/gpt-oss-20b

Repository:

https://github.com/DEVANG-60/RAGNova

📄 25. Requirements

The main Python packages used by the project are:

streamlit
pypdf
langchain
langchain-text-splitters
sentence-transformers
faiss-cpu
python-dotenv
groq

They are available in:

requirements.txt

Install them using:

pip install -r requirements.txt
🔄 26. Complete RAG Pipeline

The complete implementation can be summarized as:

                USER
                  │
                  ▼
          Upload PDF Document
                  │
                  ▼
          Extract Page Text
                  │
                  ▼
           Split Into Chunks
                  │
                  ▼
       Generate Text Embeddings
                  │
                  ▼
          Store in FAISS
                  │
                  │
                  │
          User Asks Question
                  │
                  ▼
        Generate Query Embedding
                  │
                  ▼
        Search FAISS Vector Store
                  │
                  ▼
        Retrieve Top 5 Chunks
                  │
                  ▼
       Build Context + Question
                  │
                  ▼
          Send to Groq LLM
                  │
                  ▼
          Generate Grounded
               Answer
                  │
                  ▼
       Display Answer + Sources
🌟 27. Why RAGNova?

Traditional document searching requires users to manually scan through large amounts of content.

RAGNova provides an interactive alternative by connecting:

Documents
    +
Semantic Retrieval
    +
Large Language Models
    =
Interactive Document Question Answering

The system demonstrates how RAG can turn static PDF documents into an interactive knowledge source.

🚀 28. Getting Started Quickly

For a quick setup:

git clone https://github.com/DEVANG-60/RAGNova.git

cd RAGNova

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

Create .env:

GROQ_API_KEY=your_groq_api_key_here

Then run:

streamlit run app.py

Open:

http://localhost:8501

Upload a PDF, click Process Documents, and start asking questions.

📜 29. License

This project is developed for educational and academic purposes.

⭐ RAGNova
Ask Your Documents. Get Grounded Answers.

RAGNova — Domain-Specific Retrieval-Augmented Generation for Intelligent PDF Question Answering.


This version is the **single complete README**, rather than separate pieces. It follows the structure and requirements from your project PDF, including the required modules, workflow, minimum features, testing criteria, project structure, guardrail, and deliverables. :contentReference[oaicite:0]{index=0}
