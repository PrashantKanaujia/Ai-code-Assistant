from app.services.llm_service import LLMService

llm = LLMService()

print(
    llm.generate(
        "What is FastAPI?"
    )
)