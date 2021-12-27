from collections import namedtuple

# Declaração

# Forma 1
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2
print(ray.idade)
print(ray.raça)
print(ray.nome)
