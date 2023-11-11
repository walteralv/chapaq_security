
from dtos.user import UserAuth, UserOut, UserUpdate
from dtos.citizen import CitizenCreate, CitizenOut
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
    
def getMe():
    pass

def getCitizenById(dni):
    pass

def changeImage(url):
    pass

def deleteAccount():
    pass

