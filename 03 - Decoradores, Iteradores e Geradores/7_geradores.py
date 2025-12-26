# Função geradora: usa 'yield' em vez de 'return'
# Geradores são uma forma mais simples e eficiente de criar iteradores
# Não carregam todos os valores na memória de uma vez (lazy evaluation)
def meu_gerador(numeros: list[int]):
    # Itera sobre cada número da lista
    for numero in numeros:
        # yield "pausa" a execução e retorna um valor
        # Na próxima iteração, a função continua de onde parou
        # Diferente de return, que encerra a função completamente
        # Vantagem: memória eficiente e possibilidade de sequências infinitas
        yield numero * 2


# Loop for consome o gerador
# A cada iteração, o gerador produz o próximo valor
# Saída esperada: 2, 4, 6
for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)
