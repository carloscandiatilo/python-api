import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# ⚡ Carrega variáveis do .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# ⚡ Sobrescreve a URL do banco no Alembic
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# ⚡ Adiciona a raiz do projeto ao sys.path (pasta acima de migrations)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ⚡ Importa Base do SQLAlchemy
from database import Base
target_metadata = Base.metadata

# -----------------------------
# Migrações offline
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Migrações online
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
