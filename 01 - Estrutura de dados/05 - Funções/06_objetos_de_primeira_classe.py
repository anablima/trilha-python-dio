def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    # Funções são objetos de primeira classe: podem ser passadas como argumentos
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # usa a função 'somar' como parâmetro
exibir_resultado(10, 5, subtrair)  # usa a função 'subtrair' como parâmetro

# Também é possível atribuir funções a variáveis e chamá-las
op = somar
print(op(20, 20))  # 40
