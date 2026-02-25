"""User schema definitions."""

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    """Base user schema with common fields."""
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str


class UserOut(UserBase):
    """Schema for user output."""
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  
