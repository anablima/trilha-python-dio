from abc import ABC, abstractmethod
from datetime import datetime


# Sistema bancário orientado a objetos (versão 1):
# Define cliente, pessoa física, conta, conta corrente, histórico e transações (saque/deposito).
class Cliente:
    def __init__(self, endereco):
        # Dados de identificação e lista de contas associadas ao cliente
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # Orquestra a operação delegando à transação
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Vincula uma conta ao cliente
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Inicializa atributos de Cliente e dados específicos da pessoa física
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        # Estado interno da conta (underscore por convenção de uso interno)
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Factory method: cria uma nova conta usando a classe (cls)
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
        # Agência bancária (somente leitura)
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
        # Regras de saque: valor positivo e saldo suficiente
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
        # Regras de depósito: valor deve ser positivo
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Conta corrente adiciona limite por operação e limite de saques diários
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        # Calcula quantidade de saques realizados no histórico
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        # Restrições: valor não pode exceder limite; saques não podem exceder limite diário
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            # Delega verificação comum de saldo à classe base
            return super().sacar(valor)

        return False

    def __str__(self):
        # Representação amigável para impressão dos dados da conta
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        # Lista de transações realizadas
        self._transacoes = []

    @property
    def transacoes(self):
        # Exposição somente leitura
        return self._transacoes

    def adicionar_transacao(self, transacao):
        # Registra transação com tipo, valor e timestamp formatado
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
        # Deve retornar o valor monetário envolvido
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        # Deve executar a operação na conta (sacar/depositar)
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
        # Executa saque e registra no histórico se bem-sucedido
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        # Valor a ser depositado
        self._valor = valor

    @property
    def valor(self):
        # Exposição do valor
        return self._valor

    def registrar(self, conta):
        # Executa depósito e registra no histórico se bem-sucedido
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
