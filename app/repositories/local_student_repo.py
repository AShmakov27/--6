from uuid import UUID
from models.student import Student

students: list[Student] = []

class StudentRepo():
    def get_students(self) -> list[Student]:
        return students
    
    def get_student_by_id(self, id: UUID) -> Student:
        for s in students:
            if s.id == id:
                return s
            
        raise KeyError
    
    def create_student(self, student: Student) -> Student:
        if len([s for s in students if s.id == student.id]) > 0:
            raise KeyError
        
        students.append(student)
        return student
    
    def set_status(self, student: Student) -> Student:
        for s in students:
            if s.id == student.id:
                s.status = student.status
                break

        return student
    
    def add_student_to_lesson(self, student: Student, lesson_id: UUID) -> Student:
        for s in students:
            if s.id == student.id:
                s.lesson_id = lesson_id
                return s
            
        raise KeyError
