import sqlite3
from pathlib import Path
from sqlite3 import Connection, Cursor


# Cria a estrutura (schema) do banco e tabelas necessárias.
# Usa `executescript` para executar múltiplos comandos SQL de uma vez.
def criar_bd(cursor: Cursor) -> None:
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            status TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS pessoa_fisica (
            cliente_id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            renda_mensal REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        );

        CREATE TABLE IF NOT EXISTS pessoa_juridica (
            cliente_id INTEGER PRIMARY KEY,
            nome_fantasia TEXT,
            cnpj TEXT NOT NULL UNIQUE,
            faturamento_anual REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        );
                   """
    )


# Cria e retorna uma conexão SQLite localizada ao lado deste arquivo.
# Observação: `row_factory` pode ser configurado após obter o cursor.
def criar_conexao() -> Connection:
    ROOT_PATH = Path(__file__).parent
    return sqlite3.connect(ROOT_PATH / "db.sqlite")
