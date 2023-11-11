from models.status import Status

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_



async def getAllStatus(db: Session):
    query = (
        select(Status).where(and_(Status.is_active == True, Status.is_deleted == False))
    )
    types = await db.scalars(query)
    return types

