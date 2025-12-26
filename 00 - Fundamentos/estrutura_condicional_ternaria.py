"""
Operador condicional ternário:
`x if condicao else y` retorna `x` quando a condição é verdadeira; caso contrário, `y`.
"""

saldo = 2000
saque = 2500

# Define status com base na condição de saldo suficiente
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
