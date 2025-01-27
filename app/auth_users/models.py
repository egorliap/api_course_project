from sqlalchemy import Enum, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base, str_uniq, int_pk
from app.roles import Role


class User(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str_uniq]
    password: Mapped[str]

    user_role: Mapped[str] = mapped_column(Enum(Role), server_default=Role.GUEST)

    extend_existing = True
