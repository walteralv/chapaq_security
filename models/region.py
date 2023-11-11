from sqlalchemy import Column, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .country import Country

class Region(Base):
    __tablename__ = "region_table"
    alphaCode = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    numCode = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)


    idCountry = Column(String, ForeignKey('country_table.alphaCode'))
    country = relationship("Country", back_populates="region")
    
    province = relationship("Province", back_populates="region")
