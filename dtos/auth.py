from uuid import UUID
from pydantic import BaseModel

class LoginDTO(BaseModel):
    dni: str  
    email: str  
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None