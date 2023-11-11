from sqlalchemy import Column, Boolean, String, DateTime, Date, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.mysql import  Base

class IncidenceImage(Base):
    __tablename__ = "incidence_image_table"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    url = Column(String, nullable=False)
    
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)
    
    incidenceId = Column(Integer, ForeignKey('incidence_table.id'))
    incidence = relationship("Incidence", back_populates="incidenceImage")
    