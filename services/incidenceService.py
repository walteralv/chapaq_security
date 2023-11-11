from dtos.incidence import IncidenceCreate, IncidenceUpdate, IncidenceOut, IncidenceLocationUpdate, IncidenceStatusUpdate
from models.users  import User
from models.incidence import Incidence
from repository.incidence import  getAllIncidenceCitizenId, getAllIncident, getIncidenceById , updateLocationIncidenceById, updateStatusIncidenceById

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime

class IncidenceService:
    def __init__(self, dbSession: Session) -> None:
        self.dbSession = dbSession

    async def createIncidence(self,dni, data: IncidenceCreate) -> Optional[Incidence]:
        incidenceIn = Incidence(
            #id= data.id,
            description= data.description, 
            latitude=  data.latitude,
            longitude= data.longitude,
            address= data.address,
            pheQuantity=  data.pheQuantity,
            closingDate= data.closingDate,
            is_active= data.is_active,
            is_deleted=  data.is_deleted,
            createdAt=  data.createdAt,
            updatedAt=  data.updatedAt,
            deletedAt=  data.deletedAt,
            citizenId=  dni,
            serenazgoId=  data.serenazgoId,
            districtId= data.districtId,
            currentStatusId=  data.currentStatusId,
            typeId= data.typeId,
        )
        self.dbSession.add(incidenceIn)
        await self.dbSession.flush()
        return incidenceIn
    
    async def getIncidenceById(self, id):
        incidence = await getIncidenceById(self.dbSession, id)
        if not incidence:
            return None
        return incidence

    async def getAllIncidenceCitizenId(self, citizenId: str) -> Optional[Incidence]:
        incidences = await getAllIncidenceCitizenId(self.dbSession, citizenId)
        if not incidences:
            return None
        return incidences


    async def getIncidenceStatusById(self, identifier: str) -> Optional[Incidence]:
        incidence = await getIncidenceById(self.dbSession, identifier)
        if not incidence:
            return None
        return incidence
    
    
    async def updateLocationIncidenceById(self, id: int, data: IncidenceLocationUpdate)-> Optional[Incidence]:
        incidence = await updateLocationIncidenceById(self.dbSession, id, data)
        if not incidence:
            return None
        return incidence
    
    async def updateStatusIncidenceById(self, id: int, data: IncidenceStatusUpdate)-> Optional[Incidence]:
        incidence = await updateStatusIncidenceById(self.dbSession, id, data)
        if not incidence:
            return None
        return incidence
    

    

    

    async def modifyIncident(self, user: User):
        pass

    async def incidentTracking(self, user: User):
        pass

    async def getAllIncidentTypes(self, user: User):
        pass

    async def getIncidenceLocation(self, user: User):
        pass

    async def getCurrentStatus(self, user: User):
        pass

    async def modifyStatus(self, user: User):
        pass

    async def addImage(self, user: User):
        pass

    async def getAllImages(self, user: User):
        pass

    async def deleteImage(self, user: User):
        pass



