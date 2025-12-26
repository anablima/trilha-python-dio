from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Carrega variáveis de `.env`, ignora extras e usa UTF-8
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    # URL do banco e ambiente atual
    database_url: str
    environment: str = "production"


settings = Settings()
