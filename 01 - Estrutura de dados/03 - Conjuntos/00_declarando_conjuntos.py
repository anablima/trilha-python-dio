"""
Conjuntos (`set`): coleção não ordenada, sem elementos duplicados.
`set(iterável)` converte qualquer iterável em conjunto e remove duplicatas.
"""

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # caracteres únicos da palavra

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
