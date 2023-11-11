from sqlalchemy import Column, Boolean, String, DateTime, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .district import District
from .incidence import Incidence

class Citizen(Base):

    __tablename__ = "citizen_table"

    dni = Column(String, primary_key=True, index=True)
    names = Column(String, nullable=False)
    surname1 = Column(String, nullable=False) 
    surname2 = Column(String, nullable=True)
    birthDate = Column(Date, nullable=True)
    phone = Column(String, index=True)
    address = Column(String, index=True)
    urlImage = Column(String, nullable=True)
    uploadDate = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, nullable=True)
    deletedAt = Column(DateTime, nullable=True)

    userId = Column(String, ForeignKey('user_table.dni'))
    user = relationship("User", back_populates="citizen")

    districtId = Column(String, ForeignKey('district_table.alphaCode'), nullable=True)
    district = relationship("District", back_populates="citizen")

    incidence = relationship("Incidence", back_populates="citizen")
