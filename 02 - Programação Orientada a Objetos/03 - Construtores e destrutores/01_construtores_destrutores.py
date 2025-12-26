class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        # Construtor: chamado na criação do objeto; inicializa atributos
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        # Destrutor: chamado quando o objeto é coletado/remoção da última referência
        # Não é garantido exatamente quando será chamado (depende do GC)
        print("Removendo a instância da classe.")

    def falar(self):
        # Método de instância: usa dados do objeto via 'self'
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c
# Remove referência explícita; se não houver outras, pode acionar __del__

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
