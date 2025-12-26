import sqlite3
import textwrap

from bd import criar_bd, criar_conexao
from servico import ClienteServico


# Exibe o menu e retorna a opção escolhida.
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tNovo cliente
    [2]\tListar clientes
    [0]\tSair
    => """
    # Remove indentação comum para visualização limpa
    return input(textwrap.dedent(menu))


# Ponto de entrada: cria conexão/cursor, inicializa BD e inicia o loop.
def main():
    # Abre conexão e cursor; configura `row_factory` para acesso por nome.
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.row_factory = sqlite3.Row

    # Cria tabelas caso não existam (idempotente).
    criar_bd(cursor=cursor)

    # Instancia o serviço com o cursor para operar sobre o banco.
    servico = ClienteServico(cursor=cursor)

    while True:
        match menu():
            case "1":
                # Cria cliente e persiste; `commit` confirma transação.
                servico.criar_cliente()
                conexao.commit()
            case "2":
                # Lista clientes PF e PJ
                servico.listar_clientes()
            case "0":
                # Encerra a aplicação
                break
            case _:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

    # Fecha a conexão ao terminar.
    conexao.close()


main()
