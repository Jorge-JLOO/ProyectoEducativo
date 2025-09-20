from fastapi import FastAPI
from backend.app.core.config import settings
from backend.app.db.session import engine
from sqlmodel import SQLModel
from backend.app.api.routers import auth, users, students, payments

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(students.router)
app.include_router(payments.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def root():
    return {"message": "ProyectoEducativo API"}
