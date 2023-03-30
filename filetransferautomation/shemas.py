"""Schemas."""
from __future__ import annotations

from dataclasses import dataclass
import datetime
import uuid
from pydantic import BaseModel


@dataclass
class Folder:
    """Folder dataclass."""

    folder_id: int
    name: str


@dataclass
class File:
    """File dataclass."""

    name: str
    task_id: int | None = None
    size: int | None = None
    timestamp: datetime.datetime | None = None
    file_id: str = str(uuid.uuid4())


class AddTask(BaseModel):
    """Add task model."""

    name: str
    description: str | None = ""
    active: int = 1