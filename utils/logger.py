import logging
from pathlib import Path


class Logger:
    """
    Configure and return the application logger.
    """
    @staticmethod
    def get_logger(log_directory: Path) -> logging.Logger:

        log_directory.mkdir(
            exist_ok=True
        )
        logging.basicConfig(
            filename=log_directory / "app.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        return logging.getLogger("AI Dataset Inspector")
