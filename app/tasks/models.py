from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base, int_pk


class Task(Base):
    id: Mapped[int_pk]
    given: Mapped[datetime]
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    
    lesson: Mapped["Lesson"] = relationship("Lesson", back_populates="lessons") # type: ignore

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id} date={self.start_at})"
