# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
# Compreensão com condição (filtra pares)
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
# Mapeamento: eleva cada número ao quadrado
quadrado = [numero**2 for numero in numeros]
print(quadrado)
