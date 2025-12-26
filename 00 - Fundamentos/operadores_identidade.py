"""
Operadores de identidade:
- `is` / `is not` comparam se dois objetos são o MESMO objeto na memória.
Use `==` para comparar valores; use `is` para identidade (objetos, singletons como None).
"""

# Exemplos com inteiros (pode haver interning para pequenos ints)
saldo = 1000
limite = 1000

print(saldo is limite)       # Identidade (mesmo objeto?) → pode ser False apesar de iguais em valor
print(saldo is not limite)   # Não são o mesmo objeto? → inverso de 'is'

# Dica: para verificar igualdade de conteúdo, use '=='
# Ex.: print(saldo == limite)  # True


