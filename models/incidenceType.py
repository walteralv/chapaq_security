from sqlalchemy import Column, Boolean, String, DateTime, Date, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base

class IncidenceType(Base):
    __tablename__ = "incidenceType_table"

    id = Column(String, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    priorityValue = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    incidence = relationship("Incidence", back_populates="incidenceType")
