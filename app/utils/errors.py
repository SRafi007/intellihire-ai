# -----------------------------
# FILE: app/utils/errors.py
# -----------------------------
from __future__ import annotations

from typing import Optional


class IntelliHireError(Exception):
    """Base exception for the IntelliHire project.

    All custom exceptions should inherit from this so callers can catch a
    single type for project-level errors.
    """

    def __init__(self, message: str, *, code: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"{self.__class__.__name__}: {self.message}"


class ConfigurationError(IntelliHireError):
    """Configuration or environment-related errors."""


class IngestError(IntelliHireError):
    """Errors during file ingestion, OCR, parsing, or metadata extraction."""


class ParsingError(IngestError):
    """Errors while parsing file formats (PDF/DOCX/TXT)."""


class OCRExtractionError(IngestError):
    """OCR specific failures (tesseract failure, unreadable image)."""


class EmbeddingError(IntelliHireError):
    """Errors from embedding model calls or serialization."""


class StorageError(IntelliHireError):
    """Errors interacting with the vector DB (qdrant) or other storage."""


class RetrievalError(IntelliHireError):
    """Errors during retrieval from vector DB or RAG steps."""


class ScoringError(IntelliHireError):
    """Scoring pipeline errors (aggregator, ML model, etc.)."""


class ExternalServiceError(IntelliHireError):
    """Generic error for third-party services (LLM, Ollama, remote APIs)."""


# Example helper to convert exceptions to structured dicts (useful in APIs)
def exception_to_dict(exc: Exception) -> dict:
    """Return a small serializable representation of an exception."""
    if isinstance(exc, IntelliHireError):
        return {
            "type": exc.__class__.__name__,
            "message": exc.message,
            "code": exc.code,
        }
    return {"type": exc.__class__.__name__, "message": str(exc)}
