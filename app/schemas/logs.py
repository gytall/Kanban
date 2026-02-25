"""Task log schema definitions."""

from pydantic import BaseModel
from datetime import datetime


class TaskLogBase(BaseModel):
    """Base task log schema with common fields."""
    action: str


class TaskLogCreate(TaskLogBase):
    """Schema for creating a new task log."""
    pass


class TaskLogOut(TaskLogBase):
    """Schema for task log output."""
    id: int
    task_id: int
    timestamp: datetime

    class Config:
        orm_mode = True