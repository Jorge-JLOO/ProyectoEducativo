from fastapi import FastAPI
from .core.config import settings  # si ya tienes settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚀 Proyecto Educativo en Railway funcionando!"}
    return {"message": "Proyecto Educativo funcionando correctamente 🚀"}
