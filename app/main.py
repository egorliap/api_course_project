from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.auth_users.router import router as router_users
from app.entities import schedule_router, student_router, tasks_router, teacher_router
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
app.include_router(student_router)
app.include_router(router_pages)
app.include_router(schedule_router)
app.include_router(tasks_router)
app.include_router(teacher_router)