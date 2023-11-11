from models.citizen import Citizen
from dtos.citizen import CitizenUpdateImage
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update



async def getCitizenById(db: Session, dni: str):
    query = ( 
        select(Citizen)
        .where(Citizen.dni == dni)
        .limit(1)
    )
    citizen = await db.scalar(query)
    return citizen


async def updateImageCitizenById(db: Session, dni: str, data: CitizenUpdateImage):
    query = (
        update(Citizen).
        where(Citizen.dni == dni).
        values(
            urlImage= data.urlImage,
            uploadDate= data.uploadDate,
            updatedAt= data.updatedAt
        )
    )
    await db.execute(query)







