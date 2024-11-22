from datetime import datetime, date
from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.users.models import User
from app.schedule.models import Lesson
#from .schemas import 
from .service import StudentService
from .dependencies import is_authorized_student


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
    return user

@router.post("/lesson/solution")
async def get_lesson_info(lesson_id: int, user: User = Depends(is_authorized_student)):
    return user
