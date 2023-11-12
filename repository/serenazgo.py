from models.serenazgo import Serenazgo
from dtos.serenazgo import SerenazgoUpdateImage, SerenazgoLocationUpdate, SerenazgoUpdateActivate
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update

async def getSerenazgoById(db: Session, dni: str):
    query = ( 
        select(Serenazgo)
        .where(Serenazgo.dni == dni)
        .limit(1)
    )
    serenazgo = await db.scalar(query)
    return serenazgo

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
    
    
async def getAllSerenazgo(db: Session):
    query = ( 
        select(Serenazgo)
        .where(Serenazgo.is_active == True)
    )
    serenazgos = await db.scalars(query)
    return serenazgos



async def updateLocationSerenazgoById(db: Session, dni: str, data: SerenazgoLocationUpdate):
    query = (
        update(Serenazgo).
        where(Serenazgo.dni == dni).
        values(
            latitude= data.latitude,
            longitude= data.longitude,
            updatedAt= data.updatedAt
        )
    )
    await db.execute(query)
    
    
async def updateActivateSerenazgoById(db: Session, dni: str, data: SerenazgoUpdateActivate):
    query = (
        update(Serenazgo).
        where(Serenazgo.dni == dni).
        values(
            is_active= data.is_active
        )
    )
    await db.execute(query)
    
    
async def getSerenazgoStatusById(db: Session, dni: str):
    query = (
        select(Serenazgo.dni, Serenazgo.latitude, Serenazgo.longitude)
        .where(Serenazgo.dni == dni)
        .limit(1)
    )
    user = await db.scalar(query)
    return user



    
    

