"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilisam dunder.

dunder init -> __init__

Dunder -> Double Underscore

# Método Mágico Representation -> Representação do objeto (para os desenvolverdores)
def __repr__(self):
    return f'"{self.titulo}" escrito por {self.autor}'

# Dunder string -> Representação do objeto (para os usuários)
def __str__(self):
    return f'"{self.titulo}" escrito por {self.autor}'

OBS: Caso os dois existam numa classe, o __str__ será prioritário sobre o __repr__

# Dunder length -> Retorno da função len() aplicada ao objeto

# Dunder delete -> Retorna algo quando a função del() é aplicada

# Dunder add -> Retorna algo quando obj1 + obj2 é aplicado
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'"{self.titulo}" escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'O objeto {self} foi deletado da memória')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Tipo de outro não é int'

livro1 = Livro('Sou Lindo!', 'S. RAMALHO Glênio', 400)
livro2 = Livro('Por que sou lindo?', 'S. RAMALHO Glênio', 350)

print(livro1)
print(livro2)
print()

print(repr(livro1))
print(str(livro1))
print()

print(f'O livro 1 tem {len(livro1)} pág.')
print(f'O livro 2 tem {len(livro2)} pág.')
print()

print(livro1 + livro2)
print()

print(livro1 * 3)
print()

del()
