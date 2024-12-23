from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text, nullable=True)
    column_id = Column(Integer, ForeignKey("columns.id"))

    column = relationship("BoardColumn", back_populates="tasks")

    logs = relationship("TaskLog", back_populates="task")
