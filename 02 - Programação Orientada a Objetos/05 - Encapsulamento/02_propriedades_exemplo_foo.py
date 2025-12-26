class Foo:
    def __init__(self, x=None):
        # Atributo "protegido" por convenção (uso interno)
        self._x = x

    @property
    def x(self):
        # Getter: expõe valor calculado; se None/0, retorna 0
        return self._x or 0

    @x.setter
    def x(self, value):
        # Setter: ajusta o valor somando ao atual
        self._x += value

    @x.deleter
    def x(self):
        # Deleter: "reseta" o valor para 0
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
