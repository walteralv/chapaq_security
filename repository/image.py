from models.incidenceImage import IncidenceImage
<<<<<<< HEAD
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

=======

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update
>>>>>>> f460b6e54976db3a43cb9eb2a95d2d942e5f3441
