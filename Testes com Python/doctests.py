'''
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.
Para rodar um doctest (no terminal):
python -m doctest -v nome_do_modulo.py

'''


def soma(a, b):
    """
    Soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b


# Outro exemplo, aplicando TDD

def duplicar(valores):
    """duplica os valores de uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    """
    return [2 * elemento for elemento in valores]


# Erro inesperado...
def fala_oi():
    """
    Fala oi
    >>> fala_oi()
    'oi'
    """
    return "oi"  # Ele retorna com aspas simples na verdade

# OBS: Dentro do doctest o Python não reconhece string com aspas duplas, elas precisam usar aspas simples.

