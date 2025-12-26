# Primeira função: retorna uma mensagem curta de saudação
def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


# Segunda função: retorna uma mensagem longa de saudação
def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


# Função de ordem superior: recebe uma função como parâmetro e a executa
# Demonstra o conceito de funções como objetos de primeira classe em Python
def executar(funcao, nome):
    print("executando executar")
    # Chama a função recebida como parâmetro, passando o nome como argumento
    # A ordem dos prints ajuda a visualizar o fluxo de execução
    return funcao(nome)


# Executa a função 'mensagem' através da função 'executar'
# A função 'mensagem' é passada como argumento (sem parênteses)
print(executar(mensagem, "Joao"))

# Executa a função 'mensagem_longa' através da função 'executar'
# Demonstra que podemos passar diferentes funções para a mesma função executora
print(executar(mensagem_longa, "Joao"))
