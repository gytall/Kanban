from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] 

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    column_id: int

    class Config:
        orm_mode = True
