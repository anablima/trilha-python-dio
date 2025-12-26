"""
Encapsulamento:
- Convenção `_atributo` indica uso interno (não fazer acesso direto fora da classe).
- Métodos `depositar`, `sacar` e `mostrar_saldo` provêm interface pública.
 - Evite acessar `_saldo` diretamente; prefira os métodos.
"""


class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # Atributo "protegido" por convenção
        self._saldo = saldo
        # Atributo público
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # Acrescenta valor ao saldo (sem validação neste exemplo)
        self._saldo += valor

    def sacar(self, valor):
        # Subtrai valor do saldo (sem validação/limites neste exemplo)
        self._saldo -= valor

    def mostrar_saldo(self):
        # Retorna saldo atual (ponto único de leitura do saldo)
        return self._saldo


# Uso da classe
conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
