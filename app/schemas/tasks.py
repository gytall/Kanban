"""Task schema definitions."""

from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    """Base task schema with common fields."""
    title: str
    description: Optional[str]


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    pass


class TaskOut(TaskBase):
    """Schema for task output."""
    id: int
    column_id: int

    class Config:
        orm_mode = True
