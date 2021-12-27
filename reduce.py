"""
Obs: À partir do Python3+ a função reduce() não é mais uma função built-in, agora ela tem que ser importada.
Isso foi feito porque um loop for é mais legível.

Para entender o reduce():
Assim comos os anteriores, ele também recebe uma função e um iterável, sendo que a função
tem que ser uma função que receba dois parâmetros, exemplo:

def funcao(x, y):
    return x * y

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiro parâmetros
    Passo 2: res2 = f(res1, a3) # Aplica a função no resultado anterior e o próximo parâmetro
    ...
    Isso é repetido até o final dos elementos do iterável
"""

from functools import reduce

# Exemplo 1
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)
