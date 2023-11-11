from dtos.user import UserOut, UserAuth, UserUpdate
from core.security import getPassword, verifyPassword
from models.users import User
from repository.users import getUserById

from typing import Optional
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from datetime import datetime

class UserService:

    def __init__(self, dbSession: Session):
        self.dbSession = dbSession

    async def createUser(self, user: UserAuth) -> Optional[User]:
        hashedPassword = getPassword(user.hashed_password)
        userIn = User(
            dni=user.dni,
            email=user.email,
            hashed_password=hashedPassword,
            is_active=True,
            is_deleted=False,
            createdAt=datetime.now(),
            updatedAt=None,
            deletedAt=None
        )
        self.dbSession.add(userIn)
        await self.dbSession.flush()
        return userIn


    async def authenticate(self, identifier: str, hashedPassword: str) -> Optional[User]:
        user = await getUserById(self.dbSession, identifier)

        if not user or not verifyPassword(hashedPassword, user.hashed_password):
            return None
        return user

    async def getUserByIdentifier(self, identifier: str) -> Optional[User]:
        user = await getUserById(self.dbSession, identifier)

        if not user:
            return None
        return user