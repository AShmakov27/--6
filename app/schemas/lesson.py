from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from schemas.base_schema import Base

class Lesson(Base):
    _tablename__ = 'Lessons'

    id = Column(UUID(as_uuid=True), primary_key=True)
    subject = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)

    students = relationship('Student', back_populates='lesson')