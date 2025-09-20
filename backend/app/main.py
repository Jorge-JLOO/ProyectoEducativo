from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine
from sqlmodel import SQLModel
from backend.app.api.routers import auth, users, students, payments

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION))

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(students.router)
app.include_router(payments.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@

@app.get("/")
def read_root():
    return {"message": "Proyecto Educativo funcionando correctamente 🚀"}
