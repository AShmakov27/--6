from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from schemas.base_schema import Base
from models.student import Statuses

class Student(Base):
    __tablename__ = 'Students'

    id = Column(UUID(as_uuid=True), primary_key=True)
    FIO = Column(String, nullable=False)
    status = Column(Enum(Statuses), nullable=False)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey('Lessons.id'))

    lesson = relationship('Lesson', back_populates='students')