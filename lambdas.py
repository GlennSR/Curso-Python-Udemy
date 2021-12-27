"""
São funções sem nome, ou seja, funções anônimas

# Função em Python:
def funcao(x):
    return 3 * x + 1
"""

# Expressão lambda
lambda x: 3 * x + 1

# Utilização:
calc = lambda x: 3 * x + 1

print(calc(4))


# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('glênio', 'SIMIÃO ramalho'))

# Em funções podemos ter nenhuma ou várias entradas, em Lambdas também
amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn: <expressão>
print()
print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Outro Exemplo
autores = ['Isaac Asimov', 'Ray Bradburry', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card']
print()
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split()[-1].lower())
print(autores)

# Exemplo função quadrática
# Definindo a função:
def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print()
print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(2, 3, -5)(2))
