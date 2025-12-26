# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra conceitos fundamentais de Programação Orientada a Objetos
# usando uma classe Bicicleta como exemplo
# Demonstra:
# 1. Definição de classe
# 2. Método construtor
# 3. Atributos de instância
# 4. Métodos de instância
# 5. Método especial __str__
# 6. Criação e uso de objetos

# Definição da classe Bicicleta
class Bicicleta:
    # Classe: "molde" para criar objetos (instâncias) com estado e comportamento
    # Método construtor: inicializa um novo objeto
    # self é uma referência ao próprio objeto sendo criado
    def __init__(self, cor, modelo, ano, valor):
        # Atributos de instância
        # Parâmetros recebidos viram estado interno via 'self'
        self.cor = cor      # Cor da bicicleta
        self.modelo = modelo  # Modelo (marca/tipo)
        self.ano = ano      # Ano de fabricação
        self.valor = valor  # Valor em reais

    # Métodos de instância: definem o comportamento do objeto
    # Usam 'self' para acessar o estado e executar ações
    def buzinar(self):
        print("Plim plim...")  # Simula o som da buzina

    def parar(self):
        # Método com múltiplas ações
        print("Parando bicicleta...")  # Início da parada
        print("Bicicleta parada!")     # Confirmação da parada

    def correr(self):
        print("Vrummmmm...")  # Simula o som do movimento

    # Método especial __str__: representação em string do objeto
    # Chamado automaticamente por print() e str()
    def __str__(self):
        # Usa compreensão de lista para formar string com todos os atributos
        # self.__class__.__name__ pega o nome da classe; self.__dict__ traz atributos/valores
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Criação e uso de objetos da classe Bicicleta

# Criando primeira bicicleta
# Instanciação: chama __init__ com os argumentos informados
b1 = Bicicleta("vermelha", "caloi", 2022, 600)  # Instanciação do objeto
# Chamadas de método demonstram comportamentos da instância
b1.buzinar()  # Chamada de método
b1.correr()   # Chamada de método
b1.parar()    # Chamada de método
# Acesso direto aos atributos
# Leitura de atributos de instância (estado atual do objeto)
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criando segunda bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)
# print(b2) chama implicitamente __str__ para exibir uma representação amigável
print(b2)     # Chama implicitamente __str__
b2.correr()   # Chamada de método
