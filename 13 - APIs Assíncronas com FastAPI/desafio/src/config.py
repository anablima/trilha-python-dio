from pydantic_settings import BaseSettings, SettingsConfigDict


# Configurações carregadas de variáveis de ambiente via Pydantic Settings.
class Settings(BaseSettings):
    # Lê `.env`, ignora extras e usa UTF-8
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # URL do banco (ex.: sqlite+aiosqlite:///... ou postgres)
    database_url: str
    # Ambiente: pode alterar comportamentos (ex.: conexão SQLite)
    environment: str = "production"


settings = Settings()
