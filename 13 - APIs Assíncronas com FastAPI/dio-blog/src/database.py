import databases
import sqlalchemy as sa

from src.config import settings

# Cliente assíncrono e metadados para tabelas
database = databases.Database(settings.database_url)
metadata = sa.MetaData()

# Engine: ajusta `check_same_thread` em desenvolvimento (SQLite)
if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(settings.database_url, connect_args={"check_same_thread": False})
