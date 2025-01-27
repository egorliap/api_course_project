from pydantic import BaseModel
from app.db import async_session_maker

from app.service.base import BaseService

from .models import Task

class TaskService(BaseService):
    model = Task