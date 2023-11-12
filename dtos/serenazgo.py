from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime



class SerenazgoCreate(BaseModel):
    names: str = Field(..., title='Serenazgo names')
    surname1: str = Field(..., title='Serenazgo surname1')
    surname2: str = Field(..., title='Serenazgo surname2')
    birthDate: datetime = Field(default=datetime.now().today(), title="registration date")
    phone: str = Field(..., title='Serenazgo phone')
    address: Optional[str]  = Field(default=None, title='Serenazgo phone')
    urlImage: Optional[str]  = Field(default=None, title='Serenazgo urlImage')
    uploadDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
    is_active: Optional[bool] = Field(default=True, title="Serenazgo is active")
    is_deleted: Optional[bool] = Field(default=False, title="Serenazgo is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    municipalityId: int = Field(...,title="municipality")
    scheduleId: int =  Field(..., title="scheduleId")
    latitude: float = Field(..., title='incidence latitude')
    longitude: float = Field(..., title='incidence latitude')


class SerenazgoOut(BaseModel):
    dni: str = Field(..., title='Serenazgo dni')
    names: str = Field(..., title='Serenazgo names')
    surname1: str = Field(..., title='Serenazgo surname1')
    surname2: str = Field(..., title='Serenazgo surname2')
    birthDate: datetime = Field(default=datetime.now().today(), title="registration date")
    phone: str = Field(..., title='Serenazgo phone')
    address: Optional[str]  = Field(default=None, title='Serenazgo phone')
    urlImage: Optional[str]  = Field(default=None, title='Serenazgo urlImage')
    uploadDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
    is_active: Optional[bool] = Field(default=True, title="Serenazgo is active")
    is_deleted: Optional[bool] = Field(default=False, title="Serenazgo is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    userId: str = Field(..., title='user dni')
    municipalityId: int = Field(...,title="municipality")
    scheduleId: int =  Field(..., title="scheduleId")
    latitude: float = Field(..., title='incidence latitude')
    longitude: float = Field(..., title='incidence latitude')
    

class SerenazgoUpdateImage(BaseModel):
    urlImage: str  = Field(..., title='Serenazgo urlImage')
    uploadDate: datetime = Field(..., title="uplodad image date")
    updatedAt: datetime = Field(..., title="updated date")
    

class SerenazgoUpdateActivate(BaseModel):
    is_active: bool = Field(..., title="Serenazgo is active")
    
    
class SerenazgoLocationUpdate(BaseModel):
    latitude: float = Field(..., title='Serenazgo latitude')
    longitude: float = Field(..., title='Serenazgo latitude')
    updatedAt: datetime = Field(..., title="updated date")
    

class SerenazgoStatus(BaseModel):
    dni: str =  Field(..., title='Serenazgo id')
    latitude: float = Field(..., title='Serenazgo latitude')
    longitude: float = Field(..., title='Serenazgo latitude')


    
