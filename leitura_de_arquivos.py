"""
Leitura de arquivos

Para abrir o conteúdio de um arquivo em Python, utilizamos a função intergrada open()

doc: https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos o erro FileNotFoundError
"""

# Exemplo

arq = open('texto.txt', encoding='UTF-8')
print(arq)
print(type(arq))

# Para ler o conteúdo do arquivo, após sua abertura, utilisamos a função read()
conteudo = arq.read()
print(conteudo)
print(type(conteudo)) # String
print(arq.read()) # Não imprime nada, por quê?

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona
# como o cursor que estamos escrevendo, o primeiro print() lê o arquivo e termina com o cursor situado
# no final do último caractere então quando escrevemos o segundo print() o cursor não vai ler mais
# nada pois ele está no final do arquivo e não tem mais conteúdo pra ler
