from app.entities.teacher_student.models import Teacher_Student
from app.service.base import BaseService


class Teacher_StudentService(BaseService):
    model = Teacher_Student
