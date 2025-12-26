numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# remove(x): remove x e não retorna valor (retorna None)
# se x não estiver no conjunto, levanta KeyError (diferente de discard)
print(numeros.remove(0))  # None
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
