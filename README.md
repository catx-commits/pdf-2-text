<<<<<<< HEAD
# PDF-2-TXT & RAG Data Ingestion Pipeline

A lightweight Python utility designed to extract text from PDF documents and prepare high-density, structured knowledge base files for Retrieval-Augmented Generation (RAG) pipelines.

## Project Context
Part of a modular RAG pipeline for personal knowledge bases (Dr. Yvonne Foerster & Will Munda), focused on precise source attribution and automated data processing.

## Tech Stack
- **Python 3.x**
- **PyPDF** (PDF text extraction)
- **OpenAI / OpenRouter API** (Structured text reassembly via GPT-4o-mini)
- **ChromaDB & LangChain** (Downstream RAG integration)

## Usage

1. **Extract text from PDFs:**
   ```bash
   python pdf-2-text.py --INPUT "source/*.pdf" --OUTPUT pdf_text
=======
# pdf-2-text
>>>>>>> 8496bb493a5d9a4f91b766c133e6290c9085e9e1
