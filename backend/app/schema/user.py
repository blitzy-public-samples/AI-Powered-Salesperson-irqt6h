from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: str
    email: str
    role: str
    last_login: Optional[datetime]

class UserCreate(BaseModel):
    email: str
    password: str
    role: str

class UserUpdate(BaseModel):
    email: Optional[str]
    password: Optional[str]
    role: Optional[str]