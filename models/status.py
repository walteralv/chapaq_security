from sqlalchemy import Column, Boolean, String, DateTime
from datetime import datetime
from db.mysql import  Base
from sqlalchemy.orm import relationship


class Status(Base):
    __tablename__ = "status_table"
    id = Column(String, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    incidence = relationship("Incidence", back_populates="currentStatus")
    incidenceStatus = relationship("IncidenceStatus", back_populates="status")
