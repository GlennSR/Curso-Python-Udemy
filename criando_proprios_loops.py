"""
Criando sua própria versão de loop
"""

for num in range(1, 6):
    print(num, end=', ')
print()

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

numeros = range(1, 6)
meu_for(numeros)
