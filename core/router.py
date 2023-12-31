from fastapi import APIRouter
from routers import users
from routers import auth
from routers import incidenceType
from routers import upload
from routers import incidence
from routers import citizen
from routers import serenazgo
from routers import status

router = APIRouter()

router.include_router(users.userRouter, prefix='/users', tags=["users"])
router.include_router(auth.authRouter, prefix='/auth', tags=["auth"])
router.include_router(upload.uploadRouter, prefix='/upload', tags=["upload"])
router.include_router(incidenceType.typeRouter, prefix='/incidenceType', tags=["incidenceType"])
router.include_router(incidence.incidenceRouter, prefix='/incidence', tags=["incidence"])
router.include_router(citizen.citizenRouter, prefix='/citizen', tags=["citizen"])
router.include_router(serenazgo.serenazgoRouter, prefix='/serenazgo', tags=["Serenazgo"])
router.include_router(status.statusRouter, prefix='/status', tags=["status"])
