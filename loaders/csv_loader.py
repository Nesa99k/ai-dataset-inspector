import csv
from pathlib import Path
from models.paper import Paper


class CsvLoader:
    """
    Load AI papers from a CSV file.
    """

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def load(self) -> list[Paper]:
        """
        Read a CSV dataset and return a list of Paper objects.
        """
        try:

            with self.file_path.open(
                "r",
                newline="",
                encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)

                papers = []

                for row in reader:
                    paper = Paper(
                        id=int(row["id"]),

                        title=row["title"],

                        author=row["author"],

                        category=row["category"],

                        language=row["language"],

                        tags=row["tags"].split(","),

                        content=row["content"],

                        year=int(row["year"]),

                        source=row["source"],

                        pdf_url=row["pdf_url"]
                    )
                    papers.append(paper)
                return papers
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
