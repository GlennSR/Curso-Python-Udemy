"""
Características:
- Inverted a posição dos elementos de uma lista
- Enquanto reverse() só funciona com listas, reversed() funciona com todos os iteráveis
"""

# Exemplo
numeros = [6, 1, 8, 2]
res = reversed(numeros)

# Lista
print(list(reversed(numeros)))

# Tupla
print(tuple(reversed(numeros)))

# Conjunto (Set)
print(set(reversed(numeros)))
# OBS: Em sets, não definimos a ordem dos elementos
print()

# Inverter uma palavra
print(''.join(list(reversed('Geek University'))))
# Maneira mais fácil
print('Geek University'[::-1])
