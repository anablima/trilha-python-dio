# Função decoradora que adiciona comportamento antes e depois da execução
def meu_decorador(funcao):
    # Função envelope que aceita argumentos variáveis
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        # ATENÇÃO: Esta função executa a função original mas NÃO retorna seu valor
        # Se a função original retornar algo, o valor será perdido
        # Para preservar o retorno, deveria ser: return funcao(*args, **kwargs)
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    # Retorna a função envelope
    return envelope


# Aplica o decorador à função ola_mundo
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


# Chama a função decorada com dois argumentos
# O decorador intercepta a chamada e adiciona comportamento extra
ola_mundo("João", 1000)
