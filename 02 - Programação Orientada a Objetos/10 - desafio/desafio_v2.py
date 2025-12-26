import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# Sistema bancário orientado a objetos:
# Define clientes, contas, histórico de transações e operações (depósito/saque).
class Cliente:
    def __init__(self, endereco):
        # Dados do cliente e sua lista de contas associadas
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # Orquestra a transação: delega para o objeto transação
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Vincula uma conta ao cliente
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Inicializa dados da classe base e atributos específicos
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        # Estado interno da conta (atributos com underscore por convenção)
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Factory method: cria uma nova instância usando a classe (cls)
        return cls(numero, cliente)

    @property
    def saldo(self):
        # Exposição somente leitura do saldo
        return self._saldo

    @property
    def numero(self):
        # Número da conta (somente leitura)
        return self._numero

    @property
    def agencia(self):
        # Agência da conta (somente leitura)
        return self._agencia

    @property
    def cliente(self):
        # Cliente titular (somente leitura)
        return self._cliente

    @property
    def historico(self):
        # Histórico de transações (somente leitura)
        return self._historico

    def sacar(self, valor):
        # Regras de saque: exige valor positivo e saldo suficiente
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        # Regras de depósito: exige valor positivo
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Estende a conta com limite por operação e limite de saques diários
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        # Calcula quantos saques já foram feitos no histórico
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        # Restrições adicionais: valor não pode exceder o limite e
        # quantidade de saques não pode exceder o limite configurado
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Delega a regra comum para a classe base
            return super().sacar(valor)

        return False

    def __str__(self):
        # Representação amigável da conta para impressão
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        # Lista de transações realizadas na conta
        self._transacoes = []

    @property
    def transacoes(self):
        # Exposição somente leitura
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Grava uma transação com tipo, valor e timestamp formatado
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        # Deve retornar o valor monetário da transação
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        # Deve executar a operação na conta (ex.: sacar/depositar)
        pass


class Saque(Transacao):
    def __init__(self, valor):
        # Valor solicitado para saque
        self._valor = valor

    @property
    def valor(self):
        # Exposição do valor
        return self._valor

    def registrar(self, conta):
        # Executa o saque e registra no histórico se bem-sucedido
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        # Valor a depositar
        self._valor = valor

    @property
    def valor(self):
        # Exposição do valor
        return self._valor

    def registrar(self, conta):
        # Executa o depósito e registra no histórico se bem-sucedido
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    # Apresenta o menu principal e coleta a opção do usuário
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    # Busca cliente pelo CPF; retorna o primeiro encontrado ou None
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    # Recupera uma conta do cliente para operar
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    # Retorna a primeira conta por simplicidade
    return cliente.contas[0]


def depositar(clientes):
    # Fluxo de depósito: identifica cliente, cria transação e registra
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    # Fluxo de saque: identifica cliente, cria transação e registra
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    # Exibe o extrato de movimentações e o saldo atual da conta
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        # Monta texto com cada transação do histórico
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    # Cadastro de novo cliente (Pessoa Física)
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    # Criação de nova conta corrente e vinculação ao cliente
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    # Lista todas as contas existentes com representação amigável
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    # Loop principal de interação com o usuário e orquestração das operações
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            # Número da conta sequencial baseado na quantidade atual
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            # Encerra o programa
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
