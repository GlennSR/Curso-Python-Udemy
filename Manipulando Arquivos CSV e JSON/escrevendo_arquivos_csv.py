"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve um linha
"""

'''
# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método writerow() para escrever
# cada linha. Este método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w', encoding='UTF-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o título do filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
'''

# DictWriter

from csv import DictWriter
from pathlib import Path

with open('filmes.csv', 'a', encoding='UTF-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)

    # Verificando se o arquivo já existe
    file_name = r'C:/Users/gleni/PycharmProjects/Curso_Python_Udemy/Manipulando Arquivos CSV e JSON/filmes.csv'
    file_obj = Path(file_name)
    if not file_obj.is_file():
        escritor_csv.writeheader() # Escreve o cabeçalho no arquivo
    filme = None
    while filme != 'sair':
        filme = input('Informe o título do filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})
