"""
PDB -> Python Debugger

# OBS: A utilização do print() para debuggar é uma prática ruim

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))
"""

# A utilização do debugger é uma forma mais profissional de fazer isso
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com PyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo 1 com PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado
# como função built-in chamada breakpoint

# Comando básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 2

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas no
# início do arquivo. Por isso, ao invés de colocarmos o import do pdb no inìcio do arquivo nós colocamos
# somente onde vamos debuggar, e ao final já fazemos a remoção

# Exemplo 3

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os camandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Com os nomes das variáveis são os mesmos dos comandos do pdb, devemos usar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variável