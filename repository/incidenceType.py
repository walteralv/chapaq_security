from models.incidenceType import IncidenceType

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_



async def getAllIncidentTypes(db: Session):
    query = (
        select(IncidenceType).where(and_(IncidenceType.is_active == True, IncidenceType.is_deleted == False))
    )
    types = await db.scalars(query)
    return types


async def getIncidentTypeById(db: Session, identifier: str):
    query = (
        select(IncidenceType)
        .where(IncidenceType.id == identifier)
        .limit(1)
    )
    user = await db.scalar(query)
    return user
