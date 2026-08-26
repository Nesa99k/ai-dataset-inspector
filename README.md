# AI Dataset Explorer

A Python project for loading, validating, analyzing, and exporting AI research paper datasets.

The project demonstrates object-oriented programming, file handling, dataset inspection, and clean project architecture using real research papers collected from the arXiv API.

---

## Features

- Load AI research papers from JSON
- Support loading datasets from JSON and CSV
- Dataset validation
- Search papers by title
- Filter recent papers
- Browse categories
- Generate statistics
- Export reports to JSON and CSV
- Application logging
- Configuration via JSON

---

## Project Structure

```
ai_dataset_inspector/

├── config/
├── data/
├── exports/
├── loaders/
├── logs/
├── managers/
├── models/
├── utils/
├── main.py
├── README.md
└── requirements.txt
```

---

## System Architecture & Workflow

<img src="docs/architecture.svg" alt="System Architecture & Workflow" width="700">

---

## Technologies

- Python 3.11+
- Dataclasses
- pathlib
- JSON
- CSV
- Logging
- Type Hints
- Object-Oriented Programming
- Functional Programming Concepts

---

## Dataset

The dataset was collected using the official arXiv API.

Topics include:

- Transformers
- Large Language Models
- Retrieval-Augmented Generation
- Computer Vision
- Reinforcement Learning
- Diffusion Models
- Multimodal AI

---

## Example Output

```
Dataset validation passed.

Dataset Statistics

papers: 21
categories: 10
languages: 1
newest_year: 2026
oldest_year: 2011
```

---

## Skills Demonstrated

This project demonstrates practical use of:

- Classes and Objects
- Dataclasses
- Object-Oriented Programming
- Type Hints
- Modular Project Architecture
- JSON and CSV Processing
- File Handling with pathlib
- Exception Handling
- Logging
- Static Methods
- List and Set Comprehensions
- Lambda Functions
- filter()
- sorted()
- Generators

---

## Author

Nesa Karimi
