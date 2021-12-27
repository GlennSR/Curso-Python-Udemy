"""
Características:
- Enquanto o sort() só funciona em listas, o sorted() funciona com qualquer iterável
- Sempre retorna uma lista, não importa o iterável de entrada
- ele não muda o iterável, na verdade ele cria uma nova lista
"""

# Exemplo
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))

# Exemplo mais complexo
usuarios = [{"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
            {"username": "carla", "tweets": ["Eu amo meu gato"]},
            {"username": "jeff", "tweets": []},
            {'username': 'bob123', 'tweets': []},
            {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
            {'username': 'gal', 'tweets': []}]
print(sorted(usuarios, key=lambda user: user['tweets']))
