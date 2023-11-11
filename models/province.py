from sqlalchemy import Column, Boolean, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .region import Region

class Province(Base):
    __tablename__ = "province_table"
    alphaCode = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float, nullable=False) 
    longitude = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)


    idRegion = Column(String, ForeignKey('region_table.alphaCode'))
    region = relationship("Region", back_populates="province")

    district = relationship("District", back_populates="province")
