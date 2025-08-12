 
# IntelliHire AI

IntelliHire AI is an **AI-powered recruitment assistant** that understands, evaluates, and ranks CVs for specific job roles.  
Built with **Mistral 7B (Ollama)** for local reasoning, **LangChain** for orchestration, and **Qdrant** for long-term vector storage.  

**Key Features:**
- Parse and embed CVs & job descriptions.
- Retrieve relevant candidates using RAG.
- Score, summarize, and recommend top candidates.
- Natural language search for recruiters.

> Works entirely on your local machine — no cloud API needed.

```
CV Upload (PDF/DOCX/Image) → Parsing (OCR if needed)
    ↓
Text Normalization → Embedding (nomic-embed-text)
    ↓
Store in Qdrant (LTM)
    ↓
Recruiter Uploads JD or Enters Requirements
    ↓
JD Embedding → Retrieve Top Matching CVs from Qdrant
    ↓
Send Retrieved CVs + JD Context to Ollama LLM via LangChain
    ↓
Reasoning + Scoring + Summary + Recommendations
    ↓
Return Results to UI
```

```
intellihire-ai/
│
├── app/                           # Main application logic
│   ├── ingestion/                  # CV & JD ingestion and parsing
│   │   ├── parse_cv.py
│   │   ├── parse_jd.py
│   │   └── ocr_utils.py
│   │
│   ├── embeddings/                 # Embedding generation logic
│   │   ├── embedder.py
│   │   └── model_config.py
│   │
│   ├── storage/                     # Qdrant vector DB interactions
│   │   ├── qdrant_client.py
│   │   ├── schema.py
│   │   └── upsert.py
│   │
│   ├── retrieval/                   # RAG retrieval logic
│   │   ├── retriever.py
│   │   └── filters.py
│   │
│   ├── reasoning/                   # Ollama + LangChain reasoning
│   │   ├── scorer.py
│   │   ├── summarizer.py
│   │   └── prompts.py
│   │
│   ├── ui/                          # Optional front-end (Streamlit/Next.js)
│   │   ├── app.py
│   │   └── components/
│   │
│   └── config/                      # Configuration files
│       ├── settings.py
│       └── constants.py
│
├── data/                            # Example CVs, JDs, and test data
│   ├── cvs/
│   ├── jds/
│   └── sample_results/
│
├── tests/                           # Unit & integration tests
│   ├── test_embeddings.py
│   ├── test_retrieval.py
│   ├── test_reasoning.py
│   └── test_end_to_end.py
│
├── scripts/                         # Utility scripts
│   ├── init_qdrant.py
│   ├── run_ingestion.py
│   ├── run_retrieval.py
│   └── run_demo.py
│
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── LICENSE

```