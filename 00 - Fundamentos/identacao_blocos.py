def sacar(valor): # início do bloco do método
    saldo = 500

    if saldo >= valor: # início do bloco do if
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    # fim do bloco do if
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
# fim do bloco do método

def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)
