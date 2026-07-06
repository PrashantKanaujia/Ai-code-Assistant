from pydantic import BaseModel

class AskRequest(BaseModel):
    project_id: str
    question: str



class AskResponse(BaseModel):
    answer: str
    sources: list[dict]