from models.incidenceImage import IncidenceImage
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

