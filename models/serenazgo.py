from sqlalchemy import Column, Boolean, String, DateTime, Date, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .municipality import Municipality
from .schedule import Schedule

class Serenazgo(Base):
    __tablename__ = "serenazgo_table"

    dni = Column(String, primary_key=True, index=True)
    names = Column(String, nullable=False)
    surname1 = Column(String, nullable=False) 
    surname2 = Column(String, nullable=False)
    birthDate = Column(Date, nullable=False)
    phone = Column(String, index=True)
    address = Column(String, index=True)
    urlImage = Column(String)
    uploadDate = Column(DateTime)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, default=datetime.now)
    deletedAt = Column(DateTime, default=datetime.now)
    latitude = Column(Float) 
    longitude = Column(Float)


    userId = Column(String, ForeignKey('user_table.dni'))
    user = relationship("User", back_populates="serenazgo")
    
    municipalityId = Column(Integer, ForeignKey('municipality_table.id'))
    municipality = relationship("Municipality", back_populates="serenazgo")
    
    scheduleId = Column(Integer, ForeignKey('schedule_table.id'))
    schedule = relationship("Schedule", back_populates="serenazgo")

    incidence = relationship("Incidence", back_populates="serenazgo")
