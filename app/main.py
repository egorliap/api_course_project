from fastapi import FastAPI

from app.users.router import router as router_users
from app.students.router import router as router_students


app = FastAPI()

@app.get("/")
async def home():
    return {"message":"Hw!"}

app.include_router(router_users)
app.include_router(router_students)
