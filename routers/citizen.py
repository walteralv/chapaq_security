
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.citizen import CitizenCreate, CitizenOut, CitizenUpdateImage
from services.userService import UserService
from services.citizenService import CitizenService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from dtos.auth import LoginDTO


from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.exc import IntegrityError

citizenRouter = APIRouter()


@citizenRouter.post('/create', summary="Create new citizen", response_model=CitizenOut)
async def createCitizen(data: CitizenCreate, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    return await CitizenService(session).createCitizen(user.dni, data)
                raise HTTPException(
                    status_code= status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email or dni already exist"
                )
                
                
@citizenRouter.get('/{id}', summary="Get citizen by Id", response_model= CitizenOut)
async def getCitizenById(id: int):
    async with async_session() as session:
        async with session.begin():
            try:
                incidence = await CitizenService(session).getCitizenById(id)
                print(incidence)
                return incidence
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                
                
@citizenRouter.get('/me/{id}', summary="Get current citizen", response_model= CitizenOut)
async def getCurrentCitizen(user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    return await CitizenService(session).getCitizenById(user.dni)
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
                
                
                
@citizenRouter.put('/me/{id}/update/image/', summary="update image current citizen", response_model= CitizenOut)
async def updateImageCitizenById(data: CitizenUpdateImage, user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            try:
                if user is not None:
                    await CitizenService(session).updateImageCitizenById(user.dni, data)
                    return await CitizenService(session).getCitizenById(user.dni)
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
                
                
                
    
def getMe():
    pass

def getCitizenById(dni):
    pass

def changeImage(url):
    pass

def deleteAccount():
    pass

