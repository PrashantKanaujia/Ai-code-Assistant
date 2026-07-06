class PromptBuilder:

    def build_context(self, retrieved_chunks: list, question: str) -> str:

        context = ""

        for chunk_data in retrieved_chunks:

            context += f"""
            [FILE]: {chunk_data['metadata']['file_path']}
            [LANG]: {chunk_data['metadata']['language']}
            [CHUNK]: {chunk_data['metadata']['chunk']}

            [CODE]:
            {chunk_data['content']}
            ------------------------------
            """

        prompt = f"""
You are a senior software engineer analyzing a codebase.

STRICT RULES:
- Use ONLY the provided repository context.
- Do NOT guess or assume missing code.
- If information is missing, say:
  "I could not find this in the repository."

When explaining:
- Be precise
- Reference file names when possible
- If code flow is involved, explain step-by-step

---

REPOSITORY CONTEXT:
{context}

---

QUESTION:
{question}
"""

        return prompt