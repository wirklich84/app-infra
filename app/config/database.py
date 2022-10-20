from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.auth import User
import os


async def iniciar_db():
    client = AsyncIOMotorClient(os.environ["DB_URL"])
    await init_beanie(database=client.monitoreo_infra, document_models=[User])

