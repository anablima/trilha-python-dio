"""
Funções em Python:
- Definição com `def nome(...):`.
- Parâmetros posicionais e nomeados.
- Valores padrão e f-strings para interpolar variáveis.
 - Chamadas podem usar argumentos posicionais ou nomeados.
"""

# Função sem parâmetros
def exibir_mensagem():
    # Corpo da função: executa uma ação (side-effect: print)
    print("Olá mundo!")


# Função com parâmetro obrigatório
def exibir_mensagem_2(nome):
    # Argumento obrigatório: deve ser fornecido na chamada
    print(f"Seja bem vindo {nome}!")


# Função com parâmetro opcional (valor padrão)
def exibir_mensagem_3(nome="Anônimo"):
    # Valor padrão usado quando o argumento não é informado
    print(f"Seja bem vindo {nome}!")


# Chamadas de função
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")  # argumento nomeado
exibir_mensagem_3()                    # usa valor padrão
exibir_mensagem_3(nome="Chappie")     # sobrescreve valor padrão
