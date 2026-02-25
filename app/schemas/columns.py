"""Board column schema definitions."""

from pydantic import BaseModel


class BoardColumnBase(BaseModel):
    """Base board column schema with common fields."""
    name: str


class BoardColumnCreate(BoardColumnBase):
    """Schema for creating a new board column."""
    pass


class BoardColumnOut(BoardColumnBase):
    """Schema for board column output."""
    id: int
    project_id: int

    class Config:
        orm_mode = True
