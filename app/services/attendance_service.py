from uuid import UUID
from datetime import datetime
from models.student import Student, Statuses
from models.lesson import Lesson
from repositories.local_lesson_repo import LessonRepo
from repositories.local_student_repo import StudentRepo

class AttendanceService():
    lesson_repo: LessonRepo
    student_repo: StudentRepo

    def __init__(self) -> None:
        self.lesson_repo = LessonRepo()
        self.student_repo = StudentRepo()

    def get_lessons(self) -> list[Lesson]:
        return self.lesson_repo.get_lessons()
    
    def create_lesson(self, id: UUID, date: datetime, subject: str) -> Lesson:
        lesson = Lesson(id=id, date=date, subject=subject)
        return self.lesson_repo.create_lesson(lesson=lesson)
    
    def create_student(self, id: UUID, FIO: str) -> Student:
        student = Student(id=id, FIO=FIO)
        return self.student_repo.create_student(student=student)

    def add_student_to_lesson(self, lesson_id: UUID, student_id: UUID) -> Lesson:
        lesson = self.lesson_repo.get_lesson_by_id(lesson_id)
        try:
            student = self.student_repo.get_student_by_id(student_id)
        except KeyError:
            raise ValueError
        lesson.students.append(student)
        return self.lesson_repo.add_student_to_lesson(lesson)
    
    def set_absent(self, lesson_id: UUID, student_id: UUID) -> Lesson:
        lesson = self.lesson_repo.get_lesson_by_id(lesson_id)
        for s in lesson.students:
            if s.id == student_id:
                student = s
        student.status = Statuses.ABSENT
        return self.lesson_repo.set_student_status_at_lesson(lesson=lesson, student=student)
    
    def set_attend(self, lesson_id: UUID, student_id: UUID) -> Lesson:
        lesson = self.lesson_repo.get_lesson_by_id(lesson_id)
        for s in lesson.students:
            if s.id == student_id:
                student = s
        student.status = Statuses.ATTEND
        return self.lesson_repo.set_student_status_at_lesson(lesson=lesson, student=student)