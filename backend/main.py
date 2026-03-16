from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import task
from db.database import engine
from models.task import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task.router)
