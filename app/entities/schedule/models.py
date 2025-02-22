from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from app.entities.tasks.models import Task

from app.db import Base, int_pk


class Lesson(Base):
    id: Mapped[int_pk]
    student_id: Mapped[int]
    teacher_id: Mapped[int]
    
    start_at: Mapped[datetime]
    duration: Mapped[timedelta]

    task: Mapped["Task"] = relationship("Task", back_populates="lesson") # type: ignore

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id} date={self.start_at})"
    
    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "teacher_id": self.teacher_id,
            "start_at": self.start_at,
            "duration": self.duration,
            "task": self.task,
            }
