
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.incidence import IncidenceCreate, IncidenceUpdate, IncidenceOut, IncidenceStatus, IncidenceLocationUpdate, IncidenceStatusUpdate
from services.userService import UserService
from services.incidenceService import IncidenceService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from dtos.auth import LoginDTO

from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends

incidenceRouter = APIRouter()



@incidenceRouter.post('/me/create/', summary="Create new incidence", response_model=IncidenceOut)
async def createIncidence(data: IncidenceCreate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    return await IncidenceService(session).createIncidence(user.dni, data)
                raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incidence already exist"
                ) 
            
@incidenceRouter.get('/{id}', summary="Get incidence by Id", response_model= IncidenceOut)
async def getIncidenceById(id: int):
    async with async_session() as session:
        async with session.begin():
            try:
                incidence = await IncidenceService(session).getIncidenceById(id)
                print(incidence)
                return incidence
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
@incidenceRouter.get('/citizen/{id}', summary="Get all incidences of citizen", response_model=list[IncidenceOut])
async def getAllIncidenceByCitizen(id: str):
    async with async_session() as session:
        async with session.begin():
            try:
                return await IncidenceService(session).getAllIncidenceCitizenId(id)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
@incidenceRouter.get('/{id}/status', summary="Get incidence status by Id", response_model= IncidenceStatus)
async def getIncidenceStatusById(id: str):
    async with async_session() as session:
        async with session.begin():
            try:
                return await IncidenceService(session).getIncidenceStatusById(id)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                
                
                
@incidenceRouter.put('/incidence/{id}/update/location/', summary="update location current citizen", response_model= IncidenceOut)
async def updateLocationIncidenceById(id: int, data: IncidenceLocationUpdate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await IncidenceService(session).updateLocationIncidenceById(id, data)
                    return await IncidenceService(session).getIncidenceById(id)
                raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                
                
@incidenceRouter.put('/incidence/{id}/update/status/', summary="update status current citizen", response_model= IncidenceOut)
async def updateLocationIncidenceById(id: int, data: IncidenceStatusUpdate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await IncidenceService(session).updateStatusIncidenceById(id,data)
                    return await IncidenceService(session).getIncidenceById(id)
                raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
