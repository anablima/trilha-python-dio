from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Base declarativa do SQLAlchemy 2.0 para tipagem com `Mapped[...]`.
class Base(DeclarativeBase):
    pass


# Instância do SQLAlchemy usando `Base` como classe base dos modelos.
db = SQLAlchemy(model_class=Base)
