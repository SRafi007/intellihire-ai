from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    # Qdrant settings
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))

    # Embeddings
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")

    # Ollama model for reasoning
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral:7b-instruct-q4")

    # Collection name for CV storage
    CV_COLLECTION: str = os.getenv("CV_COLLECTION", "intellihire_cvs")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
