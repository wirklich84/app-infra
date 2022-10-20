from fastapi import FastAPI
from routes.auth import router as UserAuth
from config.database import iniciar_db

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await iniciar_db()


@app.get('/')
async def home():
    return {"hola" : "Erik"}


app.include_router(UserAuth, tags=["Auth"], prefix="/auth")