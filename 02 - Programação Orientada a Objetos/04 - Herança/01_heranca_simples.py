"""
Herança simples em POO:
- `Veiculo`: classe base com atributos e métodos comuns.
- `Motocicleta` e `Carro`: herdam de `Veiculo` sem alterações.
- `Caminhao`: herda de `Veiculo` e adiciona atributo/comportamento próprio.
"""


class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        # Atributos de instância
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        # Comportamento comum a todos os veículos
        print("Ligando o motor")

    def __str__(self):
        # Representação textual: nome da classe e seus atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    # Herda comportamento e atributos de Veiculo
    pass


class Carro(Veiculo):
    # Herda comportamento e atributos de Veiculo
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # Chama construtor da classe base para inicializar parte comum
        super().__init__(cor, placa, numero_rodas)
        # Atributo específico de Caminhao
        self.carregado = carregado

    def esta_carregado(self):
        # Comportamento específico usando operador ternário
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Instanciando objetos das classes derivadas
moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

# Impressão amigável via __str__
print(moto)
print(carro)
print(caminhao)
