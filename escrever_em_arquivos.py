'''
OBS: Ao abrir um arquivo para leitura, não podemos realisar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele

OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo, utilizamos a função write().
Esta função recebe uma string como parâmetro

Abrindo um arquivo para escrita com o mode 'w', se o arquivo não existir então ele será criado,
caso ele já exista, o anterior será apagado e um novo será criado.


# Exemplo de escrita - modo 'w' - write
with open('novoTexto.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Primeira linha\n')
    arquivo.write('segunda linha\n')
    arquivo.write('Última linha')
'''

with open('Escrever_em_arquivos_texto.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Adicone uma fruta à sua lista ou digite sair: ')
        if fruta.lower() != 'sair':
            arquivo.write(fruta.capitalize() + '\n')
        else:
            break
