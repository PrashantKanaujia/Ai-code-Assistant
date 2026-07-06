from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class RetrievalService:

    def __init__(self):
        self.embedder = EmbeddingService()
        self.store = VectorStore()

    def retrieve(self, question: str, project_id: str):

        embedding = self.embedder.embed(question)

        results = self.store.search(
            embedding=embedding,
            project_id=project_id
        )

        if not results["documents"] or not results["documents"][0]:
            return []

        output = []

        for document, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            output.append({
                "content": document,
                "metadata": metadata,
                "distance": distance,
            })

        return output