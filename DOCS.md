# Aioplate usage guide

**Aioplate is a universal scalable template for creating Telegram bots on Python Aiogram.**

# Default stack for Aioplate

- **Python 3.9.x** and higher
- **Aiogram 2.x**
- **Aiogram MemoryStorage** for temporary data. You can replace it with **RedisStorage2** & aioredis.
- **PostgreSQL** (**SQLAlchemy** as ORM + **asyncpg** as driver + **alembic** as migrations helper).
- **Pydantic** as a tool for data validation & parsing.

## Installation

1) Create repo by this template
2) Configure bot settings:
    1) Rename `app.ini.example` to `app.ini`. Don't worry, app.ini already added to gitignore.
    2) Configure app.ini vars. Bot parse_mode, redis params are optional and you can remove it if you want.
3) Configure system:
    - Install postgreSQL, systemd, Python 3.9.x

4) Configure Postgres & alembic:
    - PSQL: `CREATE DATABASE your_database_name;`
    - Already made:  `alembic init --template async migrations`
    - Open alembic.ini -> `sqlalchemy.url = postgresql+asyncpg://user:pass@localhost/dbname`
    - `alembic revision --autogenerate -m "init"`
    - `alembic upgrade head`
    - Add alembic.ini to gitignore

5) You have 2 default ways to configure project.
    1) Configure python-app & dependencies with pip:
        - Create venv: `python3.10 -m venv venv`
        - Activate venv: `source venv/bin/activate`
        - Install dependencies: `pip install -r requirements.txt`
        - Run app: `python .`
    2) Configure python-app & dependencies with poetry:
        - Note: You need to have Poetry installed: `pip install poetry`
        - Install dependencies: `poetry install`
        - Run app: `make run`
        - Update dependencies: `poetry update`

6) It is highly recommended for deployment (Ubuntu / Debian):
    - Configure app.service file.
    - `cp app.service etc/systemd/system/YOUR_APP_NAME.service`
    - `sudo systemctl enable YOUR_APP_NAME.service`
    - `sudo systemctl start YOUR_APP_NAME.service`
    - Check status: `sudo systemctl status YOUR_APP_NAME.service`

**If you started app, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**

## Style guides

### Handlers

- Should be tiny: about 10-15 lines of code.
- No business logic: connection with API services, ORM queries, http requests etc.
  All this functionality should be realized in services and provide the interface to connect them from view.
- Docstrings with description of functionality for all handlers.
- No more than 4 decorators on each handler.
- Use same titles for message instances, callback-query instances in all handlers. For message use `m`, for callback
  use `call`.

### Messages

- To have an obvious structure and logic for storing messages,
  you should have the **duplicated architecture in messages and handlers package.**
  **_For example:_** If handler-module is private chat package named `base`,
  create the messages-storage-file with same name in messages/private_chat package.   
  *You can check my example with base handler.*
- **No cross-imports!** Your handler-module should import only one messages storage. E.g.: `base` handler should import
  only `base as msgs` message storage; and do not import another messages from any files.
  In this case, do not be afraid of possible duplication of texts in different files. This will further prevent
  cross-handlers-changes and text side effects.
- I suggest using the `msgs` name for the abbreviation of message storage in all handlers. This will ensure the same
  interface to call message storages.

### Docs & tests & CI

- I configured default pylint checkers. Aioplate has a full coverage of docstrings.
  In some cases, writing docstrings is unnecessary, and you can disable this checker.
- I don't write unit tests for bot & aiogram logic. Only for business-logic.
  But up to you. Some people want to have 100% test coverage, and I have nothing against them.

## Contribution

**Feel free to contribute for Aioplate. If you integrate new technologies, you are responsible for the
additions to the documentation (DOCS.md). So, I will not accept pull requests that will not pass code-style
coverage (GitHub actions pylint tests).**

**So, if you have any problems with Aioplate, feel free to open issues on GitHub or ping me in Telegram:
https://t.me/karych.**
