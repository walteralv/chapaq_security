from models.incidenceImage import IncidenceImage

from sqlalchemy.orm import Session
from datetime import datetime

class ImageService:

    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

    async def createIncidenceImage(self, image_path, incidenceId):
        incidenceImage = IncidenceImage(
            url = image_path,
            incidenceId = incidenceId
        )
        self.dbSession.add(incidenceImage)
        await self.dbSession.flush()
        return incidenceImage