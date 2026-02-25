"""Board column model definition."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class BoardColumn(Base):
    """Board column model representing a column in a Kanban board."""
    
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="columns")
    tasks = relationship("Task", back_populates="column")
