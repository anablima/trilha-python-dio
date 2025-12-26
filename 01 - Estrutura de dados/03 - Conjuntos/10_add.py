sorteio = {1, 23}

# add(x): insere x no conjunto apenas se não estiver presente
sorteio.add(25)  # {1, 23, 25}
print(sorteio)

# novos elementos aumentam o conjunto; ordem de exibição não é garantida
sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

# adicionar um elemento já existente não muda nada (sem duplicatas)
sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
