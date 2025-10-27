# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra o conceito básico de decoradores em Python
# Decoradores são funções que modificam o comportamento de outras funções
# Demonstra:
# 1. Funções como objetos de primeira classe
# 2. Funções aninhadas (closures)
# 3. Decoração manual de funções
# 4. Conceito de wrapper/envelope

# Definição do decorador
def meu_decorador(funcao):
    # Função interna que envolve (wrap) a função original
    def envelope():
        # Código executado ANTES da função decorada
        print("faz algo antes de executar")
        
        # Chamada da função original
        funcao()
        
        # Código executado DEPOIS da função decorada
        print("faz algo depois de executar")

    # Retorna a função envelope (não a executa)
    return envelope


# Função que será decorada
def ola_mundo():
    print("Olá mundo!")  # Função simples que apenas imprime uma mensagem


# Decoração manual da função (equivalente a usar @meu_decorador)
# 1. Passa ola_mundo como argumento para meu_decorador
# 2. Reatribui o resultado (função envelope) à variável ola_mundo
ola_mundo = meu_decorador(ola_mundo)

# Chamada da função decorada
# Na verdade, chama a função envelope que:
# 1. Imprime "faz algo antes"
# 2. Chama a função original
# 3. Imprime "faz algo depois"
ola_mundo()
