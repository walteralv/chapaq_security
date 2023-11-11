from sqlalchemy import Column, Boolean, String, DateTime, Date , ForeignKey, Integer, Time
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base
from .municipality import Municipality

class Schedule(Base):
    __tablename__ = "schedule_table"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name =  Column(String,  unique=True, nullable=False)
    entryTime =  Column(Time, nullable=False)
    departureTime =  Column(Time, nullable=False)

    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    municipalityId = Column(Integer, ForeignKey('municipality_table.id'))
    municipality = relationship("Municipality", back_populates="schedule")
    
    serenazgo = relationship("Serenazgo", back_populates="schedule")
