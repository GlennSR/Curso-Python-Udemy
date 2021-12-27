'''
O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with

Por exemplo:
Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar o arquivo
3 - Fechar o arquivo
'''

with open('texto.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())
    print('\n(Dentro do with) Arquivo foi fechado? ' + str(arquivo.closed))

print('\n(Fora do with) Arquivo foi fechado? ' + str(arquivo.closed))
# O bloco with fecha o arquivo automaticamente após sua execução
