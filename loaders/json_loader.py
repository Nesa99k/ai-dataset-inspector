import json
from pathlib import Path

from models.paper import Paper


class JsonLoader:
    """
    Load AI papers from a JSON file.
    """

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def load(self) -> list[Paper]:
        """
        Read a JSON dataset and return a list of Paper objects.
        """
        try:
            with self.file_path.open(
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

                papers = []

                for item in data:
                    paper = Paper(
                        id=item["id"],
                        title=item["title"],
                        author=item["author"],
                        category=item["category"],
                        language=item["language"],
                        tags=item["tags"],
                        content=item["content"],
                        year=item["year"],
                        source=item["source"],
                        pdf_url=item["pdf_url"]
                    )
                    papers.append(paper)
                return papers
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return []
