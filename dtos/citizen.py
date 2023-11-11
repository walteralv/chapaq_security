from uuid import UUID
from typing import Annotated, Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime



class CitizenCreate(BaseModel):
    names: str = Field(..., title='citizen names')
    surname1: str = Field(..., title='citizen surname1')
    surname2: str = Field(..., title='citizen surname2')
    birthDate: datetime = Field(default=datetime.now().today(), title="registration date")
    phone: str = Field(..., title='citizen phone')
    address: Optional[str]  = Field(default=None, title='citizen phone')
    urlImage: Optional[str]  = Field(default=None, title='citizen urlImage')
<<<<<<< HEAD
    uploadDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
=======
    upladDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441
    is_active: Optional[bool] = Field(default=True, title="citizen is active")
    is_deleted: Optional[bool] = Field(default=False, title="citizen is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    districtId: Optional[str] = Field(default=None, title="district alpha Code")



class CitizenOut(BaseModel):
    dni: str = Field(..., title='citizen dni')
    names: str = Field(..., title='citizen names')
    surname1: str = Field(..., title='citizen surname1')
    surname2: str = Field(..., title='citizen surname2')
    birthDate: datetime = Field(default=datetime.now().today(), title="registration date")
    phone: str = Field(..., title='citizen phone')
    address: Optional[str]  = Field(default=None, title='citizen phone')
    urlImage: Optional[str]  = Field(default=None, title='citizen urlImage')
<<<<<<< HEAD
    uploadDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
=======
    upladDate: Optional[datetime] = Field(default=datetime.now(), title="uplodad image date")
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441
    is_active: Optional[bool] = Field(default=True, title="citizen is active")
    is_deleted: Optional[bool] = Field(default=False, title="citizen is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    userId: str = Field(..., title='user dni')
    districtId: Optional[str] = Field(default=None, title="district alpha Code")

<<<<<<< HEAD
class CitizenUpdateImage(BaseModel):
    urlImage: str  = Field(..., title='citizen urlImage')
    uploadDate: datetime = Field(..., title="uplodad image date")
    updatedAt: datetime = Field(..., title="updated date")

    
=======
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441
