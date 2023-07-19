from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from app.settings import paths


def build_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {
            "ru": ("ru", "en"),
            "en": ("en",)
        },
        [
            FluentTranslator("en", translator=FluentBundle.from_files(
                locale="en-US",
                filenames=[paths.EN_TEMPLATES_DIR])),
            FluentTranslator("ru", translator=FluentBundle.from_files(
                locale="ru-RU",
                filenames=[paths.RU_TEMPLATES_DIR]))
        ],
        root_locale="en"
    )
    return translator_hub
