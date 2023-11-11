from dtos.user import UserOut, UserAuth, UserUpdate
from dtos.citizen import CitizenCreate, CitizenUpdateImage, CitizenOut
from core.security import getPassword, verifyPassword
from models.users import User
from models.citizen import Citizen
from repository.users import getUserById
from repository.citizen import getCitizenById, updateImageCitizenById

from typing import Optional
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from datetime import datetime

class CitizenService:

    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

    async def createCitizen(self, userDni: str, data: CitizenCreate) -> Optional[Citizen]:
        citizenIn = Citizen(
            dni= userDni,
            names= data.names,
            surname1= data.surname1, 
            surname2= data.surname2,
            birthDate= data.birthDate,
            phone= data.phone,
            address= data.address,
            urlImage= data.urlImage,
            uploadDate= data.uploadDate,
            is_active= data.is_active,
            is_deleted= data.is_deleted,
            createdAt= datetime.now(),
            updatedAt= data.updatedAt,
            deletedAt= data.deletedAt,
            userId= userDni,
            districtId= data.districtId

        )

        self.dbSession.add(citizenIn)
        await self.dbSession.flush()
        return citizenIn



    async def getCitizenById(self, dni: str) -> Optional[Citizen]:
        citizen = await getCitizenById(self.dbSession, dni)
        if not citizen:
            return None
        return citizen
    
    async def updateImageCitizenById(self, dni: str, data: CitizenUpdateImage):
        await updateImageCitizenById(self.dbSession, dni, data)
        
    
    