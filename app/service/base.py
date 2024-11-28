from typing import Annotated, Type
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from app.db import async_session_maker


class BaseService:
    model = None
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            items = await session.execute(query)
            return items.scalars().all()
    
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            students = await session.execute(query)
            return students.scalars().one_or_none()
    
    @classmethod
    async def insert(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return new_instance
