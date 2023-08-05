from pathlib import Path, PurePath
from typing import Final

# Path to the root of project
ROOT_DIR: Final[Path] = Path(__file__).parent.parent.parent

TEMPLATES_DIR: Final[PurePath] = PurePath(ROOT_DIR / "app/templates/")
RU_TEMPLATES_DIR: Final[PurePath] = PurePath(TEMPLATES_DIR / "ru.ftl")
EN_TEMPLATES_DIR: Final[PurePath] = PurePath(TEMPLATES_DIR / "en.ftl")
