from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.file_services import FileService

router = APIRouter()


@router.get("/projects/{project_id}/file")
def get_file(
    project_id: str,
    path: str,
    db: Session = Depends(get_db)
):

    try:

        service = FileService(db)

        return service.get_file(
            project_id=project_id,
            file_path=path
        )

    except Exception as error:

        raise HTTPException(
            status_code=404,
            detail=str(error)
        )