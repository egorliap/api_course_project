from typing import List
from sqlalchemy.future import select

from app.auth_users.models import User
from app.db import async_session_maker
from app.roles import Role
from app.service import BaseService
from ..schedule.models import Lesson


class StudentService(BaseService):
    model = User

    @classmethod
    async def find_all(cls, **filter_by) -> List[User]:
        return await super().find_all(**filter_by, user_role=Role.STUDENT)

    @classmethod
    async def find_all_by_ids(cls, ids: List[int]) -> List[User]:
        return await super().find_all_by_ids(ids, user_role=Role.STUDENT)

    @classmethod
    async def find_lessons_between_dates_for_student(
        cls, student_id, date_from, date_to
    ) -> List[Lesson]:
        async with async_session_maker() as session:
            query = select(Lesson).filter(
                Lesson.start_at.between(date_from, date_to),
                Lesson.student_id == student_id,
            )
            items = await session.execute(query)
            return items.scalars().all()
