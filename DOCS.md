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
    - `alembic init --template async migrations`
    - `alembic revision --autogenerate -m "init"`
    - `alembic upgrade head`
    - Open migrations/env.py -> `target_metadata = Base.metadata`. DON'T FORGET import Base from
      app.services.database.base
    - Open alembic.ini -> `sqlalchemy.url = postgresql+asyncpg://DB_OWNER:DB_OWNER_PASSWD@localhost/DB_NAME`

5) Configure python-app & dependencies:
    - `python3.9.x -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
    - Execute `__main__.py` script
6) It is highly recommended for deployment (Ubuntu / Debian):
    - Configure app.service file.
    - `cp app.service etc/systemd/system/`
    - `sudo systemctl enable app.service`
    - `sudo systemctl start app.service`
    - Check status: `sudo systemctl status app.service`

**If you launched bot polling, and no errors occurred, after submitting /start command to your Bot, welcome message
should be sent.**

✔ **Well Done!**


## Style guides
