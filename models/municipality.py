from sqlalchemy import Column, Boolean, String, DateTime, Date , ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base


class Municipality(Base):
    __tablename__ = "municipality_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)
    
    districtId = Column(String, ForeignKey('district_table.alphaCode'))
    district = relationship("District", back_populates="municipality")

    serenazgo = relationship("Serenazgo", back_populates="municipality")
    schedule = relationship("Schedule", back_populates="municipality")
