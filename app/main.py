from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.users.router import router as router_users
from app.students.router import router as router_students
from app.pages.router import router as router_pages


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def home():
    return {"message":"Hw!"}

app.include_router(router_users)
app.include_router(router_students)
app.include_router(router_pages)
