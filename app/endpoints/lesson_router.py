from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from services.attendance_service import AttendanceService
from models.lesson import Lesson

lesson_router = APIRouter(prefix='/lesson', tags=['lesson'])

@lesson_router.get('/')
def get_lessons(attendance_service: AttendanceService = Depends(AttendanceService)) -> list[Lesson]:
    return attendance_service.get_lessons()


@lesson_router.post('/{lesson_id}/{student_id}/add')
def add_student_to_lesson(lesson_id: UUID, student_id: UUID, attendance_service: AttendanceService = Depends(AttendanceService)) -> Lesson:
    try:
        lesson = attendance_service.add_student_to_lesson(lesson_id=lesson_id, student_id=student_id)
        return lesson.dict()
    except KeyError:
        raise HTTPException(404, f'Lesson with id={lesson_id} not found')
    except ValueError:
        raise HTTPException(400, f'Student with id={student_id} can\'t be added')


@lesson_router.post('/{lesson_id}/{student_id}/absent')
def set_absent(lesson_id: UUID, student_id: UUID, attendance_service: AttendanceService = Depends(AttendanceService)) -> Lesson:
    try:
        lesson = attendance_service.set_absent(lesson_id=lesson_id, student_id=student_id)
        return lesson.dict()
    except KeyError:
        raise HTTPException(404, f'Lesson with id={lesson_id} not found')
    except ValueError:
        raise HTTPException(400, f'Student with id={student_id} can\'t be marked as absent')


@lesson_router.post('/{lesson_id}/{student_id}/attend')
def set_attend(lesson_id: UUID, student_id: UUID, attendance_service: AttendanceService = Depends(AttendanceService)) -> Lesson:
    try:
        lesson = attendance_service.set_attend(lesson_id=lesson_id, student_id=student_id)
        return lesson.dict()
    except KeyError:
        raise HTTPException(404, f'Lesson with id={lesson_id} not found')
    except ValueError:
        raise HTTPException(400, f'Student with id={student_id} can\'t be marked as attend')
    
