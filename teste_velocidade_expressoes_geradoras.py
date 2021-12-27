"""
Teste de velocidade com Expressões Geradoras
"""

# Generators


def nums():
    for n in range(1, 10):
        yield n


ge1 = nums()
print(ge1)

# Generator Expression
ge2 = (num for num in range(1, 10))
print(ge2)  # Generator Expression

# Realizando o teste de velocidade
import time

# Generator Expression
gen_ini = time.time()
print(sum(n for n in range(1, 60000000)))
gen_tempo = time.time() - gen_ini

# List Comprehension
list_ini = time.time()
print(sum([n for n in range(1, 60000000)]))
list_tempo = time.time() - list_ini

print(f'Generator Expression levou {gen_tempo}s')
print(f'List Comprehension levou {list_tempo}s')