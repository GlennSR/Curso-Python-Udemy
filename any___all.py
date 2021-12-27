"""
Any e All

all() -> Retorna True se todos os elementos do iteráveis são verdadeiros ou ainda se o interável está vazio
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio any() retorna False
"""
# Exemplo all()
print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all([]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes]))
print()

# Exemplo any()
print(any([0, 1, 2, 3, 4]))
print(any([0, False, {}, (), []]))
