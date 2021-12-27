"""
POO - Method Resolution Order

Resolução de Ordem de Métodos em português. É a ordem de execução de métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Oi! Eu sou {self.__nome}'


class AnimalAquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Oi! Eu sou {self._Animal__nome} do mar'


class AnimalTerrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Oi! Eu sou {self._Animal__nome} da terra'


class Pinguim(AnimalTerrestre, AnimalAquatico):

    def __init__(self, nome):
        super().__init__(nome)


pinguim = Pinguim('Happy')
print(pinguim.cumprimentar())

"""
class Pinguim(AnimalTerrestre, AnimalAquatico)
print(pinguim.cumprimentar()) = Oi! Eu sou o Happy da terra

class Pinguim(AnimalAquatico, AnimalTerrestre)
print(pinguim.cumprimentar()) = Oi! Eu sou o Happy do mar
"""

print(Pinguim.__mro__)
print(Pinguim.mro())
help(Pinguim)