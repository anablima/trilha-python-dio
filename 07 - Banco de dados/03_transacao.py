import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Abre conexão e configura cursor/row_factory para acesso por nome de coluna.
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# Demonstração de transações: commit e rollback.
# Se algum comando falhar dentro do try, fazemos rollback para desfazer mudanças.
try:
    # Exclui cliente com id=8 e confirma alteração
    cursor.execute("DELETE FROM clientes WHERE id = 8;")
    conexao.commit()

    # Insere um registro válido
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    # Tenta inserir um registro com id explícito 2 (pode violar UNIQUE/PRIMARY KEY)
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    conexao.commit()
except Exception as exc:
    # Capta a exceção, informa e reverte todas as mudanças não desejadas
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()
