from pathlib import Path


class FileUtils:
    """
    Utility functions for working with files and directories.
    """
    @staticmethod
    def create_directory(path: str) -> None:
        """
        Create a directory if it does not exist.
        """
        Path(path).mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def file_exists(path: str) -> bool:
        """
        Check whether a file exists.
        """
        return Path(path).exists()
