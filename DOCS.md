# Aioplate usage guide

**Aioplate is a universal scalable template for creating Telegram bots on Python Aiogram.**

# Default stack for Aioplate

- **Python 3.9.x** and higher
- **Aiogram 2.x**
- **Aiogram MemoryStorage** for temporary data. You can replace it with **RedisStorage2** & aioredis.
- **PostgreSQL** (**SQLAlchemy** as an ORM + **asyncpg** as a driver + **alembic** as a migration service).

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

5) Configure environment with poetry:
    - Note: You need to have Poetry installed: `pip install poetry`
    - Install dependencies: `poetry install`
    - Run app: `make run`
    - Update dependencies*: `poetry update`

6) It is highly recommended for deployment (Ubuntu / Debian):
    - Configure app.service file.
    - `cp app.service etc/systemd/system/YOUR_APP_NAME.service`
    - `sudo systemctl enable YOUR_APP_NAME.service`
    - `sudo systemctl start YOUR_APP_NAME.service`
    - Check status: `sudo systemctl status YOUR_APP_NAME.service`

**If you started app, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**
