from sqlalchemy import Column, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base

class Country(Base):
    __tablename__ = "country_table"

    alphaCode = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    numCode = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)
    
    region = relationship("Region", back_populates="country")
    