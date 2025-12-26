import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


# Iterador customizado para exibir contas formatadas.
# Mantém um índice interno e retorna uma string com os dados da conta a cada avanço.
class contasIterador:
    def __init__(self, contas):
        # Armazena a lista de contas recebida
        self.contas = contas
        # Índice atual do iterador
        self._index = 0

    def __iter__(self):
        # Um iterador retorna a si mesmo em __iter__
        return self

    def __next__(self):
        try:
            # Tenta obter a conta corrente pelo índice
            conta = self.contas[self._index]
            # Retorna uma string multilinha com os dados formatados
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            # Quando não há mais itens, sinaliza o fim da iteração
            raise StopIteration
        finally:
            # Avança o índice independentemente de sucesso/erro
            self._index += 1


# Representa um cliente com endereço e múltiplas contas.
class Cliente:
    def __init__(self, endereco):
        # Endereço do cliente (string descritiva)
        self.endereco = endereco
        # Coleção de contas do cliente
        self.contas = []
        # Índice da conta ativa (não utilizado aqui, mas reservado)
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        # Regra de limite diário de transações: máximo 2 por dia
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return

        # Executa o registro da transação na conta
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Vincula uma nova conta ao cliente
        self.contas.append(conta)


# Cliente pessoa física com nome, data de nascimento e CPF.
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# Conta bancária genérica com saldo, número, agência, cliente e histórico.
class Conta:
    def __init__(self, numero, cliente):
        # Atributos "protegidos" (convenção de underscore)
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Fábrica de contas: facilita criar instâncias de subclasses
        return cls(numero, cliente)

    @property
    def saldo(self):
        # Acesso somente leitura ao saldo
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        # Validações básicas de saldo e valor
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            # Debita e sinaliza sucesso
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        # Em casos de falha, retorna False
        return False

    def depositar(self, valor):
        # Deposita valor positivo no saldo
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


# Conta corrente com limite de valor por saque e limite de quantidade de saques.
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        # Fábrica ajustada com parâmetros de limites
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        # Conta quantos saques já ocorreram no histórico desta conta
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        # Verifica limites de valor e de quantidade
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Delega para a lógica base de saque
            return super().sacar(valor)

        return False

    def __str__(self):
        # Representação amigável para imprimir dados da conta
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


# Histórico de transações (tipo, valor, data formatada).
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Registra transação com carimbo de data/hora local
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        # Gera um iterador (generator) filtrando por tipo, se informado
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        # Usa a data atual em UTC para comparação
        # Nota: como as transações são salvas com hora local (datetime.now),
        # essa comparação pode divergir em fusos horários diferentes.
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


# Interface de transação com valor e método de registro.
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta):
        pass


# Transação de saque: debita da conta se houver saldo.
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta realizar o saque e registra no histórico em caso de sucesso
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Transação de depósito: credita valor positivo na conta.
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta depositar e registra no histórico em caso de sucesso
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Decorador para logar a execução das funções de fluxo.
def log_transacao(func):
    def envelope(*args, **kwargs):
        # Executa a função original e captura seu resultado
        resultado = func(*args, **kwargs)
        # Log simples com timestamp local e nome da função em maiúsculas
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado

    return envelope


# Exibe o menu e captura a opção do usuário.
def menu():
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

    # textwrap.dedent remove indentação comum do texto do menu
    return input(textwrap.dedent(menu))


# Busca um cliente pelo CPF na coleção.
def filtrar_cliente(cpf, clientes):
    # Filtra por igualdade de CPF e retorna o primeiro encontrado
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


# Recupera a primeira conta do cliente (simplificação).
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


# Fluxo de depósito com entradas pelo teclado.
@log_transacao
def depositar(clientes):
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


# Fluxo de saque com validações de saldo/limites.
@log_transacao
def sacar(clientes):
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


# Exibe o extrato gerado pelo histórico da conta.
@log_transacao
def exibirExtrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    # Itera sobre o relatório (todas as transações) e formata o extrato
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f'\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


# Cria um novo cliente pessoa física e adiciona à lista.
@log_transacao
def criarCliente(clientes):
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


# Cria uma conta corrente para um cliente existente.
@log_transacao
def criarConta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    # NOTE: O valor padrão de limite de saques foi alterado para 50 saques
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


# Lista todas as contas usando o iterador customizado.
def listarContas(contas):
    for conta in contasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


# Loop principal do programa: orquestra as operações via menu interativo.
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibirExtrato(clientes)

        elif opcao == "nu":
            criarCliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criarConta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listarContas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
