# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra todos os operadores aritméticos em Python
# Operadores disponíveis:
# +  : Adição
# -  : Subtração
# /  : Divisão (resultado sempre float)
# // : Divisão inteira (descarta decimal)
# *  : Multiplicação
# %  : Módulo (resto da divisão)
# ** : Exponenciação (potência)

# Definição das variáveis para os exemplos
produto_1 = 20  # Primeiro operando
produto_2 = 10  # Segundo operando

# Demonstração de cada operador
print(produto_1 + produto_2)   # Adição: 20 + 10 = 30
print(produto_1 - produto_2)   # Subtração: 20 - 10 = 10
print(produto_1 / produto_2)   # Divisão: 20 / 10 = 2.0 (sempre retorna float)
print(produto_1 // produto_2)  # Divisão inteira: 20 // 10 = 2 (descarta decimal)
print(produto_1 * produto_2)   # Multiplicação: 20 * 10 = 200
print(produto_1 % produto_2)   # Módulo: 20 % 10 = 0 (resto da divisão)
print(produto_1 ** produto_2)  # Exponenciação: 20 ** 10 = 20^10

# Exemplos com expressões complexas e precedência de operadores
# Parênteses têm precedência sobre operadores
x = (10 + 5) * 4              # Primeiro soma (15), depois multiplica: 15 * 4 = 60
y = (10 / 2) + 25 * ((2 - 2) ** 2)  # Resolução: (5) + 25 * (0 ** 2) = 5 + 25 * 0 = 5
print(x)  # Resultado da primeira expressão
print(y)  # Resultado da segunda expressão
