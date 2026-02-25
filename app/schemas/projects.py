"""Project schema definitions."""

from pydantic import BaseModel
from typing import Optional


class ProjectBase(BaseModel):
    """Base project schema with common fields."""
    name: str
    description: Optional[str]


class ProjectCreate(ProjectBase):
    """Schema for creating a new project."""
    pass


class ProjectOut(ProjectBase):
    """Schema for project output."""
    id: int
    user_id: int

    class Config:
        orm_mode = True
