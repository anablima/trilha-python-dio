import os


# Configuração base da aplicação.
# `SQLALCHEMY_DATABASE_URI` pode vir de variável de ambiente `DATABASE_URL`.
class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


# Ambiente de produção: herda a configuração base.
class ProductionConfig(Config):
    pass


# Ambiente de desenvolvimento: usa SQLite local por padrão.
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///bank.sqlite"


# Ambiente de testes: usa banco em memória.
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
