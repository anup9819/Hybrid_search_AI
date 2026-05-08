# Hybrid Search PoC for Construction Document Retrieval

A Proof of Concept (PoC) hybrid retrieval system built in Python that combines traditional keyword-based search with semantic search using transformer embeddings.

The project demonstrates how modern retrieval systems can support both:
- exact keyword/code matching (e.g. OSHA, ASTM, regulation numbers)
- natural language intent-based search queries

This system was designed around a construction document retrieval use case involving:
- safety regulations
- technical bulletins
- material specifications
- incident reports
- procedure manuals

---

# Problem Statement

Traditional keyword search fails when users describe problems using natural language instead of exact terminology.

Example:

A user may search:

```text
what do we do if pouring concrete when it's freezing outside?
```

Even if the document contains:

```text
Cold Weather Concreting
```

A semantic retrieval system should still understand the intent and return the correct document.

At the same time, the system must still support precise lookups for regulation codes like:

```text
OSHA 1926.501
ASTM C150
```

This project solves both problems using a hybrid retrieval architecture.

---

# Features

- JSON document ingestion
- TF-IDF based keyword search
- Semantic search using Sentence Transformers
- Cosine similarity ranking
- Hybrid retrieval pipeline
- Reciprocal Rank Fusion (RRF)
- Structured search results
- Clean console formatting
- Modular and extensible architecture

---

# Tech Stack

- Python
- scikit-learn
- sentence-transformers
- numpy

---

# Retrieval Architecture

```text
                    User Query
                         │
         ┌───────────────┼────────────────┐
         │                                │
         ▼                                ▼

  Keyword Search                  Semantic Search
      (TF-IDF)                     (Embeddings)

         │                                │
         ▼                                ▼

  Lexical Rankings                Semantic Rankings

                 └────────┬────────┘
                          ▼

              Reciprocal Rank Fusion
                         (RRF)

                          ▼

                Final Hybrid Results
```

---

# How It Works

## 1. Keyword Search

Uses TF-IDF vectorization and cosine similarity to:
- prioritize exact term matches
- support acronym/code retrieval
- rank documents lexically

Best for:
- OSHA codes
- ASTM references
- exact terminology

---

## 2. Semantic Search

Uses transformer embeddings via:

```python
all-MiniLM-L6-v2
```

to:
- understand semantic meaning
- support natural language queries
- retrieve contextually similar documents

Best for:
- intent-based search
- descriptive queries
- paraphrased language

---

## 3. Hybrid Search

Combines:
- lexical rankings
- semantic rankings

using:

## Reciprocal Rank Fusion (RRF)

Formula:

```text
RRF(d) = Σ 1 / (k + rank(d))
```

This approach:
- avoids averaging incompatible score scales
- rewards documents ranked highly across multiple systems
- produces more stable retrieval quality

---

# Example Queries

## Keyword-heavy Query

```text
specs for ASTM C150 cement
```

Expected Top Result:
- Material specification document

---

## Semantic Query

```text
what do we do if pouring concrete when it's freezing outside?
```

Expected Top Result:
- Cold Weather Concreting procedure manual

---

# Project Structure

```text
hybrid_search_poc/
│
├── documents.json
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/anup9819/Hybrid_search_AI.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Concepts Explored

This project explores important Information Retrieval (IR) concepts including:

- lexical retrieval
- semantic retrieval
- vectorization
- cosine similarity
- transformer embeddings
- sparse vs dense vectors
- ranking systems
- hybrid search pipelines
- retrieval fusion techniques

---

# Future Improvements

Potential enhancements:

- acronym/code boosting
- query intent detection
- weighted hybrid fusion
- snippet highlighting
- explainable ranking
- stop-word filtering
- vector database integration
- API deployment

---

# Status

Completed:
- Keyword Search 
- Semantic Search 
- Hybrid Search 
- Reciprocal Rank Fusion 
- Console Formatting 
---

# Author

Anup Das
