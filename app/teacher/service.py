from typing import List
from sqlalchemy.future import select

from app.db import async_session_maker
from app.service import BaseService
from app.schedule.models import Lesson


class TeacherService(BaseService):
    @classmethod
    async def find_lessons_between_dates_for_teacher(cls, teacher_id, date_from, date_to) -> List[Lesson]:
        async with async_session_maker() as session:
            query = select(Lesson).filter(Lesson.start_at.between(date_from, date_to), 
                                          Lesson.teacher_id == teacher_id)
            items = await session.execute(query)
            return items.scalars().all()
        
    @classmethod
    async def find_all_lessons(cls, teacher_id) -> List[Lesson]:
        async with async_session_maker as session:
            query = select(Lesson).filter(Lesson.teacher_id == teacher_id)
            items = await session.execute(query)
            return items.scalars().all()