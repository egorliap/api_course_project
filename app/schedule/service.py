from sqlalchemy.future import select
from app.db import async_session_maker
from app.service import BaseService
from sqlalchemy.orm import joinedload
from sqlalchemy import delete

from .models import Lesson


class ScheduleService(BaseService):
    model = Lesson
    
    @classmethod
    async def find_by_id(cls, lesson_id:int):
        async with async_session_maker() as session:
            query_lesson = select(cls.model).options(joinedload(cls.model.task)).filter_by(id = lesson_id)
            result_lesson = await session.execute(query_lesson)
            lesson_info = result_lesson.scalar_one_or_none
            
            if not lesson_info:
                return None
            
            lesson_data = lesson_info.to_dict()
            return lesson_data
        
    @classmethod
    async def find_all(cls, **lesson_data):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.task)).filter_by(**lesson_data)
            result = await session.execute(query)
            lesson_info = result.scalar().all()
            
            lesson_data = []
            for lesson in lesson_info:
                lesson_dict = lesson.to_dict()
                lesson_data.append(lesson_dict)
            
            return lesson_data
    
    @classmethod
    async def insert_lesson(cls, **lesson_data: dict):
        with async_session_maker() as session:
            async with session.begin():
                new_lesson = Lesson(**lesson_data)
                session.add(new_lesson)
                await session.flush()
                new_lesson_id = new_lesson.id
                await session.commit()
                return new_lesson_id
            
    @classmethod
    async def delete_lesson_by_id(cls, lesson_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id = lesson_id)
                result = await session.execute(query)
                lesson_to_delete = result.scalar_one_or_none()
                
                if not lesson_to_delete:
                    return None
                
                await session.execute(
                    delete(cls.model).filter_by(id = lesson_id)
                    )
                
                await session.commit()
                return lesson_id