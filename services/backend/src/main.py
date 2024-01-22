from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from tortoise import Tortoise # NEW

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM  

# Tortoise.init_models(["src.database.models"], "models")

from src.routes import plant_diseases
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(plant_diseases.router)
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

