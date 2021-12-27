"""
Nas aulas anteriores nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension...porque ele recebe o nome de Generator Expression
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']
# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
print()
# OBS: Generator ocupa menos espaço em memória que os outros, mais performático

# getsizeof() retorna a quantidade de bytes em memória o parâmetro de entrada toma
from sys import getsizeof

print(getsizeof(9))
print(getsizeof('Geek'))
print(getsizeof(99999999))
print()

# Aplicando no nosso caso de estudo
list_comp = getsizeof([x * 10 for x in range(100)])
set_comp = getsizeof({x * 10 for x in range(100)})
dict_comp = getsizeof({x: x * 10 for x in range(100)})
gen = getsizeof((x * 10 for x in range(100)))
print(f"""Tamanho ocupado em memória:
    - List Comp: {list_comp}
    - Set Comp: {set_comp}
    - Dictonary Comp: {dict_comp}
    - Generator Expression: {gen}""")

# Podemos iterar com o Generator? Sim
gen = (x * 10 for x in range(100))
for num in gen:
    print(num)

users = {'nome': 'glenio', 'idade': 22}
for v, k in users.items():
    print(v, k)
