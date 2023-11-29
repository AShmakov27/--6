from uuid import UUID
from pydantic import BaseModel, ConfigDict
import enum

class Statuses(enum.Enum):
    ABSENT = 'absent'
    ATTEND = 'attend'


class Student(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    FIO: str
    status: Statuses
    lesson_id: UUID