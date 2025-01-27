from fastapi import APIRouter, Depends

from .dependencies import is_authorized_teacher
from .schemas import STeacher
from .service import TeacherService

from app.users.models import User

router = APIRouter(prefix='/teacher', tags=['teacher handler'])

@router.get('/info')
async def get_teacher_info(user: User = Depends(is_authorized_teacher)) -> dict:
    return user

@router.get('/schedule')
async def get_all_teacher_schedule(user: User = Depends(is_authorized_teacher)) -> dict:
    lessons = await TeacherService.find_all_lessons(user.id)
    if not lessons:
        return {
        "message": "Error getting teacher lessons"
            }
    else:
        return {
            "lessons": lessons
            }
        
@router.get('/schedule/date')
async def test():
    pass
