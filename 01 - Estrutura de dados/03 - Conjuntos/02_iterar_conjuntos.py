carros = {"gol", "celta", "palio"}

# Iteração direta (conjuntos são iteráveis, ordem não garantida)
for carro in carros:
    print(carro)

# `enumerate` em conjuntos: fornece índice gerado durante a iteração
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
