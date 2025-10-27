lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(f'\nID de L2 (função copy): {id(l2)}\nID da Lista: {id(lista)}')

# Devido possuirem IDs diferentes, o que alterarmos em uma não ocorrerá com a outra
