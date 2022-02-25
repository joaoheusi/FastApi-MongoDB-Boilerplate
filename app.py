from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from config import DOCUMENT_MODELS, MONGODB_URL
from src.auth.router import router as auth_router
from src.modules.users.routers.index import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)


@app.on_event("startup")
async def startup_event():
    """
    Initializing Beanie Database
    """

    # Whatever comes after AsyncIOMotorClient is the name of the database
    # For example AsyncIOMotorClient(MONGODB_URL).app is going to access the
    # database app
    # -----------
    # Inside document_models must go our Beanie Documents

    database = AsyncIOMotorClient(MONGODB_URL).application
    await init_beanie(database, document_models=DOCUMENT_MODELS)
