from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.students.router import get_schedule, get_student_info, get_lesson_info

router = APIRouter(prefix='/pages', tags=["Pages"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/auth/")
async def home(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@router.get("/student/")
async def student(request: Request, students = Depends(get_student_info)):
    return templates.TemplateResponse(
        "student/student.html", 
        {"request": request,
         "students": students
         })

@router.get("/student/schedule")
async def student_schedule(request: Request, lessons = Depends(get_schedule)):
    return templates.TemplateResponse(
        "student/schedule.html", 
        {"request": request,
         "lessons": lessons,
        })

@router.get("/student/homework")
async def student_homework(request: Request, tasks = Depends(get_lesson_info)):
    return templates.TemplateResponse(
        "student/homework.html", 
        {"request": request,
         "tasks": tasks
         })

@router.get("/teacher/")
async def teacher(request: Request):
    return templates.TemplateResponse(
        "teacher/schedule.html", 
        {"request": request,
         
         })

@router.get("/teacher/submissions")
async def teacher_submissions(request: Request):
    return templates.TemplateResponse("teacher/submissions.html", {"request": request})

@router.get("/teacher/students")
async def teacher_students(request: Request):
    return templates.TemplateResponse("teacher/students.html", {"request": request})