# Função decoradora: recebe uma função como parâmetro e retorna uma versão modificada dela
def meu_decorador(funcao):
    # Função envelope (wrapper): adiciona comportamento antes e depois da função original
    def envelope():
        print("faz algo antes de executar")
        # Executa a função original
        funcao()
        print("faz algo depois de executar")

    # Retorna a função envelope que "envolve" a função original
    return envelope


# Sintaxe do decorador (açúcar sintático)
# O @meu_decorador é equivalente a: ola_mundo = meu_decorador(ola_mundo)
# Aplica o decorador à função, adicionando funcionalidade extra
@meu_decorador
def ola_mundo():
    print("Olá mundo!")


# Chama a função decorada
# Isso executará o envelope que contém a função original
ola_mundo()
