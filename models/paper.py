from dataclasses import dataclass, field


@dataclass
class Paper:
    id: int
    title: str
    author: str
    category: str
    language: str
    tags: list[str] = field(default_factory=list)
    content: str = ""
    year: int = 0
    source: str = ""
    pdf_url: str = ""

    def summary(self) -> str:
        """
        Return a short summary of the paper.
        """

        return f"[{self.id}] {self.title} ({self.year})"

    def abstract_word_count(self) -> int:
        """
        Return the number of words in the abstract.
        """

        return len(self.content.split())

    def has_tag(self, tag: str) -> bool:
        """
        Check whether the paper contains the given tag.
        """

        return tag in self.tags

    def has_author(self, author: str) -> bool:
        """
        Check whether the given author contributed to the paper.
        """

        return author.lower() in self.author.lower()

    def is_published_after(self, year: int) -> bool:
        """
        Return True if the paper was published after the given year.
        """

        return self.year >= year

    def author_count(self) -> int:
        """
        Return the number of authors.
        """

        return len(self.author.split(","))

    def short_title(self, max_length: int = 60) -> str:
        """
        Return a shortened title.
        """

        if len(self.title) <= max_length:
            return self.title
        return self.title[:max_length] + "...."
