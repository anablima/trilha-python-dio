"""
Operadores lógicos em Python:
- `and`: só é True se todas as condições forem True.
- `or`: é True se pelo menos uma condição for True.

Precedência: `and` tem prioridade sobre `or` (use parênteses para clareza).
"""

# Exemplos simples de AND e OR
print(True and True and True)     # True
print(True and False and True)    # False
print(False and False and False)  # False
print(True or True or True)       # True
print(True or False or False)     # True
print(False or False or False)    # False

# Cenário: regra para permitir saque
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Sem parênteses: AND é avaliado antes de OR
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # True se conta normal tem saldo e dentro do limite OU conta especial com saldo

# Com parênteses: torna a intenção explícita
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# Fatorando condições com nomes descritivos
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
