# ==============================================
# IntelliHire - Core: config/settings.py, app/logger.py, app/errors.py
# Save the three modules separately in your project as described below.
# - config/settings.py
# - app/logger.py
# - app/errors.py
#
# This single file is a convenience bundle for the editor. Copy each section
# into the corresponding file path in your repository.
# ==============================================

# -----------------------------
# FILE: config/settings.py
# -----------------------------
from __future__ import annotations
from typing import Optional
from pydantic import BaseSettings, Field, AnyHttpUrl, validator
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables (or .env).

    Use `settings = Settings()` to load with defaults overridden by the env.
    """

    # Qdrant
    QDRANT_HOST: str = Field("localhost", description="Qdrant host")
    QDRANT_PORT: int = Field(6333, description="Qdrant port")
    QDRANT_API_KEY: Optional[str] = Field(None, description="Qdrant API key (if any)")
    QDRANT_COLLECTION: str = Field(
        "intellihire", description="Default Qdrant collection name"
    )

    # Ollama / Local LLM
    OLLAMA_URL: Optional[AnyHttpUrl] = Field(
        None, description="Base URL for Ollama server, e.g. http://localhost:11434"
    )
    OLLAMA_MODEL: str = Field("mistral-7b", description="Local model name in Ollama")
    OLLAMA_TIMEOUT: int = Field(30, description="Timeout seconds for Ollama requests")

    # Embeddings
    EMBEDDING_MODEL: str = Field(
        "local-embedding-model", description="Embedding model identifier"
    )
    EMBEDDING_DIM: int = Field(
        1536, description="Dimensionality of embeddings (set according to model)"
    )

    # App behavior
    LOG_LEVEL: str = Field("INFO", description="Logging level")
    DATA_DIR: str = Field(
        "data", description="Root data directory for samples and benchmarks"
    )
    TEMP_DIR: str = Field("/tmp/intellihire", description="Temporary working directory")

    # Server / API
    API_HOST: str = Field("127.0.0.1", description="Host for local API (if used)")
    API_PORT: int = Field(8000, description="Port for local API")

    # Misc
    MAX_CV_FILE_SIZE_MB: int = Field(10, description="Max accepted CV file size (MB)")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # Derived property
    @property
    def qdrant_url(self) -> str:
        return f"http://{self.QDRANT_HOST}:{self.QDRANT_PORT}"

    @validator("OLLAMA_URL", pre=True, always=True)
    def default_ollama_url(cls, v):
        # If env doesn't set OLLAMA_URL, try common default
        if v is None:
            default = os.getenv("OLLAMA_URL", "http://localhost:11434")
            return default
        return v


# Single shared settings instance for convenience
settings = Settings()
