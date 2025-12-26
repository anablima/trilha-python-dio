def calcular_total(numeros):
    # Retorna a soma dos elementos do iterável
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    # Retorna múltiplos valores como tupla (packing)
    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
# Dica: pode fazer unpacking: a, b = retorna_antecessor_e_sucessor(10)
