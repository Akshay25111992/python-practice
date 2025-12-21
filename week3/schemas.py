# Pydantic Schemas for Request/Response Validation

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# User Registration Schema
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: Optional[str] = None


# User Response Schema
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Login Schema
class UserLogin(BaseModel):
    username: str
    password: str


# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str


# Token Data Schema
class TokenData(BaseModel):
    username: Optional[str] = None

