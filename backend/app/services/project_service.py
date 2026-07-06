from pathlib import Path 
from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.project import Project
from app.services.git_service import GitService
from app.services.indexer_service import IndexerService

class ProjectService:
    def __init__(self,db:Session):
        self.db=db
        self.indexer = IndexerService()

    def create(self, github_url:str):
            project_id = str(uuid4())
            repo_name = github_url.rstrip("/").split("/")[-1]
            repo_name = repo_name.replace(".git","")
            clone_path = Path("repositories") / project_id
            GitService.clone(
                github_url,
                clone_path
            )

            project = Project(
                id = project_id,
                name = repo_name,
                github_url = github_url,
                local_path = str(clone_path),
                status="READY"
            )
            self.db.add(project)
            print("before commit")
            self.db.commit()
            print("after commit")
            self.db.refresh(project)

            self.indexer.index(project)

            return project
    

    def get_all(self):

        projects = self.db.query(Project).all()

        return [
            {
                "id": project.id,
                "name": project.name,
                "github_url": project.github_url,
                "status": project.status,
                "created_at": project.created_at
            }
            for project in projects
        ]