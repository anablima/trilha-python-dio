import sqlalchemy as sa

from src.database import metadata

# Tabela de posts: título único, conteúdo e publicação
posts = sa.Table(
    "posts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    # Limite de 150 caracteres e unicidade
    sa.Column("title", sa.String(150), nullable=False, unique=True),
    # Conteúdo livre em `String`
    sa.Column("content", sa.String, nullable=False),
    # Data/hora de publicação (pode ser nula)
    sa.Column("published_at", sa.TIMESTAMP(timezone=True), nullable=True),
    # Flag indicando se está publicado
    sa.Column("published", sa.Boolean, default=False),
)
