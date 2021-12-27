'''
Métodos de Data e Hora

'''

import datetime

# Com now() podemos especificar uma timezone (Fuso Horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))
print()

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
print()


# Mudanças ocorrendo à meia-noite combine()
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
# datetime.time() zera a hora
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
print()

# Encontrar o dia da semana: weekday()

# Os dias da semana do método weekday() começam em 0, sendo este segunda-feira
# 0 - Segunda-feira
# 1 - Terça-feira
# 2 - Quarta-feira
# 3 - Quinta-feira
# 4 - Sexta-feira
# 5 - Sábado
# 6 - Domingo

print(manutencao.weekday())
print()

''''# Recebendo dados do usuário e convertendo para data
aniversario = input('Digite a sua data de nascimento (DD/MM/AAAA): ').split('/')
aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo')
print()'''


# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:min
hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # com y ele retorna os dois últimos dígitos do ano
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%m/%y')
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%B/%y')
print(hoje_formatado)
print()

# Para mais opções, olhar documentação


# Traduzindo a formatação para Português com a biblioteca textblob
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


print(formata_data(hoje))
print()

# Método strptime: Converte string em datetime
nascimento = datetime.datetime.strptime('13/06/1998', '%d/%m/%Y')
print(nascimento)


# Método time(): Trabalhar com hora
almoco = datetime.time(12, 30, 0)
print(almoco)
print()


# Método timeit(): Marcando o tempo de execução do código
import timeit

# Loop for
tempo = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)
print('Loop for', tempo)

# List Comprehension
tempo = timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000)
print('List Comprehension:', tempo)

# Map
tempo = timeit.timeit("'-'.join(map(str, range(100)))", number=10000)
print('Map:', tempo)

n = '-'.join(map(str, range(100)))
print(n)

# Usando com a função functools
import functools

def soma(n):
    soma = 0
    for num in range(n * 200):
        soma += num ** num + 4
    return soma


print(timeit.timeit(functools.partial(soma, 2), number=10000))
