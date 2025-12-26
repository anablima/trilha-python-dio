import textwrap

from servico import ClienteServico


# Função utilitária para imprimir o menu e coletar a opção do usuário.
def menu():
    menu = """\n
    ================ MENU ================
    [1]\tNovo cliente
    [2]\tListar clientes
    [0]\tSair
    => """
    # `textwrap.dedent` remove indentação comum para uma visualização limpa
    return input(textwrap.dedent(menu))


# Ponto de entrada da aplicação interativa.
def main():
    # Instancia o serviço com `cursor=None` como placeholder.
    # Em uma implementação completa, obteríamos um cursor real da conexão
    # (ex.: via `criar_conexao()` em `bd.py`) e passaríamos aqui.
    servico = ClienteServico(cursor=None)

    while True:
        # Estrutura de `match` para decidir a ação conforme a opção digitada.
        match menu():
            case "1":
                # Cria um novo cliente (PF se CPF, PJ se CNPJ)
                servico.criar_cliente()
            case "2":
                # Lista todos os clientes cadastrados
                servico.listar_clientes()
            case "0":
                # Encerra o loop e o programa
                break
            case _:
                # Mensagem de opção inválida para qualquer outro caso
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
