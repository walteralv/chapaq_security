from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class IncidenceTypeCreate(BaseModel):
    id: str = Field(..., title='name of incidence type')
    name: str = Field(..., title='name of incidence type')
    priorityValue: int = Field(..., title='priority value of incidence type', ge=1, le=5)
    is_active: Optional[bool] = Field(default=True, title="incidence type is active")
    is_deleted: Optional[bool] = Field(default=False, title="incidence type is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")

class IncidenceTypeUpdate(BaseModel):
    name: Optional[str] = Field(None, title='name of incidence type')
    priorityValue: Optional[int] = Field(None, title='priority value of incidence type', ge=1, le=5)
    is_active: Optional[bool] = Field(default=True, title="incidence type is active")
    is_deleted: Optional[bool] = Field(default=False, title="incidence type is inactive")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")


class IncidenceTypeOut(BaseModel):
    id : str = Field(..., title='Id of incidence type')
    name: str = Field(..., title='name of incidence type')
    priorityValue: int = Field(..., title='priority value of incidence type', ge=1, le=5)
    is_active: bool = Field(default=True, title="incidence type is active")
    is_deleted: bool = Field(default=False, title="incidence type is inactive")
    createdAt: datetime = Field(default=datetime.now(), title="registration date")
    updatedAt: datetime | None = Field(default=None, title="updated date")
    deletedAt: datetime | None = Field(default=None, title="removed date")







