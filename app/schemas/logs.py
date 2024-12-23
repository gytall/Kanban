from pydantic import BaseModel
from datetime import datetime

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