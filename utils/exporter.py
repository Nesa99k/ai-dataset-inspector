import json
import csv

from models.paper import Paper


class Exporter:
    """
    Export paper collections to different file formats.
    """

    @staticmethod
    def export_to_json(
        papers: list[Paper],
        output_path: str
    ) -> None:

        data = [
            paper.__dict__
            for paper in papers
        ]

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def export_titles_to_csv(
        papers: list[Paper],
        output_path: str
    ) -> None:

        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Title", "Year"]
            )

            for paper in papers:

                writer.writerow(
                    [
                        paper.title,
                        paper.year
                    ]
                )
