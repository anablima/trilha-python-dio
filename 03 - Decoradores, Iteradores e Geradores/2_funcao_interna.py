# Função externa (principal) que contém funções aninhadas
def principal():
    print("executando a funcao principal")

    # Primeira função interna (aninhada)
    # Esta função só existe no escopo da função principal
    def funcao_interna():
        print("executando a funcao interna")

    # Segunda função interna (aninhada)
    # Também existe apenas no escopo da função principal
    def funcao_2():
        print("executando a funcao 2")

    # Chamando as funções internas dentro da função principal
    # Elas só podem ser chamadas aqui, não fora de 'principal()'
    # Poderíamos retornar uma função interna para criar uma closure
    funcao_interna()
    funcao_2()


# Chamada da função principal
# Isso executará a função principal e suas funções internas
principal()
