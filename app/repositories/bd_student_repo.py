import traceback
from uuid import UUID 
from sqlalchemy.orm import Session 
from database import get_db
from models.student import Student
from schemas.student import Student as DBStudent

class StudentRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def get_students(self) -> list[Student]:
        students = []
        for l in self.db.query(DBStudent).all():
            students = Student.from_orm(l)
        return students

    def get_lesson_by_id(self, id: UUID) -> Student:
        student = self.db \
            .query(DBStudent) \
            .filter(DBStudent.id == id) \
            .first()

        if student == None:
            raise KeyError
        return Student.from_orm(student)
    
    def create_lesson(self, student: Student) -> Student:
        try:
            db_student = DBStudent(**dict(student))
            self.db.add(db_student)
            self.db.commit()
            return Student.from_orm(db_student)
        except:
            traceback.print_exc()
            raise KeyError
        
    def set_status(self, student: Student) -> Student:
        db_student = self.db.query(DBStudent).filter(DBStudent.id == student.id).first()
        db_student.status = student.status
        self.db.commit()
        return Student.from_orm(db_student)
    
    def add_student_to_lesson(self, student: Student) -> Student:
        db_student = self.db.query(DBStudent).filter(DBStudent.id == student.id).first()
        db_student.lesson_id = student.lesson_id
        self.db.commit()
        return Student.from_orm(db_student)