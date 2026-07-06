from pydantic import BaseModel, HttpUrl

class ProjectCreate(BaseModel):
    github_url: HttpUrl