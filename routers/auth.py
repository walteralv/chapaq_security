from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from db.mysql import async_session
from models.users import User
from services.userService import UserService 
from services.authService import getCurrentUser
from core.security import createAccessToken, createRefreshToken
from dtos.auth import TokenSchema , TokenPayload
from dtos.user import UserOut
from core.config import settings
from jose import jwt , JWTError
from pydantic import ValidationError
from typing import Any



authRouter = APIRouter()

@authRouter.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(formData: OAuth2PasswordRequestForm= Depends()) -> Any:
    async with async_session() as session:
        async with session.begin():
            user = await UserService(session).authenticate(identifier= formData.username, hashedPassword= formData.password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Incorrect identifier or password"
                )
            return {
                "access_token": createAccessToken(user.dni),
                "refresh_token": createRefreshToken(user.dni),
            }

@authRouter.post('/refresh', summary="Refresh token", response_model=TokenSchema)
async def refreshToken(refres_token: str = Body(...)):
    async with async_session() as session:
        async with session.begin():
            try:
                payload = jwt.decode(refres_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
                tokenData = TokenPayload(**payload)
            except (JWTError, ValidationError):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            user = await UserService(session).getUserByIdentifier(tokenData.sub)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid token",
                )
            return {
                "access_token": createAccessToken(user.dni),
                "refresh_token": createRefreshToken(user.dni),
            }
