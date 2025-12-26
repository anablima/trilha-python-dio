class Estudante:
    # Atributo de classe: compartilhado por todas as instâncias
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Atributos de instância: específicos de cada objeto
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

# Alterar atributo de classe reflete em instâncias que não tenham sobrescrito
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
