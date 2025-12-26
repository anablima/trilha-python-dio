from sqlite3 import Connection, Cursor


# Funções utilitárias de banco de dados (camada de persistência).
# A ideia é centralizar criação de conexão e estrutura (tabelas).
# Mantemos `pass` para indicar que ainda será implementado.
def criar_bd(cursor: Cursor) -> None:
    # Responsabilidade esperada:
    # - Executar os comandos SQL de criação de tabelas necessárias
    #   (ex.: tabela de clientes PF/PJ, colunas obrigatórias, constraints).
    # - Usar `cursor.execute(...)` e, após concluir, realizar `commit` na conexão
    #   (o commit não é feito aqui porque só temos o cursor; pode ser feito fora).
    # - Implementar `CREATE TABLE IF NOT EXISTS ...` para idempotência.
    # Exemplo (ilustrativo):
    # cursor.execute("""
    #   CREATE TABLE IF NOT EXISTS clientes (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     tipo TEXT NOT NULL,          -- 'pf' ou 'pj'
    #     documento TEXT UNIQUE NOT NULL, -- cpf ou cnpj
    #     nome TEXT NOT NULL,
    #     email TEXT NOT NULL,
    #     telefone TEXT NOT NULL,
    #     status TEXT NOT NULL
    #   )
    # """)
    pass


def criar_conexao() -> Connection:
    # Responsabilidade esperada:
    # - Abrir/retornar uma `Connection` para SQLite (ou outro SGBD),
    #   preferencialmente usando um caminho estável via `pathlib.Path`.
    # - Configurar `row_factory` quando necessário para acesso por nome.
    # - Pode também criar o `cursor` e invocar `criar_bd(cursor)` na inicialização.
    # Exemplo (ilustrativo):
    # from sqlite3 import connect, Row
    # from pathlib import Path
    # db_path = Path(__file__).parent / "clientes.sqlite"
    # conn = connect(db_path)
    # conn.row_factory = Row
    # return conn
    pass
