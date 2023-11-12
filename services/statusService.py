from models.users  import User
from models.status import Status
from dtos.status import StatusCreate, StatusOut
from repository.status import getAllStatus

from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import datetime


class StatusService:
    def __init__(self, dbSession: Session) -> None:
        self.dbSession = dbSession
    
    async def getAllStatus(self) ->  List[Status]:
        types = await getAllStatus(self.dbSession)
        if not types:
            return None
        return types
    
    async def createStatus(self, data: StatusCreate) -> Optional[Status]:
        typeIn = Status(
            id = data.id,
            name= data.name
        )
        self.dbSession.add(typeIn)
        await self.dbSession.flush()
        return typeIn
    
    



    


    