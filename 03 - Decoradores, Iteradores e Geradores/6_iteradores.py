# Classe que implementa o protocolo de iterador personalizado
# Para ser um iterador, a classe deve implementar __iter__ e __next__
class MeuIterador:
    # Construtor: inicializa a lista de números e o contador
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0  # Controla a posição atual na iteração

    # Método __iter__ retorna o próprio objeto iterador
    # É chamado quando usamos o objeto em um loop for
    def __iter__(self):
        return self

    # Método __next__ retorna o próximo valor da iteração
    # É chamado automaticamente em cada ciclo do loop for
    def __next__(self):
        try:
            # Obtém o número na posição atual
            numero = self.numeros[self.contador]
            # Incrementa o contador para a próxima iteração
            self.contador += 1
            # Retorna o número multiplicado por 2
            return numero * 2
        except IndexError:
            # Quando não há mais elementos, lança StopIteration
            # Isso sinaliza ao Python que a iteração terminou
            # Obrigatório para iteradores: encerra o loop for
            raise StopIteration


# Loop for usa o iterador personalizado
# Para cada elemento, imprime o valor dobrado
# Saída esperada: 76, 26, 22
for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)
