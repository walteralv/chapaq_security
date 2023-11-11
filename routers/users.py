from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from dtos.user import UserAuth, UserOut, UserUpdate
from services.userService import UserService
from models.users import User
from services.authService import getCurrentUser
from db.mysql import async_session
from sqlalchemy.exc import IntegrityError
from dtos.auth import LoginDTO

userRouter = APIRouter()

@userRouter.post('/create', summary="Create new user", response_model=UserOut)
async def createUser(data: UserAuth):
    async with async_session() as session:
        async with session.begin():
            try:
                return await UserService(session).createUser(data)
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email or dni already exist"
                )
    
@userRouter.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def getMe(user: User = Depends(getCurrentUser)):
    async with async_session() as session:
        async with session.begin():
            return user

