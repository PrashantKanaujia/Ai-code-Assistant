from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".pytest_cache",
    ".mypy_cache"
}

IGNORE_FILES = {
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "poetry.lock",
    ".DS_Store"
}

IGNORE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".pdf",
    ".exe",
    ".dll",
    ".pyc",
    ".class",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".mp3",
    ".mp4",
    ".mov"
}


class RepositoryIndexer:

    def scan(self, repository_path: str) -> list[Path]:
        repository = Path(repository_path)

        files = []

        for file in repository.rglob("*"):

            if not file.is_file():
                continue

            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            if file.name in IGNORE_FILES:
                continue

            if file.suffix.lower() in IGNORE_EXTENSIONS:
                continue


            files.append(file)

        return files

    def read_file(self, file_path: Path) -> str:
        try:
            return file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except Exception as e:
            print(f"Failed to read {file_path}: {e}")
            return ""
    

    def detect_language(self, file_path: str) -> str:

        suffix = Path(file_path).suffix.lower()

        mapping = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".tsx": "tsx",
            ".jsx": "jsx",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".cs": "csharp",
            ".go": "go",
            ".rs": "rust",
            ".php": "php",
            ".rb": "ruby",
            ".html": "html",
            ".css": "css",
            ".scss": "scss",
            ".json": "json",
            ".yaml": "yaml",
            ".yml": "yaml",
            ".xml": "xml",
            ".md": "markdown",
            ".txt": "text",
            ".sql": "sql",
            ".sh": "shell",
            ".ejs": "ejs"
        }

        return mapping.get(suffix, "unknown")