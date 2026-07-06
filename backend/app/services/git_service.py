from pathlib import Path
from git import Repo


class GitService:

    @staticmethod
    def clone(url: str, destination: Path):
        destination.parent.mkdir(parents=True, exist_ok=True)

        Repo.clone_from(url, destination)