from pathlib import Path

from sqlalchemy.orm import Session

from app.models.project import Project
from app.services.repository_indexer import RepositoryIndexer


class RepositoryExplorerService:

    def __init__(self, db: Session):

        self.db = db
        self.scanner = RepositoryIndexer()

    def get_files(self, project_id: str):

        project = (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if project is None:
            raise Exception("Project not found.")

        files = self.scanner.scan(project.local_path)

        return [

            {
                "path": str(
                    file.relative_to(project.local_path).as_posix()
                )
            }

            for file in files

        ]