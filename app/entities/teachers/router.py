import json
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.entities.students.schemas import SStudent
from app.entities.students.service import StudentService
from app.entities.teacher_student.service import Teacher_StudentService

from .dependencies import is_authorized_teacher
from .schemas import STeacher
from .service import TeacherService

from app.auth_users.models import User

router = APIRouter(prefix="/teacher", tags=["teacher handler"])


@router.get("/info/")
async def get_teacher_info(user: User = Depends(is_authorized_teacher)):
    return STeacher.model_validate(user, from_attributes=True)


@router.post("/students/add/")
async def add_student(student_id: int, user: User = Depends(is_authorized_teacher)):
    student = await StudentService.find_one_or_none_by_id(student_id)
    if student:
        try:
            new_pair = await Teacher_StudentService.insert(
                teacher_id=user.id, student_id=student_id
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="student is already added",
            )
        return Response(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="student not found"
        )


@router.get("/students/get/", response_model=List[SStudent])
async def get_all_teacher_students(user: User = Depends(is_authorized_teacher)):
    students_ids = [
        en.student_id
        for en in await Teacher_StudentService.find_all(teacher_id=user.id)
    ]

    return [
        SStudent.model_validate(m)
        for m in await StudentService.find_all_by_ids(students_ids)
    ]


@router.get("/schedule")
async def get_all_teacher_schedule(user: User = Depends(is_authorized_teacher)) -> dict:
    lessons = await TeacherService.find_all_lessons(user.id)
    if not lessons:
        return {"message": "Error getting teacher lessons"}
    else:
        return {"lessons": lessons}
