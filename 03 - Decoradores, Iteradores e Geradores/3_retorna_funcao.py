# Função factory que retorna uma função de acordo com a operação solicitada
# Demonstra o conceito de closure e funções de ordem superior
def calculadora(operacao):
    # Função interna para operação de soma
    def soma(a, b):
        return a + b

    # Função interna para operação de subtração
    def sub(a, b):
        return a - b

    # Função interna para operação de multiplicação
    def mul(a, b):
        return a * b

    # Função interna para operação de divisão
    def div(a, b):
        return a / b

    # Match/case (estrutural pattern matching) para selecionar a operação
    # Retorna a FUNÇÃO correspondente (não o resultado da execução)
    # Recurso disponível no Python 3.10+
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


# Obtém a função de soma através da calculadora
op = calculadora("+")
# Executa a função de soma com os valores 2 e 2 (resultado: 4)
print(op(2, 2))

# Obtém a função de subtração através da calculadora
op = calculadora("-")
# Executa a função de subtração com os valores 2 e 2 (resultado: 0)
print(op(2, 2))

# Obtém a função de multiplicação através da calculadora
op = calculadora("*")
# Executa a função de multiplicação com os valores 2 e 2 (resultado: 4)
print(op(2, 2))

# Obtém a função de divisão através da calculadora
op = calculadora("/")
# Executa a função de divisão com os valores 2 e 2 (resultado: 1.0)
print(op(2, 2))
