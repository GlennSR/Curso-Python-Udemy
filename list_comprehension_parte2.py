"""
Nós podemos adicionar estruturas condicionais às nossas List Comprehension
"""

# Exemplos

# Exemplo 1
numeros = range(1, 7)

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Outra forma: usando not
# Qualquer número par módulo 2 é 0 e 0 é false por isso o if not
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo 2 é 1 e 1 é true
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
