from models.users import User

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_

async def getUserById(db: Session, identifier: int):
    query = (
        select(User)
        .where(or_(User.email == identifier, User.dni == identifier))
        .limit(1)
    )
    user = await db.scalar(query)
    return user