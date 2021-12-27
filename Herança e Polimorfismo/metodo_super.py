"""
POO - O método super()

O método super() se refere à Super Classe
"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} ({self.__especie}) faz {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)  # O método super() descarta o uso do self
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')