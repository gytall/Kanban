from pydantic import BaseModel

class BoardColumnBase(BaseModel):
    name: str

class BoardColumnCreate(BoardColumnBase):
    pass

class BoardColumnOut(BoardColumnBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True
