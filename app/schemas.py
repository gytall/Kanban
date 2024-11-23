from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  # Пароль будет передаваться при создании пользователя

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Включаем, чтобы Pydantic корректно работал с SQLAlchemy моделями

# Project Schemas
class ProjectBase(BaseModel):
    name: str
    description: Optional[str]  # Описание проекта может быть пустым

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int

    class Config:
        orm_mode = True

# BoardColumn (Column) Schemas
class BoardColumnBase(BaseModel):
    name: str

class BoardColumnCreate(BoardColumnBase):
    pass

class BoardColumnOut(BoardColumnBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True

# Task Schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str]  # Описание задачи может быть пустым

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    column_id: int

    class Config:
        orm_mode = True

# TaskLog Schemas
class TaskLogBase(BaseModel):
    action: str

class TaskLogCreate(TaskLogBase):
    pass

class TaskLogOut(TaskLogBase):
    id: int
    task_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
