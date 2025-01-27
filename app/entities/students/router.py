from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends

from app.auth_users.models import User
from app.entities.teacher_student.service import Teacher_StudentService
from app.entities.teachers.schemas import STeacher
from app.entities.teachers.service import TeacherService
from ..schedule.models import Lesson

from .service import StudentService
from .dependencies import is_authorized_student
from .schemas import SStudent


router = APIRouter(prefix='/students', tags=["Students"], dependencies=[])

@router.get("/schedule/")
async def get_schedule(date_from: datetime = datetime.now(), 
                       date_to: datetime = datetime.now(), 
                       user: User = Depends(is_authorized_student)):
    lessons = await StudentService.find_lessons_between_dates_for_student(user.id, date_from, date_to)
    lessons.sort(key=lambda x: x.start_at)
    structured_lessons = {}
    
    for lesson in lessons:
        if lesson.start_at.date() in structured_lessons.keys():
            structured_lessons[lesson.start_at.date()].append(lesson)
        else:
            structured_lessons[lesson.start_at.date()] = [lesson]
    
    return structured_lessons

@router.get("/info/")
async def get_student_info(user: User = Depends(is_authorized_student)):
    return SStudent.model_validate(user, from_attributes=True)

@router.get("/teachers/get/", response_model=List[STeacher])
async def get_teachers(user: User = Depends(is_authorized_student)):
    teachers_ids = [
        en.teacher_id
        for en in await Teacher_StudentService.find_all(student_id=user.id)
    ]

    return [
        STeacher.model_validate(m)
        for m in await TeacherService.find_all_by_ids(teachers_ids)
    ]