# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra diferentes formas de declarar listas em Python
# Demonstra:
# 1. Lista literal com elementos
# 2. Lista vazia
# 3. Conversão de string para lista
# 4. Conversão de range para lista
# 5. Lista com tipos mistos

# Exemplo 1: Declaração de lista com elementos literais
# Lista de strings usando colchetes []
frutas = ["laranja", "maca", "uva"]
print(frutas)  # Resultado: ['laranja', 'maca', 'uva']

# Exemplo 2: Declaração de lista vazia
# Pode ser preenchida posteriormente com append(), extend(), etc.
frutas = []
print(frutas)  # Resultado: []

# Exemplo 3: Criação de lista a partir de string
# A função list() converte uma string em uma lista de caracteres
letras = list("python")
print(letras)  # Resultado: ['p', 'y', 't', 'h', 'o', 'n']

# Exemplo 4: Criação de lista a partir de range
# list() converte o objeto range em uma lista de números
numeros = list(range(10))  # range(10) gera números de 0 a 9
print(numeros)  # Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exemplo 5: Lista com diferentes tipos de dados
# Python permite misturar tipos em uma mesma lista
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
# Tipos na lista acima:
# - Strings: "Ferrari", "F8", "São Paulo"
# - Inteiros: 4200000, 2020, 2900
# - Booleano: True
print(carro)
