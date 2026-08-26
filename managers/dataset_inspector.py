from models.paper import Paper


class DatasetInspector:
    """
    Analyze and validate a collection of AI research papers.
    """

    def __init__(self, papers: list[Paper]):
        self.papers = papers

# -------------- paper_count---------------------------
    def paper_count(self) -> int:
        """
        Return the total number of papers.
        """
        return len(self.papers)

# -------------- all unique categories---------------------------

    def categories(self) -> list[str]:
        """
        Return all unique categories.
        """

        return sorted({
            paper.category
            for paper in self.papers
        })

# --------------languages---------------------------

    def languages(self) -> list[str]:
        """
        Return available languages.
        """
        return sorted({
            paper.language for paper in self.papers
        })

# --------------paper by title---------------------------

    def search_by_title(self, title: str) -> Paper | None:
        """
        Search for a paper by title.
        """
        for paper in self.papers:
            if paper.title.lower() == title.lower():
                return paper

        return None

# --------------sorted by publication year------------------

    def newest_papers(self) -> list[Paper]:
        """
        Return papers sorted by publication year.
        """
        return sorted(
            self.papers,
            key=lambda paper: paper.year,
            reverse=True
        )
# --------------filter papers------------------

    def recent_papers(
        self,
        year: int,
    ) -> list[Paper]:
        """
        Return papers published after a given year.
        """
        return list(
            filter(
                lambda paper: paper.is_published_after(year),
                self.papers
            )
        )
# --------------Search by category------------------

    def papers_by_category(self, category: str) -> list[Paper]:

        return [
            paper for paper in self.papers
            if paper.category.lower() == category.lower()
        ]
# --------------Search by tag------------------

    def papers_with_tag(self, tag: str) -> list[Paper]:
        return [
            paper for paper in self.papers
            if paper.has_tag(tag)
        ]

# --------------Search by author------------------

    def papers_by_author(self, author: str) -> list[Paper]:
        return [
            paper for paper in self.papers
            if paper.has_author(author)
        ]

# --------------Generator------------------

    def titles(self):
        """
        Yield paper titles.
        """
        for paper in self.papers:
            yield paper.title

# --------------Project Statistics------------------

    def statistics(self) -> dict:
        """
        Return dataset statistics.
        """

        return {

            "papers": self.paper_count(),

            "categories":
            len(self.categories()),

            "languages":
            len(self.languages()),

            "newest_year":
            max(
                paper.year
                for paper in self.papers
            ),

            "oldest_year":
            min(
                paper.year
                for paper in self.papers
            )
        }
# --------------Dataset Validation------------------

    def validate_dataset(self) -> list[str]:
        """
        Validate dataset content.
        """

        errors = []

        for paper in self.papers:
            if not paper.title.strip():
                errors.append(
                    f"Paper {paper.id} has no title."
                )

            if not paper.content.strip():
                errors.append(
                    f"Paper {paper.id} has no abstract."
                )
            if paper.year <= 0:
                errors.append(
                    f"Paper {paper.id} has invalid year."
                )
            if not paper.pdf_url.strip():
                errors.append(
                    f"Paper {paper.id} has no PDF URL."
                )
        return errors
