from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    status: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

    class Config:
        from_attributes = True