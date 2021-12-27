"""
Escrevendo um iterador customizado
"""

class Contador:
    def __init__(self, menor, maior): # self é usado sempre numa função criada dentro de uma classe
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


con = Contador(1, 61)

print(con.menor)
print(con.maior)

'''it = iter(con)
while True:
    try:
        print(next(it))
    except StopIteration:
        break'''
for n in Contador(1, 61):
    print(n, end=' ')


