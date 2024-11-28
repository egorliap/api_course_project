from sqlalchemy.future import select

from app.db import async_session_maker
from app.service import BaseService
from .models import User


class UserService(BaseService):
    model = User
    