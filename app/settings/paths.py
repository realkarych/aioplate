from pathlib import Path


def get_project_root() -> Path:
    """Returns path to project dir"""
    return Path(__file__).parent.parent.parent
