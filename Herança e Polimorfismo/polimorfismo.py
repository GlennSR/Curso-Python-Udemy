"""
POO - Polimorfismo

Poli -> Muitas
Morfos -> Formas

Objeto com muitas formas

Quando a gente reimplementa um método presenta na classe pai em classes filhas estamos realizando uma sobrescrita de
método (Overriding).

O Overriding é a melhor representação do polimorfismo. Cada sub classe precisa falar() de uma forma diferente, isso é o
polimorfismo
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está latindo')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} está miando')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

garfield = Gato('Garfield')
garfield.comer()
garfield.falar()

bolt = Cachorro('Bolt')
bolt.comer()
bolt.falar()

jerry = Rato('Jerry')
jerry.comer()
jerry.falar()
