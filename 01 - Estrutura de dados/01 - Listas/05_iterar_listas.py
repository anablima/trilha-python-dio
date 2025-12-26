carros = ["gol", "celta", "palio"]

# Iteração direta sobre elementos
for carro in carros:
    print(carro)


# `enumerate(seq)`: fornece pares (índice, elemento)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
