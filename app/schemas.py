from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class UserSignup(BaseModel):
    email: str
    password: str


class UserPublic(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
