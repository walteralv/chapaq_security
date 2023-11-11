from sqlalchemy import Column, Boolean, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .province import Province
from .municipality import Municipality

class District(Base):
    __tablename__ = "district_table"
    alphaCode = Column(String, primary_key=True)
    name = Column(String, index=True)
    latitude = Column(Float, nullable=False) 
    longitude = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    idProvince = Column(String, ForeignKey('province_table.alphaCode'))
    province = relationship("Province", back_populates="district" )
     
    citizen = relationship("Citizen", back_populates="district")
    municipality = relationship("Municipality", back_populates="district")
    incidence = relationship("Incidence", back_populates="district")
