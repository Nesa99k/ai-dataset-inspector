from pathlib import Path
import json

from loaders.json_loader import JsonLoader
from managers.dataset_inspector import DatasetInspector
from utils.exporter import Exporter
from utils.file_utils import FileUtils
from utils.logger import Logger


def main():
    BASE_DIR = Path(__file__).parent

    # ----------------Load configuration-----------
    config_path = BASE_DIR / "config" / "config.json"
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    export_dir = BASE_DIR / config["export_directory"]
    log_dir = BASE_DIR / config["log_directory"]
    data_file = BASE_DIR / "data" / "papers.json"

# ----------------Create directories-----------
    FileUtils.create_directory(export_dir)
    FileUtils.create_directory(log_dir)


# --------------Create logger--------------------

    logger = Logger.get_logger(log_dir)
    logger.info("Application started.")


# ----------------Load dataset------------------
    loader = JsonLoader(data_file)
    papers = loader.load()

    logger.info(f"{len(papers)} papers loaded.")

# ---------------- Inspector--------------------
    inspector = DatasetInspector(papers)

# ----------------Validate Dataset--------------

    errors = inspector.validate_dataset()

    if errors:
        print("\nDataset Validation Errors")
        print("-" * 40)

        for error in errors:
            print(error)
        logger.warning("Dataset contains validation errors.")
    else:
        print("\nDataset validation passed.")
        logger.info("Dataset validation passed.")

# ----------------Show statistics--------------------

    stats = inspector.statistics()
    print("\nDataset Statistics")
    print("-" * 40)

    for key, value in stats.items():
        print(f"{key:<15}:{value}")
    logger.info("Statistics generated.")

# ----------------Recent Papers-------------------
    print("\nRecent Papers")

    print("-" * 40)
    recent = inspector.recent_papers(
        config["recent_year"]
    )
    for paper in recent[:config["top_results"]]:
        print(paper.summary())

# ----------------Categories----------------------
    print("\nCategories")

    print("-" * 40)
    for category in inspector.papers_by_category():
        print(category)
# ----------------Generator Demo------------------
    print("\nFirst Five Titles")

    print("-" * 40)
    for title in list(inspector.titles())[:5]:
        print(title)
        print("\n")

# --------------languages---------------------------
    print("\nLanguages")

    print("-" * 40)

    for language in list(inspector.languages())[:]:
        print(language)

# ----------------Export reports-------------------
    Exporter.export_to_json(
        recent,
        export_dir/"recent_papers.json"
    )
    Exporter.export_titles_to_csv(
        papers,
        export_dir/"papers.csv"
    )
    logger.info("Reports exported.")
    print("\nReports exported successfully.")
    logger.info("Program finished.")


if __name__ == "__main__":
    main()
