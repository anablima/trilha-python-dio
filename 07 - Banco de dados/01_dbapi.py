import sqlite3
from pathlib import Path

# Diretório raiz do arquivo atual para manter o banco junto do script.
ROOT_PATH = Path(__file__).parent

# Abre/Cria uma conexão SQLite usando um arquivo .sqlite no diretório do script.
# Observação: uma conexão deve ser fechada ao final (omitido aqui por simplicidade didática).
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
# Cria um cursor para executar comandos SQL.
cursor = conexao.cursor()
# `row_factory` como `sqlite3.Row` permite acessar colunas por nome (estilo dict).
cursor.row_factory = sqlite3.Row


# Cria a tabela `clientes` com colunas id, nome e email.
def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


# Insere um registro usando placeholders `?` para evitar SQL injection.
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


# Atualiza um registro pelo `id`, também utilizando parâmetros.
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


# Exclui um registro pelo `id` com consulta parametrizada.
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


# Insere múltiplos registros de uma vez com `executemany`.
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


# Recupera um cliente pelo `id`; retorna uma única linha (ou None).
def recuperar_cliente(cursor, id):
    cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


# Lista clientes em ordem decrescente por nome; retorna um iterável de linhas.
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# Exemplo de uso: listar todos os clientes e imprimir como dict.
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

# Recupera cliente com id=2 e imprime dados.
cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])
print(f'Seja bem vindo ao sistema {cliente["nome"]}')

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Chappie", "chappie@gmail.com"),
#     ("Melaine", "melaine@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)
