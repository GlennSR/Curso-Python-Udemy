"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, Youtube, Instagram...)
e terceiros (nós desenvolvedores).

# Intergrando o JSON com o Pickle

pip install jsonpickle

"""

import json

# Exemplo
ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', 2340)}])

print(type(ret))
print(ret)
print()

# Exemplo prático
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)
print()


# Exemplo integrando JSON com Pickle

import jsonpickle

ret = jsonpickle.encode(felix)
print(ret)
print()

# Escrevendo o arquivo json/pickle

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo o arquivo json/pickle

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
