from pathlib import Path

from sqlalchemy.orm import Session

from app.models.project import Project


class FileService:

    def __init__(self, db: Session):
        self.db = db

    def get_file(self, project_id: str, file_path: str):

        project = (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if project is None:
            raise Exception("Project not found.")

        repository_path = Path(project.local_path)

        absolute_file_path = repository_path / file_path

        if not absolute_file_path.exists():
            raise Exception("File not found.")

        content = absolute_file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return {
            "file_name": absolute_file_path.name,
            "content": content
        }