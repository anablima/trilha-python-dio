from sqlite3 import Cursor

from dominio import Cliente, PessoaFisica, PessoaJuridica


# Camada de serviço que encapsula lógica de criação e listagem de clientes.
class ClienteServico:
    def __init__(self, cursor: Cursor) -> None:
        # Cursor do BD para executar consultas e comandos de inserção/seleção.
        self.cursor = cursor

    def filtrar_cliente(self, documento: str) -> int:
        # Retorna a contagem de registros para CPF ou CNPJ informado.
        # Consulta parametrizada evita SQL injection.
        if len(documento) == 11:
            self.cursor.execute("SELECT COUNT(*) AS total FROM pessoa_fisica WHERE cpf=?;", (documento,))
        else:
            self.cursor.execute("SELECT COUNT(*) AS total FROM pessoa_juridica WHERE cnpj=?;", (documento,))
        return self.cursor.fetchone()["total"]

    def _criar_cliente_pessoa_fisica(self, documento: str) -> PessoaFisica:
        # Coleta dados interativos e constrói objeto de domínio PF.
        nome = input("Informe o nome completo: ")
        renda_mensal = float(input("Informe sua renda mensal: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        return PessoaFisica(
            nome=nome, cpf=documento, renda_mensal=renda_mensal, email=email, telefone=telefone, status="ativo"
        )

    def _criar_cliente_pessoa_juridica(self, documento: str) -> PessoaJuridica:
        # Coleta dados interativos e constrói objeto de domínio PJ.
        nome = input("Informe o nome fantasia: ")
        faturamento_anual = float(input("Informe seu faturamento anual: "))
        email = input("Informe seu email: ")
        telefone = input("Informe seu telefone: ")

        return PessoaJuridica(
            nome_fantasia=nome,
            cnpj=documento,
            faturamento_anual=faturamento_anual,
            email=email,
            telefone=telefone,
            status="ativo",
        )

    def _criar_cliente(self, cliente: Cliente) -> int:
        # Insere os dados comuns na tabela `cliente` e retorna o `id` gerado.
        self.cursor.execute(
            "INSERT INTO cliente (email, telefone, status) VALUES (?,?,?);",
            (cliente.email, cliente.telefone, cliente.status),
        )
        return self.cursor.lastrowid

    def criar_cliente(self) -> None:
        # Orquestra a criação do cliente base e sua especialização PF/PJ.
        documento = input("Informe o documento (CPF/CNPJ): ")
        existe_cliente = self.filtrar_cliente(documento)

        if existe_cliente:
            print("\n@@@ Já existe cliente com esse documento (CPF/CNPJ)! @@@")
            return

        if len(documento) == 11:
            # Cria PF, insere base em `cliente` e especialização em `pessoa_fisica`.
            cliente = self._criar_cliente_pessoa_fisica(documento=documento)
            cliente_id = self._criar_cliente(cliente=cliente)
            self.cursor.execute(
                "INSERT INTO pessoa_fisica (cliente_id, nome, cpf, renda_mensal) VALUES (?,?,?,?)",
                (cliente_id, cliente.nome, cliente.cpf, cliente.renda_mensal),
            )
        else:
            # Cria PJ, insere base em `cliente` e especialização em `pessoa_juridica`.
            cliente = self._criar_cliente_pessoa_juridica(documento=documento)
            cliente_id = self._criar_cliente(cliente=cliente)
            self.cursor.execute(
                "INSERT INTO pessoa_juridica (cliente_id, nome_fantasia, cnpj, faturamento_anual) VALUES (?,?,?,?)",
                (cliente_id, cliente.nome_fantasia, cliente.cnpj, cliente.faturamento_anual),
            )

        print("\n=== Cliente criado com sucesso! ===")

    def listar_clientes(self) -> None:
        # Busca registros de PF e PJ associados à tabela `cliente`.
        self.cursor.execute("SELECT * FROM pessoa_fisica pf INNER JOIN cliente c ON c.id = pf.cliente_id;")
        clientes = self.cursor.fetchall()
        self.cursor.execute("SELECT * FROM pessoa_juridica pj INNER JOIN cliente c ON c.id = pj.cliente_id;")
        clientes += self.cursor.fetchall()

        if not clientes:
            print("\n@@@ Não existem clientes cadastrados! @@@")

        # Mapeia cada linha para dataclass adequada e imprime sua representação.
        for cliente in clientes:
            print(self._apresentar_dados(dados_cliente=dict(cliente)))

    def _apresentar_dados(self, dados_cliente: dict[str, str | int]) -> str:
        # Decide PF ou PJ pela presença de `cpf` na linha.
        # Retorna instância de dataclass cuja `__str__` formata a saída.
        if "cpf" in dados_cliente:
            return PessoaFisica.converter_objeto_bd(objeto_db=dados_cliente)
        return PessoaJuridica.converter_objeto_bd(objeto_db=dados_cliente)
