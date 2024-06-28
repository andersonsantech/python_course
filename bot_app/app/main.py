from fastapi import FastAPI
from app.controllers.user_controller import router as user_controller

app = FastAPI()

app.include_router(user_controller, prefix="/api")