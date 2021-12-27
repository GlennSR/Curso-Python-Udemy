'''
Manipulando Data e Hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime
'''

import datetime

print(dir(datetime))

# Retorna a data e hora corrente
print(datetime.datetime.now())

# datetime.datetime(YYYY, MM, DD, Hour, Minute, Second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para ajustar a data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horário para 16 h, 0 min, 0 s, 0 microsecond
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
print()

# Recebendo dados do usuário e convertendo para data
nascimento = input('Digite a sua data de nascimento (DD/MM/AAAA): ').split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))

# Acesso individual dos elementos de data e hora
evento = datetime.datetime.now()

print()
print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)
# e assim em seguida até microsegundos
print(dir(evento))
