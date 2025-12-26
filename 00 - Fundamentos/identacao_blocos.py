"""
Indentação e blocos:
- Em Python, a indentação define blocos (funções, condicionais, loops).
- Não há chaves `{}`; a estrutura é determinada por recuo.
"""

def sacar(valor):  # início do bloco da função
    saldo = 500

    if saldo >= valor:  # início do bloco do if
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    # fim do bloco do if
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
# fim do bloco da função


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)
