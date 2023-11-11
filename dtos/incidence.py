from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime



class IncidenceCreate(BaseModel):
    #id: int =  Field(..., title='incidence id')
    description: Optional[str] = Field(default=None, title="incidence description")
    latitude: float = Field(..., title='incidence latitude')
    longitude: float = Field(..., title='incidence latitude')
    address: Optional[str] = Field(default=None, title="incidence address")
    pheQuantity: float = Field(..., title='incidence pheromone')
    closingDate: Optional[datetime] = Field(default=None, title="closing date")
    is_active: Optional[bool] = Field(default=True, title="incidence type is active")
    is_deleted: Optional[bool] = Field(default=False, title="incidence type is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now().today(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    citizenId: Optional[str] = Field(default=None, title="citizen dni")
    serenazgoId: Optional[str] = Field(default=None, title="serenazgo dni")
    districtId: Optional[str] = Field(default=None, title="district alpha Code")
    currentStatusId: Optional[str] = Field(default=None, title="incidence status id")
    typeId: Optional[str] = Field(default=None, title="incidence type id")


class IncidenceUpdate(BaseModel):
    description: Optional[str] = Field(default=None, title="incidence description")
    latitude:  Optional[float] = Field(..., title='incidence latitude')
    longitude:  Optional[float] = Field(..., title='incidence latitude')
    address: Optional[str] = Field(default=None, title="incidence address")
    pheQuantity:  Optional[float] = Field(..., title='incidence pheromone')
    closingDate: Optional[datetime] = Field(default=None, title="closing date")
    is_active: Optional[bool] = Field(default=True, title="incidence type is active")
    is_deleted: Optional[bool] = Field(default=False, title="incidence type is inactive")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    serenazgoId: Optional[str] = Field(default=None, title="serenazgo dni")
    currentStatusId: Optional[str] = Field(default=None, title="incidence status id")


class IncidenceOut(BaseModel):
    id: int =  Field(..., title='incidence id')
    description: Optional[str] = Field(default=None, title="incidence description")
    latitude: float = Field(..., title='incidence latitude')
    longitude: float = Field(..., title='incidence latitude')
    address: Optional[str] = Field(default=None, title="incidence address")
    pheQuantity: float = Field(..., title='incidence pheromone')
    closingDate: Optional[datetime] = Field(default=None, title="closing date")
    is_active: Optional[bool] = Field(default=True, title="incidence type is active")
    is_deleted: Optional[bool] = Field(default=False, title="incidence type is inactive")
    createdAt: Optional[datetime] = Field(default=datetime.now().today(), title="registration date")
    updatedAt: Optional[datetime] = Field(default=None, title="updated date")
    deletedAt: Optional[datetime] = Field(default=None, title="removed date")
    citizenId: Optional[str] = Field(default=None, title="citizen dni")
    serenazgoId: Optional[str] = Field(default=None, title="serenazgo dni")
    districtId: Optional[str] = Field(default=None, title="district alpha Code")
    currentStatusId: Optional[str] = Field(default=None, title="incidence status id")
    typeId: Optional[str] = Field(default=None, title="incidence type id")


class IncidenceStatus(BaseModel):
    id: int =  Field(..., title='incidence id')
    latitude: float = Field(..., title='incidence latitude')
    longitude: float = Field(..., title='incidence latitude')
    pheQuantity: float = Field(..., title='incidence pheromone')
    currentStatusId: Optional[str] = Field(default=None, title="incidence status id")
    typeId: Optional[str] = Field(default=None, title="incidence type id")
    
    







