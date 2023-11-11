
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.incidenceType import IncidenceTypeCreate, IncidenceTypeUpdate, IncidenceTypeOut

from services.userService import UserService
from services.incidenceTypeServices import IncidenceTypeService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from dtos.auth import LoginDTO

from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends





typeRouter = APIRouter()



@typeRouter.get('/', summary="Get all indicent types", response_model=list[IncidenceTypeOut])
async def getAllIncidentTypes():
    async with async_session() as session:
        async with session.begin():
            try:
                return await IncidenceTypeService(session).getAllIncidentTypes()
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
               

@typeRouter.post('/create', summary="Create new indicent type", response_model=IncidenceTypeOut)
async def createUser(data: IncidenceTypeCreate):
    async with async_session() as session:
        async with session.begin():
            try:
                return await IncidenceTypeService(session).createIncidentType(data)
            
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incidence type already exist"
                )        

@typeRouter.get('/indicentType', summary="Get indicent type by Id", response_model=IncidenceTypeOut)
async def getAIncidentType(identifier: str):
    async with async_session() as session:
        async with session.begin():
            try:
                return await IncidenceTypeService(session).getIncidentTypeById(identifier)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )


