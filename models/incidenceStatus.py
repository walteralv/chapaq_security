from sqlalchemy import Column, Boolean, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base

class IncidenceStatus(Base):
    __tablename__ = "incidenceStatus_table"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")


    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)

    statusId = Column(String, ForeignKey('status_table.id'))
    incidenceId = Column(Integer, ForeignKey('incidence_table.id'))

    incidence = relationship("Incidence", back_populates="incidenceStatus")
    status = relationship("Status",  back_populates="incidenceStatus")
    