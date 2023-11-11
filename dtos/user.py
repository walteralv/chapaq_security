from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
import datetime

class UserAuth(BaseModel):
    dni: str = Field(..., description="user dni") 
    email: EmailStr = Field(..., description="user email")
    hashed_password: str = Field(..., min_length=5, max_length=24, description="user password")

class UserOut(BaseModel):
    dni: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False

class UserUpdate(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    