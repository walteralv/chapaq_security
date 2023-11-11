from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class StatusCreate(BaseModel):
    id: str = Field(..., title='name of status type')
    name: str = Field(..., title='name of status type')

class StatusOut(BaseModel):
    id : str = Field(..., title='Id of status type')
    name: str = Field(..., title='name of status type')
