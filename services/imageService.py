from models.incidenceImage import IncidenceImage
<<<<<<< HEAD

from sqlalchemy.orm import Session
from datetime import datetime
=======
from core.config import Settings

from sqlalchemy.orm import Session
from datetime import datetime
import uuid
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441

class ImageService:

    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

<<<<<<< HEAD
=======
    async def loadToS3(self, s3, file ,filename: str):
        s3.upload_fileobj(file, "walter-garbage", filename)
        image_url = f"https://{Settings.AWS_BUCKET_NAME}.s3.{Settings.AWS_BUCKET_REGION}.amazonaws.com/{filename}"
        return image_url
    
    def generateImageuuid(self, file_type: str, file_extension: str):
        if(file_type == "image"):
            random_filename = str(uuid.uuid4()) + '.' + file_extension
        return random_filename
    
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441
    async def createIncidenceImage(self, image_path, incidenceId):
        incidenceImage = IncidenceImage(
            url = image_path,
            incidenceId = incidenceId
        )
        self.dbSession.add(incidenceImage)
        await self.dbSession.flush()
        return incidenceImage