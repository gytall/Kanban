from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

# Модель пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    created_at = Column(DateTime, default=func.now())

    # Связь с проектами
    projects = relationship("Project", back_populates="user")


# Модель проекта
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Связь с пользователем
    user = relationship("User", back_populates="projects")
    # Связь с колонками
    columns = relationship("BoardColumn", back_populates="project")


# Модель колонки
class BoardColumn(Base):
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Связь с проектом
    project = relationship("Project", back_populates="columns")
    # Связь с задачами
    tasks = relationship("Task", back_populates="column")


# Модель задачи
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text, nullable=True)
    column_id = Column(Integer, ForeignKey("columns.id"))

    # Связь с колонкой
    column = relationship("BoardColumn", back_populates="tasks")
    # Связь с логами
    logs = relationship("TaskLog", back_populates="task")


# Модель лога задачи
class TaskLog(Base):
    __tablename__ = "task_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    action = Column(Text)
    timestamp = Column(DateTime, default=func.now())

    # Связь с задачей
    task = relationship("Task", back_populates="logs")