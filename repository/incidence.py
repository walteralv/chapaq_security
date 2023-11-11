from models.incidence import Incidence

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update

async def getAllIncident(db: Session):
    query = (
        select(Incidence).where(and_(Incidence.is_active == True, Incidence.is_deleted == False))
    )
    incidences = await db.scalars(query)
    return incidences

async def getAllIncidenceCitizenId(db: Session, citizenId: str):
    query = (
        select(Incidence).where(and_(Incidence.is_active == True, Incidence.is_deleted == False, Incidence.citizenId == citizenId))
    )
    incidences = await db.scalars(query)
    return incidences


async def getIncidenceById(db: Session, identifier: str):
    query = ( 
        select(Incidence)
        .where(Incidence.id == identifier)
        .limit(1)
    )
    user = await db.scalar(query)
    return user


async def getIncidenceStatusById(db: Session, identifier: str):
    query = (
        select(Incidence.id, Incidence.latitude, Incidence.longitude, Incidence.pheQuantity, Incidence.currentStatusId, Incidence.typeId)
        .where(Incidence.id == identifier)
        .limit(1)
    )
    user = await db.scalar(query)
    return user

