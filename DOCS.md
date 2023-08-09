# Aioplate usage guide

**Aioplate is a universal scalable template for creating Telegram bots on Python Aiogram.**

# Default stack for Aioplate

- **Python 3.11** and higher
- **Aiogram 3.x**
- **Aiogram MemoryStorage** for temporary data.
- **PostgreSQL** (**SQLAlchemy** as an ORM + **asyncpg** as a driver + **alembic** as a migration service).

## Installation

1) Create repo by this template and clone project.
2) Configure bot settings:
    - Rename `app.ini.example` to `app.ini`. Don't worry, app.ini already added to gitignore.
    - Configure app.ini variables.
3) Configure system:
   Install PostgreSQL, systemd, Python3.11, poetry.

4) Configure Postgres & alembic:
    - PSQL: `CREATE DATABASE db_name;`
    - `alembic init --template async migrations`
    - Open alembic.ini -> `sqlalchemy.url = postgresql+asyncpg://user:pass@localhost/dbname`
    - `alembic revision --autogenerate -m "init"`
    - `alembic upgrade head`

5) Configure environment with poetry:
    - Note: You need to have Poetry installed: `python3 -m pip install poetry`
    - Install dependencies: `poetry install`
    - Run app: `poetry run python -m app` *(only for testing your app. On production use launching by systemd service or
      create docker image)*. `app` is an entry point to the project.

6) Deployment:
    - Configure app.service file.
    - `cp app.service /etc/systemd/system/YOUR_APP_NAME.service`
    - `sudo systemctl enable YOUR_APP_NAME.service`
    - `sudo systemctl start YOUR_APP_NAME.service`
    - Check status: `sudo systemctl status YOUR_APP_NAME.service`

**If you started app, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**
