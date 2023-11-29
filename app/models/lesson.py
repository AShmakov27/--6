from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from .student import Student

class Lesson(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    subject: str
    date: datetime