from sqlalchemy import Column, Boolean, String, DateTime, Date, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base

from .serenazgo import Serenazgo
from .district import District
from .status import Status
from .incidenceType import IncidenceType

from .incidenceImage import IncidenceImage
from .incidenceStatus import IncidenceStatus
class Incidence(Base):
    __tablename__ = "incidence_table"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    description = Column(String, nullable=True)
    latitude = Column(Float) 
    longitude = Column(Float)
    address = Column(String, nullable=True)
    pheQuantity = Column(Float, nullable=True)
    closingDate = Column(DateTime, nullable=True)


    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, nullable=True)
    deletedAt = Column(DateTime, nullable=True)


    citizenId = Column(String, ForeignKey('citizen_table.dni'), nullable=True)
    citizen = relationship("Citizen", back_populates="incidence")

    serenazgoId = Column(String, ForeignKey('serenazgo_table.dni'), nullable=True)
    serenazgo = relationship("Serenazgo", back_populates="incidence")
    
    districtId = Column(String, ForeignKey('district_table.alphaCode'), nullable=True)
    district = relationship("District", back_populates="incidence")

    currentStatusId = Column(String, ForeignKey('status_table.id'), nullable=True)
    currentStatus = relationship("Status", back_populates="incidence")

    typeId = Column(String, ForeignKey('incidenceType_table.id'), nullable=True)
    incidenceType = relationship("IncidenceType", back_populates="incidence")

    incidenceStatus = relationship("IncidenceStatus", back_populates="incidence")
    incidenceImage = relationship("IncidenceImage", back_populates="incidence")
