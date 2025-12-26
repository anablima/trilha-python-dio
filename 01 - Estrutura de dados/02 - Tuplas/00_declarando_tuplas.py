"""
Declaração de tuplas (sequências imutáveis):
- Literais com parênteses `(...)`.
- Conversão usando `tuple(iterável)`.
- Tupla unitária requer vírgula final.
"""

# Tupla literal com strings
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

# Conversão de string em tupla de caracteres
letras = tuple("python")
print(letras)

# Conversão de lista em tupla
numeros = tuple([1, 2, 3, 4])
print(numeros)

# Tupla unitária: precisa da vírgula para ser reconhecida como tupla
pais = ("Brasil",)
print(pais)
