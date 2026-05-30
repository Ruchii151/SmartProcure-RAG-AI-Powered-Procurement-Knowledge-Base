# SmartProcure-RAG: AI-Powered Procurement Knowledge Base

An intelligent Retrieval-Augmented Generation (RAG) system designed to simplify procurement document analysis and supplier information retrieval. The application enables procurement professionals to query supplier documents using natural language and receive accurate, context-aware responses grounded in organizational procurement data.

## Problem Statement

Procurement teams often manage large volumes of supplier contracts, pricing sheets, certifications, and procurement records stored across multiple documents. Manually searching through these files to find relevant information is time-consuming, inefficient, and prone to errors.

There is a need for an intelligent system that can quickly retrieve supplier-related information and provide concise answers based on organizational procurement documents.

## Solution Overview

This project introduces an AI-powered Procurement Knowledge Assistant that leverages Retrieval-Augmented Generation (RAG) to process supplier PDFs and Excel documents and generate accurate responses to procurement-related queries.

By combining semantic search, vector databases, and Large Language Models (LLMs), the system delivers reliable, document-grounded insights on suppliers, contracts, pricing, payment terms, certifications, lead times, and procurement risks.

## System Architecture

User Query

↓

Procurement Documents (PDFs & Excel Files)

↓

Document Loading & Processing

↓

Text Chunking

↓

Embedding Generation

↓

Vector Database (ChromaDB)

↓

Retriever (Top-K Similar Chunks)

↓

LLM (Gemini 2.5 Flash)

↓

Context-Aware Procurement Insights

## Core Features

* Multi-document procurement question answering
* Support for PDF and Excel procurement documents
* Semantic search using vector embeddings
* Context-aware answer generation using Gemini
* Supplier information retrieval
* Pricing and payment terms analysis
* Contract and certification lookup
* Procurement risk identification
* Source document transparency
* Real-time Streamlit interface

## Technology Stack

**Framework:** LangChain

**Vector Database:** ChromaDB

**Embeddings:** Ollama (nomic-embed-text)

**LLM:** Google Gemini (gemini-2.5-flash)

**Frontend:** Streamlit

**Data Processing:** Pandas, OpenPyXL

**Document Loaders:** PyPDFLoader

**Language:** Python

**Concepts:** NLP, Semantic Search, Retrieval-Augmented Generation (RAG)

## Workflow Explanation

### 1. Data Ingestion

The system loads procurement-related PDF documents and Excel spreadsheets containing supplier information, contracts, pricing details, certifications, and procurement records.

### 2. Document Processing

Documents are cleaned and converted into a standardized format. Excel sheets are transformed into structured text representations while preserving metadata such as file names, sheet names, and row information.

### 3. Text Chunking

The processed content is divided into smaller chunks using a Recursive Character Text Splitter to improve retrieval accuracy.

### 4. Embedding Generation

Each chunk is converted into dense vector representations using Ollama's nomic-embed-text embedding model.

### 5. Vector Storage

The generated embeddings are stored in ChromaDB for efficient semantic similarity search.

### 6. Retrieval

When a user submits a query, the retriever identifies the most relevant document chunks based on vector similarity.

### 7. Response Generation

The retrieved context is provided to Gemini 2.5 Flash using a procurement-focused prompt that generates accurate, document-grounded answers.

### 8. Source Transparency

The system displays the source documents used to generate the response, enabling users to verify information and maintain trust in the outputs.

## Example Questions
- Which suppliers have ISO certification?
- What are the payment terms of ABC Ltd?
- Which supplier has the highest rating?
- Compare ABC Ltd and XYZ Corp.
- Which supplier has the shortest lead time?
- Are there any risk clauses in Supplier A's contract?
- What penalties exist for delayed delivery?

## Example Use Cases

* What are the payment terms offered by Supplier A?
* Which suppliers hold ISO certifications?
* What is the lead time for raw material procurement?
* Are there any supplier contract renewal clauses?
* Which supplier offers the lowest pricing?
* What procurement risks are identified in supplier agreements?
* What certifications are available for a specific supplier?
* Compare pricing information across suppliers.

## Impact

This system significantly reduces the time spent searching procurement documents by enabling instant retrieval of supplier information through natural language queries. It improves procurement efficiency, enhances knowledge accessibility, and supports faster decision-making.

## Future Enhancements

* Supplier performance analytics dashboard
* OCR support for scanned procurement documents
* Multi-format document support (Word, CSV, PPT)
* Hybrid search (keyword + semantic search)
* Supplier comparison and ranking module
* Automated contract clause extraction
* Procurement trend analysis and reporting
* Cloud deployment for enterprise scalability

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/smartprocure-rag.git
cd smartprocure-rag
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```env
GOOGLE_API_KEY=your_google_api_key
```

### 4. Run Application

```bash
streamlit run app.py
```

## Conclusion

SmartProcure-RAG demonstrates the practical application of Retrieval-Augmented Generation in procurement and supply chain operations. By combining semantic search, vector databases, and Large Language Models, the system enables efficient retrieval of supplier knowledge and transforms unstructured procurement documents into actionable business insights.
