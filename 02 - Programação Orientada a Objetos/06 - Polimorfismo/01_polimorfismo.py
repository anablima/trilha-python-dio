class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        # Sobrescreve comportamento: mesma interface, ação diferente
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        # Polimorfismo: a chamada a 'voar' depende do tipo concreto
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        # Duck typing seria suficiente; herança aqui não representa relação "é um"
        print("Avião está decolando...")


def plano_voo(obj):
    # Aceita qualquer objeto com método 'voar' (polimorfismo/duck typing)
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
