# File: app/storage/schema.py

"""
Qdrant Payload Schema for CV Storage:

- cv_id: str                 -> Unique CV identifier
- name: str                  -> Candidate name
- email: str                 -> Email (optional for contact)
- phone: Optional[str]       -> Phone number (optional)
- years_experience: float    -> Numeric years of experience (filterable)
- skills: List[str]          -> Skills tags (filterable)
- education: Optional[str]   -> Highest education level
- location: Optional[str]    -> Geographic filter
- current_role: Optional[str]-> Present job title
- last_updated: str          -> ISO timestamp of ingestion
- raw_text: str              -> Full parsed text (for context retrieval)
"""

from typing import List, Optional
from pydantic import BaseModel, Field
import datetime


class CVPayload(BaseModel):
    cv_id: str
    name: str
    email: str
    phone: Optional[str] = None
    years_experience: float = Field(..., ge=0)  # non-negative
    skills: List[str]
    education: Optional[str] = None
    location: Optional[str] = None
    current_role: Optional[str] = None
    last_updated: str = datetime.datetime.utcnow().isoformat()
    raw_text: Optional[str] = None
