'''
r -> Abre para leitura
w -> Abre para escrita - sobrescreve caso o arquivo já existir
x -> Abre para escrita somente se o arquivo não existir
a -> Abre para a escrita, adicionando o conteúdo ao final do arquivo
+ -> Abre para o modo de atualização: Leitura e Escrita

http://docs.python.org/3/library/functions.html#open
'''

# Exemplo 'x'
try:
    with open('modos_abertura_arquivo_texto.txt', 'x') as arquivo:
        arquivo.write('Teste 1')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo 'a'
# OBS: nesse modo o conteúdo será adicionado sempre ao final do arquivo, ou seja, não podemos controlar o cursor
with open('modos_abertura_arquivo_frutas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Adicone uma fruta à sua lista ou digite sair: ')
        if fruta.lower() != 'sair':
            arquivo.write(fruta.capitalize() + '\n')
        else:
            break

# Exemplo '+': deve ser usado com outro modo, seja 'a', 'r', 'w'
with open('modos_abertura_arquivo_texto.txt', 'a+', encoding='UTF-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('Linha 0\n')
    arquivo.write('linha 1\n')
