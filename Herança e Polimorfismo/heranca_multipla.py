"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe
filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta
    - Por Multiderivação Indireta

OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e
métodos das Super Classes.
"""

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2: Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass


# Caso real

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


# Testando
baleia = AnimalAquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = AnimalTerrestre('Bola')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Happy')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())  # Oi! Eu sou Happy da terra - Method Resolution Order (MRO)
# Ele printa o método da primeira classe mãe da classe Pinguim


# Objeto é instância de ...
print()
print(f'Happy é instância de Pinguim? {isinstance(pinguim, Pinguim)}')  # True
print(f'Happy é instância de AnimalAquatico? {isinstance(pinguim, AnimalAquatico)}')  # True
print(f'Happy é instância de AnimalTerrestre? {isinstance(pinguim, AnimalTerrestre)}')  # True
print(f'Happy é instância de Animal? {isinstance(pinguim, Animal)}')  # True
print(f'Happy é instância de object? {isinstance(pinguim, object)}')  # True
