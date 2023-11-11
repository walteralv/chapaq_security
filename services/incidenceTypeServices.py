from models.users  import User
from models.incidenceType import IncidenceType
from dtos.incidenceType import IncidenceTypeCreate, IncidenceTypeOut, IncidenceTypeUpdate
from repository.incidenceType import getAllIncidentTypes, getIncidentTypeById

from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime


class IncidenceTypeService:
    def __init__(self, dbSession: Session) -> None:
        self.dbSession = dbSession
    
    async def getAllIncidentTypes(self) ->  List[IncidenceType]:
        types = await getAllIncidentTypes(self.dbSession)
        if not types:
            return None
        return types
    
    async def createIncidentType(self, data: IncidenceTypeCreate) -> Optional[IncidenceType]:
        typeIn = IncidenceType(
            id = data.id,
            name= data.name,
            priorityValue= data.priorityValue,
            is_active= data.is_active,
            is_deleted= data.is_deleted,
            createdAt= data.createdAt,
            updatedAt= data.updatedAt,
            deletedAt= data.deletedAt
        )
        self.dbSession.add(typeIn)
        await self.dbSession.flush()
        return typeIn
    
    async def getIncidentTypeById(self, identifier: str) -> Optional[IncidenceType]:
        incidentType = await getIncidentTypeById(self.dbSession, identifier)
        if not incidentType:
            return None
        return incidentType
    



    


    