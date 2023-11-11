from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import Base
from .citizen import Citizen
from .serenazgo import Serenazgo

class User(Base):
    
    __tablename__ = "user_table"

    dni = Column(String, primary_key=True)

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    citizen = relationship("Citizen", back_populates="user", uselist=False)
    serenazgo = relationship("Serenazgo", back_populates="user", uselist=False)
