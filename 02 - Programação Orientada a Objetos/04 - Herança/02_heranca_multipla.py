class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        # Recebe atributos específicos e repassa demais para a superclasse
        self.cor_pelo = cor_pelo
        super().__init__(**kw)  # chama Animal.__init__ via MRO


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        # Mesmo padrão: inicializa próprio atributo e delega resto
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # Em herança múltipla, super() segue a ordem de resolução de métodos (MRO)
        # Passa argumentos nomeados que serão consumidos pelas classes na hierarquia
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
