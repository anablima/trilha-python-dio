import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Conecta ao banco SQLite no arquivo local.
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# ATENÇÃO: O uso de f-string para montar SQL é vulnerável a injeção de SQL.
# Exemplo de ataque: inserir `1 OR 1=1` como id pode retornar todos os registros.
# Boas práticas: sempre use consultas parametrizadas com `?`.
# Código seguro equivalente:
#   id_cliente = input("Informe o id do cliente: ")
#   cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
# Abaixo mantemos o exemplo inseguro apenas para fins didáticos.
id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
