import chromadb


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="vector_db")

        self.collection = self.client.get_or_create_collection(
            name="repository_chunks"
        )

    def add_chunk(
        self,
        chunk_id: str,
        content: str,
        embedding: list[float],
        metadata: dict
    ):

        self.collection.add(
            ids=[chunk_id],
            documents=[content],
            embeddings=[embedding],
            metadatas=[metadata]
        )
    

    def search(self, embedding, project_id: str):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=5,
            where={
                "project_id": project_id
            }
        )