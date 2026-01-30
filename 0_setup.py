from pathlib import Path
import nbformat
from nbformat.v4 import new_notebook

# Root project folder
PROJECT_ROOT = Path.cwd()

# Folder structure
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "reports/figures"
]

# Files to create
py_files = [
    "src/metrics.py",
    "src/stats_tests.py",
    "src/power_analysis.py",
    "src/plotting.py",
]

other_files = [
    "README.md",
    "requirements.txt",
    "reports/executive_summary.md"
]

notebooks = [
    "notebooks/01_data_validation.ipynb",
    "notebooks/02_experiment_design.ipynb",
    "notebooks/03_statistical_testing.ipynb",
    "notebooks/04_results_and_recommendations.ipynb"
]

def create_folders():
    for folder in folders:
        path = PROJECT_ROOT / folder
        path.mkdir(parents=True, exist_ok=True)


def create_py_and_md_files():
    for file in py_files + other_files:
        path = PROJECT_ROOT / file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)


def create_notebooks():
    for nb in notebooks:
        path = PROJECT_ROOT / nb
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            nb_content = new_notebook(cells=[])
            with open(path, "w", encoding="utf-8") as f:
                nbformat.write(nb_content, f)


if __name__ == "__main__":
    create_folders()
    create_py_and_md_files()
    create_notebooks()
    print("Project structure created successfully.")