"""Task log model definition."""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db import Base


class TaskLog(Base):
    """Task log model representing an action log for a task."""
    
    __tablename__ = "task_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    action = Column(Text)
    timestamp = Column(DateTime, default=func.now())

    task = relationship("Task", back_populates="logs")