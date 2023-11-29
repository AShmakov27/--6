from uuid import UUID
from models.lesson import Lesson
from models.student import Student
from models.student import Statuses

lessons: list[Lesson] = []

class LessonRepo():
    def get_lessons() -> list[Lesson]:
        return lessons
    
    def get_lesson_by_id(self, id: UUID) -> Lesson:
        for l in lessons:
            if l.id == id:
                return l
            
        raise KeyError
    
    def create_lesson(self, lesson: Lesson) -> Lesson:
        if len([l for l in lessons if l.id == lesson.id]) > 0:
            raise KeyError
        
        lessons.append(lesson)
        return lesson
    