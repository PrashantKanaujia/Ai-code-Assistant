class TextChunker:

    def chunk(self, text, lines_per_chunk=40):

        lines = text.splitlines()

        chunks = []

        for i in range(0, len(lines), lines_per_chunk):

            chunk_lines = lines[i:i + lines_per_chunk]

            chunks.append({

                "content": "\n".join(chunk_lines),

                "start_line": i + 1,

                "end_line": min(i + lines_per_chunk, len(lines))

            })

        return chunks