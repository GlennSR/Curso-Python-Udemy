"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System
"""

import os

# getcwd() -> Pega o diretório de trabalho corrent - current work directory
print(os.getcwd()) # C:\Users\gleni\PycharmProjects\Curso_Python_Udemy

# Para mudar de diretório podemos usar o chdir()
os.chdir('..') # C:\Users\gleni\PycharmProjects
print('\nVoltar um diretório')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
print()
os.chdir('/Users/gleni/PycharmProjects/Curso_Python_Udemy')

# Podemos checar se um diretório é o absoluto ou o relativo
print('Is absolute path?', os.path.isabs('C:/Users/gleni'))
print('Is absolute path?', os.path.isabs('C:\\Users\\gleni'))
print('Is absolute path?', os.path.isabs('/Users/gleni'))
# Podemos usar esses três modos acima para paths no windows

print('Is absolute path?', os.path.isabs('Users/gleni'))
print()

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # nt -> windows

# Ou podemos usar também o módulo sys
import sys
print(sys.platform)
print()
# Podemos ter mais detalhes do sistema operacional
# print(os.uname()) -> NÃO FUNCIONA PARA WINDOWS

# Criação de arquivos ou pastas
# Exemplo: criar a pasta 'sistema_de_arquivos_pasta' no diretório corrente
diretorio = os.path.join(os.getcwd(), 'geek')
print(os.getcwd())
os.chdir(diretorio)
print(os.getcwd())

# Podemos listar os arquivos e diretórios com o listdir()
# Essa função nos retorna uma lista contendo os nomes e extensões dos arquivos no diretório
print(os.listdir('..'))
print(len(os.listdir('..')), 'arquivos')
print()

# Podemos também usar o scandir() para listar os arquivos com mais detalhes
scanner = os.scandir('..')
arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[1].is_dir())

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim como quando abrimos um arquivo
scanner.close()
