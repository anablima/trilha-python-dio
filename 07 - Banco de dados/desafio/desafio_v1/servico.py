from sqlite3 import Cursor

from dominio import Cliente, PessoaFisica, PessoaJuridica


# Camada de serviço (regras de negócio) que orquestra entradas e persistência.
class ClienteServico:
    def __init__(self, cursor: Cursor) -> None:
        # Cursor do banco para executar consultas e comandos.
        # Em implementação real, viria de `criar_conexao()` (bd.py) e seria compartilhado.
        self.cursor = cursor

    def filtrar_cliente(self, documento: str) -> Cliente | None:
        # Responsabilidade esperada:
        # - Consultar o banco pelo `documento` (CPF/CNPJ) de forma parametrizada,
        #   ex.: `SELECT * FROM clientes WHERE documento=?`.
        # - Retornar uma instância de `PessoaFisica` ou `PessoaJuridica` conforme o tipo salvo,
        #   ou `None` se não existir.
        # - Evitar SQL injection (nunca concatenar string com entrada do usuário).
        # Mantemos `pass` para indicar implementação futura.
        pass

    def _criar_cliente_pessoa_fisica(self, documento: str) -> PessoaFisica:
        # Coleta dados de PF via input (interativo).
        nome = input("Informe o nome completo: ")
        renda_mensal = float(input("Informe sua renda mensal: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        # Cria objeto de domínio com status "ativo" por padrão.
        return PessoaFisica(
            nome=nome, cpf=documento, renda_mensal=renda_mensal, email=email, telefone=telefone, status="ativo"
        )

    def _criar_cliente_pessoa_juridica(self, documento: str) -> PessoaJuridica:
        # Coleta dados de PJ via input (interativo).
        nome = input("Informe o nome fantasia: ")
        faturamento_anual = float(input("Informe sua renda mensal: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        # Cria objeto de domínio com status "ativo" por padrão.
        return PessoaJuridica(
            nome_fantasia=nome,
            cnpj=documento,
            faturamento_anual=faturamento_anual,
            email=email,
            telefone=telefone,
            status="ativo",
        )

    def criar_cliente(self) -> None:
        # Fluxo de criação: impede duplicidade, escolhe PF/PJ pelo tamanho do documento.
        documento = input("Informe o documento (CPF/CNPJ): ")
        cliente = self.filtrar_cliente(documento)

        if cliente:
            # Se já existe, cancela criação
            print("\n@@@ Já existe cliente com esse documento (CPF/CNPJ)! @@@")
            return

        if len(documento) == 11:
            # Documento com 11 dígitos: CPF
            cliente = self._criar_cliente_pessoa_fisica(documento=documento)
        else:
            # Senão, tratamos como CNPJ
            cliente = self._criar_cliente_pessoa_juridica(documento=documento)

        # Exibe o objeto criado (didático). Em produção, persistir no BD.
        print(cliente)
        print("\n=== Cliente criado com sucesso! ===")

    def listar_clientes(self) -> None:
        # Responsabilidade esperada:
        # - Consultar e listar clientes do BD (SELECT ... ORDER BY ...).
        # - Converter linhas em objetos de domínio quando necessário.
        # No momento, apenas mensagem didática.
        print("Não existem clientes cadastrados!")
