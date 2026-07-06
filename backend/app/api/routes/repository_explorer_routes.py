from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.repository_explorer_service import RepositoryExplorerService

router = APIRouter()


@router.get("/projects/{project_id}/files")
def get_repository_files(

    project_id: str,

    db: Session = Depends(get_db)

):

    try:

        service = RepositoryExplorerService(db)

        return service.get_files(project_id)

    except Exception as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )