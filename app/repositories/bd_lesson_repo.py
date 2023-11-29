import traceback
from uuid import UUID 
from sqlalchemy.orm import Session 
from database import get_db
from models.lesson import Lesson
from schemas.lesson import Lesson as DBLesson 

class LessonRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def get_lessons(self) -> list[Lesson]:
        lessons = []
        for l in self.db.query(DBLesson).all():
            lessons = Lesson.from_orm(l)
        return lessons

    def get_lesson_by_id(self, id: UUID) -> Lesson:
        lesson = self.db \
            .query(DBLesson) \
            .filter(DBLesson.id == id) \
            .first()

        if lesson == None:
            raise KeyError
        return Lesson.from_orm(lesson)
    
    def create_lesson(self, lesson: Lesson) -> Lesson:
        try:
            db_lesson = DBLesson(**dict(lesson))
            self.db.add(db_lesson)
            self.db.commit()
            return Lesson.from_orm(db_lesson)
        except:
            traceback.print_exc()
            raise KeyError