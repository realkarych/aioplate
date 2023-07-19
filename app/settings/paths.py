from pathlib import Path, PurePath

# Path to the root of project
ROOT_DIR: Path = Path(__file__).parent.parent.parent

TEMPLATES_DIR: PurePath = PurePath(ROOT_DIR / "app/templates/")
RU_TEMPLATES_DIR: PurePath = PurePath(TEMPLATES_DIR / "ru.ftl")
EN_TEMPLATES_DIR: PurePath = PurePath(TEMPLATES_DIR / "en.ftl")
