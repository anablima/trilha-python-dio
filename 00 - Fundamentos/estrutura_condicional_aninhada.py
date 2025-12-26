"""
Condicionais aninhadas:
- Encadeiam decisões específicas por tipo de conta.
- Cada bloco trata regras próprias (saldo, cheque especial, etc.).
"""

conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    # Regras para conta normal: permite cheque especial
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    # Regras para conta universitária: sem cheque especial
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    # Apenas seleciona conta especial (exemplo didático)
    print("Conta especial selecionada!")

else:
    # Fallback quando nenhum tipo reconhecido
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")
