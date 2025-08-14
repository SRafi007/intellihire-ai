 
# IntelliHire AI

IntelliHire AI is an **AI-powered CV evaluation & ranking system** that understands a job description (JD) and evaluates multiple CVs against that JD — producing ranked lists and per-CV ratings.  
Built for local use with **Mistral 7B (Ollama)** for reasoning, **LangChain** for orchestration, and **Qdrant** for vector storage.

**Key Features:**
- Parse CVs (PDF/DOCX/TXT) & Job Descriptions (free-form text).
- Embed CVs & JDs, then retrieve and compare semantically via RAG.
- Batch-rank CVs for a JD and produce explainable scores.
- Rate a single CV against a JD (ad-hoc rating).
- Streamlit-ready UI integration (no chatbot).

> Local-first: runs on your laptop/device with Ollama + Qdrant — no cloud APIs required.


```

```
intellihire-ai/
│
├── app/                            # Main application logic
│   ├── ingestion/                  # CV & JD ingestion and parsing (no UI)
│   │   ├── parse_cv.py             # parse PDF/DOCX/TXT -> raw text + metadata
│   │   ├── parse_jd.py             # normalize free-form JD text -> canonical JD object
│   │   └── ocr_utils.py            # tesseract wrapper + image helpers
│   │
│   ├── pipelines/                  # High-level pipelines (batch & single-run)
│   │   ├── ingest_pipeline.py      # text -> chunk -> embed -> upsert
│   │   ├── batch_ranker.py         # given jd_id and CVs -> produce ranked results
│   │   └── cv_rater.py             # rate a single CV against an active JD
│   │
│   ├── embeddings/                 # Embedding generation & model config
│   │   ├── embedder.py             # async embedding interface (pluggable)
│   │   └── model_config.py         # embedding dim, model name constants
│   │
│   ├── storage/                    # Qdrant vector DB interactions + schema
│   │   ├── qdrant_client.py        # async wrapper around Qdrant (init, upsert, search)
│   │   ├── schema.py               # <-- authoritative schema (app/storage/schema.py)
│   │   └── upsert.py               # convenience upsert helpers
│   │
│   ├── scoring/                    # Scoring engine (Ollama + aggregator)
│   │   ├── scorer.py               # call Ollama to get sub-scores & summaries
│   │   ├── aggregator.py           # combine sub-scores into final rank (weights)
│   │   └── prompts.py              # canonical prompts for rating/scoring (versioned)
│   │
│   ├── retrieval/                  # RAG retrieval helpers around Qdrant
│   │   ├── retriever.py            # typed retrieve functions for CV/JD collections
│   │   └── filters.py              # common HR filters (skills, location, years)
│   │
│   ├── ui/                         # Streamlit or minimal demo UI (optional)
│   │   ├── streamlit_app.py        # Streamlit integration (upload JD & CVs -> rank)
│   │   └── components/             # small UI components (file list, result card)
│   │
│   └── config/                     # Config + settings (Pydantic BaseSettings)
│       ├── settings.py             # env-driven settings (Qdrant host/ports, dims, names)
│       └── constants.py
│
├── data/                           # Example CVs, JDs, and demo results
│   ├── samples/cvs/
│   ├── samples/jds/
│   └── sample_results/
│
├── scripts/                        # CLI convenience scripts (single-command)
│   ├── init_qdrant.py              # create collections
│   ├── ingest_jd.py                # ingest single JD (text/file) -> returns jd_id
│   ├── ingest_cvs.py               # ingest folder of CVs -> returns list of cv_ids
│   ├── run_batch_ranking.py        # run ranking for jd_id against stored cv_ids
│   ├── rate_cv.py                  # rate a single CV against a JD (ad-hoc)
│   └── run_demo.py                 # quick demo: ingest JD -> ingest CVs -> rank -> write results
│
├── tests/                          # Unit & integration tests
│   ├── test_ingest.py
│   ├── test_embeddings.py
│   ├── test_ranking.py
│   └── test_end_to_end.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   └── PROMPTS.md
│
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── LICENSE


```