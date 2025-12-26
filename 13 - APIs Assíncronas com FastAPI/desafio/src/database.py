import databases
import sqlalchemy as sa

from src.config import settings

# Cliente async de banco e metadados do SQLAlchemy Core.
database = databases.Database(settings.database_url)
metadata = sa.MetaData()

# Engine síncrona para criação de tabelas/migrações; em SQLite, ajusta `check_same_thread`.
if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})
