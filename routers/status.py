
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.status import StatusCreate, StatusOut

from services.userService import UserService
from services.statusService import StatusService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from dtos.auth import LoginDTO

from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends





statusRouter = APIRouter()



@statusRouter.post('/create', summary="Create new status type", response_model=StatusOut)
async def createUser(data: StatusCreate):
    async with async_session() as session:
        async with session.begin():
            try:
                return await StatusService(session).createStatus(data)
            
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incidence type already exist"
                )       


@statusRouter.get('/AllStatus', summary="Get status type by Id", response_model=list[StatusOut])
async def getAllStatus():
    async with async_session() as session:
        async with session.begin():
            try:
                return await StatusService(session).getAllStatus()
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )


