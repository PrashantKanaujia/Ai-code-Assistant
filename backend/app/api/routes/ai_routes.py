# app/api/routes/ai_routes.py

from fastapi import APIRouter
from app.schemas.ask_schema import AskRequest, AskResponse
from app.services.ai_service import AIService

router = APIRouter()
service = AIService()


@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):

    result = service.ask(
        question=payload.question,
        project_id=payload.project_id
    )

    return result