from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.project import Project   # Import the model
from app.api.routes.ai_routes import router as ai_router

from app.api.routes.project_routes import router as project_router

from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.file_routes import router as file_router
from app.api.routes.repository_explorer_routes import (
    router as repository_explorer_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Repository Engineer"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(project_router)
app.include_router(ai_router)
app.include_router(file_router)
app.include_router(repository_explorer_router)

@app.get("/")
def root():
    return {"message": "Backend is running"}