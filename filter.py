"""
Filter serve para filtrar dados de uma determinada coleção
"""
from statistics import mean

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = mean(dados)
print(media)

# Obs: Assim como a função map(), filter() recebe dois parâmetros
# sendo eles uma função e um iterável
res = filter(lambda x: x > media, dados)
print(list(res))
print(type(res))
print()
# Obs: Assim como o map(), os dados aqui também são deletados após o uso

# Exemplo 2
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# paises = filter(lambda p: p != '', paises)
paises = filter(None, paises)
print(list(paises))

# Exemplo 3
usuarios = [{"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
            {"username": "carla", "tweets": ["Eu amo meu gato"]},
            {"username": "jeff", "tweets": []},
            {'username': 'bob123', 'tweets': []},
            {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gal', 'tweets': []}]
# Filtrar os usuários que estão inativos no Twitter
activeUsers = filter(lambda user: user['tweets'] != [], usuarios)
inactiveUsers = filter(lambda user: not user['tweets'], usuarios)
print(list(activeUsers))
print(list(inactiveUsers))
print()

# Exemplo 4: Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']
# Criar uma lista contendo 'Sua instrutora é' + nome, sendo que o nome não pode ter mais de 5 letras
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
