from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Union, Any
from core.config import settings
from jose import jwt

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def createAccessToken(subject: Union[str, Any], expiresDelta: int = None) -> str:
    if expiresDelta is not None:
        expiresDelta = datetime.utcnow() + expiresDelta
    else:
        expiresDelta = datetime.utcnow() +timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    toEncode = {"exp": expiresDelta, "sub": str(subject)}
    encodedJWT = jwt.encode(toEncode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return encodedJWT

def createRefreshToken(subject: Union[str, Any], expiresDelta: int=None) -> str:
    if expiresDelta is not None:
        expiresDelta = datetime.utcnow() + expiresDelta
    else:
        expiresDelta = datetime.utcnow() +timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES) 

    toEncode = {"exp": expiresDelta, "sub": str(subject)}

    encodedJWT = jwt.encode(toEncode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    return encodedJWT

def getPassword(password: str) -> str:
    return passwordContext.hash(password)

def verifyPassword(password: str, hashedpass: str) -> bool:
    return passwordContext.verify(password, hashedpass)