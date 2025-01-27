from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.users.router import router as router_users
from app.students.router import router as router_students
from app.schedule.router import router as router_schedule
from app.tasks.router import router as router_tasks
from app.teacher.router import router as router_teacher
from app.pages.router import router as router_pages


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def home():
    return {"message":"Hw!"}

templates = Jinja2Templates(directory="app/templates")

@app.exception_handler(404)
async def custom_404_handler(request, __):
    return templates.TemplateResponse("404.html", {"request" : request})

app.include_router(router_users)
app.include_router(router_students)
app.include_router(router_pages)
app.include_router(router_schedule)
app.include_router(router_tasks)
app.include_router(router_teacher)