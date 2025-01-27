from typing import Literal
from pydantic import BaseModel, EmailStr, Field

from app.roles import Role


class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(
        ..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков"
    )
    first_name: str = Field(
        ..., min_length=3, max_length=50, description="Имя, от 3 до 50 символов"
    )
    last_name: str = Field(
        ..., min_length=3, max_length=50, description="Фамилия, от 3 до 50 символов"
    )
    user_role: Role


class SUserAuth(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(
        ..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков"
    )
