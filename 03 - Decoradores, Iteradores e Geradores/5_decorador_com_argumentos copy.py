# Função decoradora que aceita funções com argumentos
def meu_decorador(funcao):
    # Função envelope que aceita qualquer número de argumentos
    # *args: argumentos posicionais variáveis
    # **kwargs: argumentos nomeados variáveis
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        # Executa a função original passando todos os argumentos recebidos
        # Captura o resultado para poder retorná-lo depois
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        # Retorna o resultado da função original
        return resultado

    # Retorna a função envelope que mantém a assinatura flexível
    return envelope


# Aplica o decorador a uma função que recebe múltiplos argumentos
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    # Retorna o nome em maiúsculas
    return nome.upper()


# Chama a função decorada com argumentos
# O decorador intercepta a chamada, executa código antes e depois
resultado = ola_mundo("João", 1000)
# Imprime o resultado retornado pela função original (JOÃO)
print(resultado)
# Imprime informações sobre a função (mostra que é a função envelope)
# Para preservar metadados da função original, use @functools.wraps (veja 5.1)
print(ola_mundo)
