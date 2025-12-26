import sqlalchemy as sa

from src.database import metadata

# Tabela de contas: saldo, vínculo com usuário e timestamp
accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    # `user_id` representa o dono da conta
    sa.Column("user_id", sa.Integer, nullable=False, index=True),
    # `Numeric(10,2)` armazena valores monetários com 2 casas decimais
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, default=0),
    # `TIMESTAMP(timezone=True)` registra data/hora com informação de fuso
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
