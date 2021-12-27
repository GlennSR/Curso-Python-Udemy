"""
Com map, fazemos mapeamento de valores para função
"""
import math

def area(r):
    return math.pi * (r ** 2)

raios = [2, 5, 7.1, 0.3, 10, 44]
# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)
print()

# Forma 2 - com map
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))
print()

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Obs: Após utilizar a função map() depois da primeira utilização do resultado, ele zera para liberar memória

# Outro exemplo: Conversão de escala de temperatura
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)

c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)
print(list(map(c_para_f, cidades)))
