import os

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('geek'))
print(os.path.exists('bloco_with.py'))

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close() # Podemos usar 'a' também

# Forma 2
with open('arquivo-teste2.txt', 'w') as arquivo:
    pass
# OBS: Nenhuma dessas duas formas são as melhores para criar arquivos

# Forma melhor
# os.mknod('arquivo-teste3.txt')

# OBS: O mknod não funciona no windows, nos dá um erro AttibuteError
# OBS2: Se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios
if not os.path.exists('templates'):
    os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError
"""if not os.path.exists('/Users/gleni/template'):
    os.mkdir('/Users/gleni/template')"""

# Criando multiplos diretórios (árvore de diretórios)
# os.mkdir('pasta1/subpasta') O mkdir() não consegue criar mais de um diretório de uma vez
# Para isso usamos makedirs()
os.makedirs('pasta1/subpasta1/subsubpasta1', exist_ok=True)
# O parâmetro 'exist_ok=True' garante que se o diretório já existir então o program ignora o comando
# e não apresenta o erro

# Renomear arquivos e diretórios
if not os.path.exists('mydir'):
    os.rename('templates', 'mydir')

if not os.path.exists('pasta1/subpasta1/subsubpasta2'):
    os.rename('pasta1/subpasta1/subsubpasta1', 'pasta1/subpasta1/subsubpasta2')

# Deletar arquivos
# ATENÇÃO! Tomar cuidado quando deletar um arquivo, pois eles não vão para a lixeira, eles são excluídos permanentemente
os.remove('arquivo-teste.txt')
# OBS: Essa função só serve para remover arquivos, não diretórios

# Deletar diretórios vazios
os.rmdir('templates')
# OBS: Se o diretório não estiver vazio teremos um OSError

# Removendo uma árvore de diretórios vazios
os.removedirs('pasta1/subpasta1/subsubpasta2')

# Trabalhando com arquivos e diretórios temporários
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Diretório temporário criando em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
# O diretório é criado na pasta C:\Users\gleni\AppData\Local\Temp do sistema, ou seja,
# ele é deletado assim que o with termina

with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write(b'Geek University\n')
    tmpfile.seek(0)
    print(tmpfile.read())
    print()
# b'' converte a string para binário, pois para arquivos temporário só podemos escrever em binário

with tempfile.NamedTemporaryFile() as tmpfile:
    tmpfile.write(b'Geek University\n')
    print(tmpfile.name)
    input()
