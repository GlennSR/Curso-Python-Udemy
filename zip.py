"""
zip() -> Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares
"""

# Exemplos

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zip1 = zip(list1, list2)
print(zip1)
print(type(zip1))

print(list(zip1))

zip1 = zip(list1, list2, 'abc')
print(tuple(zip1))

zip1 = zip(list1, list2, 'abc')
print(set(zip1))

zip1 = zip(list1, list2)
print(dict(zip1))
print()

# Exemplo 2
list3 = [7, 8, 9, 10, 11]
# Nesse caso de iteráveis de tamanho diferente, o zip gera um resultado com o tamanho do menor iterável e ignora os
# outros valores
zip1 = zip(list1, list2, list3)
print(list(zip1))
print()

# Exemplo 3: Podemos utilizar diferentes tipos de iteráveis com o zip()
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario)
print(list(zt))
print()

# Exemplo 4: Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
print()

# Exemplo mais complexo

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map() para isso

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
