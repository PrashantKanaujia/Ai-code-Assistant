import uuid

from app.services.repository_indexer import RepositoryIndexer
from app.services.text_chunker import TextChunker
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class IndexerService:

    def __init__(self):

        self.scanner = RepositoryIndexer()
        self.chunker = TextChunker()
        self.embedder = EmbeddingService()
        self.vector_store = VectorStore()

    def index(self, project):

        files = self.scanner.scan(project.local_path)

        for file in files:

            content = self.scanner.read_file(file)

            if not content.strip():
                continue

            chunks = self.chunker.chunk(content)
            language = self.scanner.detect_language(file)

            for i, chunk in enumerate(chunks):

                embedding = self.embedder.embed(
                    chunk["content"]
                )

                self.vector_store.add_chunk(

                    chunk_id=str(uuid.uuid4()),

                    content=chunk["content"],

                    embedding=embedding,

                    metadata={

                        "project_id": project.id,

                        "file_path": str(
                            file.relative_to(project.local_path).as_posix()
                        ),

                        "chunk": i,

                        "language": language,

                        "start_line": chunk["start_line"],

                        "end_line": chunk["end_line"]

                    }
                )