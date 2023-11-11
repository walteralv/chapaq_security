from db.mysql import async_session
from services.imageService import ImageService

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from sqlalchemy.exc import IntegrityError
import uuid
import shutil
from services.imageService import ImageService  
from db.s3 import get_s3_client

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from sqlalchemy.exc import IntegrityError

uploadRouter = APIRouter()

@uploadRouter.post("/img/inicidence/{id}")
async def create_upload_file(id: int, file: UploadFile):
    
    file_type, file_extension = file.content_type.split('/')
    if(file_type == "image"):
        random_filename = str(uuid.uuid4()) + '.' + file_extension
        image_path = "img/" + random_filename
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    async with async_session() as session:
        async with session.begin():
            try:
                imageService = ImageService(session)
                return await imageService.createIncidenceImage(image_path, incidenceId=id)
                file_type, file_extension = file.content_type.split('/')
                random_filename = imageService.generateImageuuid(file_type, file_extension)
                s3 = get_s3_client()
                image_path = await imageService.loadToS3(s3, file.file, random_filename)
                return await imageService.createIncidenceImage(image_path, id)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error to load Incidence Image"
                )

@uploadRouter.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}