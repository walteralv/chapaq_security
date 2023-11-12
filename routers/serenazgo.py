
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.serenazgo import SerenazgoCreate, SerenazgoOut, SerenazgoUpdateImage, SerenazgoLocationUpdate, SerenazgoUpdateActivate
from services.userService import UserService
from services.serenazgoService import SerenazgoService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from dtos.auth import LoginDTO


from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.exc import IntegrityError

serenazgoRouter = APIRouter()


@serenazgoRouter.post('/create', summary="Create new Serenazgo", response_model=SerenazgoOut)
async def createSerenazgo(data: SerenazgoCreate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    return await SerenazgoService(session).createSerenazgo(user.dni, data)
                raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email or dni already exist"
                )

@serenazgoRouter.get('/me', summary="Get current Serenazgo", response_model= SerenazgoOut)
async def getCurrentSerenazgo(user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    return await SerenazgoService(session).getSerenazgoById(user.dni)
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
                
@serenazgoRouter.put('/me/update/image/', summary="update image current Serenazgo")
async def updateImageSerenazgoById(data: SerenazgoUpdateImage, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await SerenazgoService(session).updateImageSerenazgoById(user.dni, data)
                    return await SerenazgoService(session).getSerenazgoById(user.dni)
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

@serenazgoRouter.get('/allserenazgos', summary="Get all Serenazgo", response_model= list[SerenazgoOut])
async def getAllSerenazgo():
    async with async_session() as session:
        async with session.begin():
            try:
                
                serenazgos = await SerenazgoService(session).getAllSerenazgo()
                return serenazgos
             
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )  

@serenazgoRouter.get('/{id}', summary="Get Serenazgo by Id", response_model= SerenazgoOut)
async def getSerenazgoById(id: int):
    async with async_session() as session:
        async with session.begin():
            try:
                incidence = await SerenazgoService(session).getSerenazgoById(id)
                print(incidence)
                return incidence
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )    
                
                
@serenazgoRouter.put('/serenazgo/{dni}/update/location/', summary="update location serenazgo", response_model= SerenazgoOut)
async def updateLocationSerenazgoById(dni: str, data: SerenazgoLocationUpdate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await SerenazgoService(session).updateLocationIncidenceById(dni, data)
                    return await SerenazgoService(session).getSerenazgoById(dni)
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
                
@serenazgoRouter.put('/serenazgo/{dni}/update/activate/', summary="update activate current serenazgo", response_model= SerenazgoOut)
async def updateActivateSerenazgoById(dni: str, data: SerenazgoUpdateActivate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await SerenazgoService(session).updateActivateSerenazgoById(dni, data)
                    return await SerenazgoService(session).getSerenazgoById(dni)
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

@serenazgoRouter.get('/{dni}/status', summary="Get serenazgo status by Id", response_model= SerenazgoOut)
async def getIncidenceStatusById(dni: str):
    async with async_session() as session:
        async with session.begin():
            try:
                return await SerenazgoService(session).getSerenazgoStatusById(dni)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )