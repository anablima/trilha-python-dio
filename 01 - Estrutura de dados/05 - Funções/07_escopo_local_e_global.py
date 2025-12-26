salario = 2000


def salario_bonus(bonus):
    # Usando 'global' para alterar a variável definida no escopo global
    global salario
    salario += bonus  # efeito colateral: modifica estado global
    return salario


salario_bonus(500)  # 2500
