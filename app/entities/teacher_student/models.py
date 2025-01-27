from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column
from app.db import Base, int_pk

from sqlalchemy.orm import Mapped


class Teacher_Student(Base):
    id: Mapped[int_pk]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    __table_args__ = (UniqueConstraint('teacher_id', 'student_id', name='_person_post_uc'),
                     )
