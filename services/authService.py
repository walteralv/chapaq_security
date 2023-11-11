from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.config import settings
from models.users import User
from jose import jwt, JWTError
from pydantic import ValidationError
from services.userService import UserService
from dtos.auth import TokenPayload
from sqlalchemy.orm import Session  # Add the import for the Session type
from db.mysql import async_session


reuseableOauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

async def getCurrentUser(
    token: str = Depends(reuseableOauth),
) -> User:
    async with async_session() as session:
        async with session.begin():
            try:
                payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
                tokenData = TokenPayload(**payload)

                if datetime.fromtimestamp(tokenData.exp) < datetime.now():
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token expired",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
            except (JWTError, ValidationError):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            user = await UserService(session).getUserByIdentifier(tokenData.sub)  

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Could not find user",
                )

            return user
    
