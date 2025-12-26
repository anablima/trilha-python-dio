"""
Controle de fluxo em laços:
- `break`: interrompe o loop atual.
- `continue`: pula para a próxima iteração.
"""

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break  # encerra quando o número é 10

    if numero % 2 == 0:
        continue  # ignora pares

    print(numero)


# Exemplo equivalente com for (comentado):
# for numero in range(100):
#     if numero % 2 == 0:
#         continue
#     print(numero, end=" ")
