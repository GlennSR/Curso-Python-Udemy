"""
Utilizando List Comprehension nós podemos gerar novas listas com dados processados à partir de outro
iterável.
"""

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

# List Comprehension vs Loop

numeros = [1, 2, 3, 4, 5]
# Loop
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Outros exemplos
# Exemplo 1
nome = 'Geek University'
print([letra.upper() for letra in nome])

# Exemplo 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 3
print([numero * 3 for numero in range(1, 10)])

# Exemplo 4
print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])

# Exemplo 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
