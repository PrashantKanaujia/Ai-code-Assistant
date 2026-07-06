from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.project_service import ProjectService
from app.schemas.project import ProjectCreate

router = APIRouter()


@router.post("/projects")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    service = ProjectService(db)
    return service.create(str(project.github_url))


@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db)
):
    service = ProjectService(db)
    return service.get_all()