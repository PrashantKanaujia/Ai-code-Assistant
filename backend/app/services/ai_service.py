from app.services.retrieval_service import RetrievalService
from app.services.prompt_builder import PromptBuilder
from app.services.llm_service import LLMService


class AIService:

    def __init__(self):
        self.retrieval = RetrievalService()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMService()

    def ask(self, question: str, project_id: str):

        retrieved_chunks = self.retrieval.retrieve(
            question=question,
            project_id=project_id
        )

        prompt = self.prompt_builder.build_context(
            retrieved_chunks=retrieved_chunks,
            question=question
        )

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": [
                {
                    "file_path": chunk["metadata"]["file_path"],
                    "language": chunk["metadata"]["language"],
                    "chunk": chunk["metadata"]["chunk"],
                    "start_line": chunk["metadata"]["start_line"],
                    "end_line": chunk["metadata"]["end_line"],
                    "distance": chunk["distance"]
                }
                for chunk in retrieved_chunks
            ]
        }