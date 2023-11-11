from models.serenazgo import Serenazgo
from dtos.serenazgo import SerenazgoUpdateImage
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update

async def getSerenazgoById(db: Session, dni: str):
    query = ( 
        select(Serenazgo)
        .where(Serenazgo.dni == dni)
        .limit(1)
    )
    Serenazgo = await db.scalar(query)
    return Serenazgo

async def updateImageSerenazgoById(db: Session, dni: str, data: SerenazgoUpdateImage):
    query = (
        update(Serenazgo).
        where(Serenazgo.dni == dni).
        values(
            urlImage= data.urlImage,
            uploadDate= data.uploadDate,
            updatedAt= data.updatedAt
        )
    )
    await db.execute(query)
