"""
seek() -> É utilizada para movimentar o cursor pelo arquivo.
"""

arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read())

# A função seek() recebe um parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0) # seta o cursor de volta à posição zero do arquivo
print('Lendo de novo: ' + arquivo.read())

arquivo.seek(200)
print(arquivo.read())

# Leitura linha à linha
arquivo.seek(0)
linha1 = arquivo.readline()
print(linha1)
print(linha1.split(' '))
print()

# Separar cada linha como elemento de uma string
arquivo.seek(0)
print(arquivo.readlines())
print()

'''
OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Esse conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso usamos a função close()

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar o arquivo
3 - Fechar o arquivo
'''

# 1 - Abrir o arquivo
arquivo = open('texto.txt', encoding='UTF-8')

# 2 - Trabalhar o arquivo
print(arquivo.read())

# 3 - Fechar o arquivo
arquivo.close()

print('\nArquivo foi fechado? ' + str(arquivo.closed)) # Verifica se o arquivo está aberto ou fechado