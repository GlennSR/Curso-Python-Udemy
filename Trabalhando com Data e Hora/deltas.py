'''
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34:993932
data_final = dd/mm/yyyy 13:34:23.094884

delta data_final - data_inicial
'''

import datetime

# data atual
data_hoje = datetime.datetime.now()

# Data para o aniversário
aniversario = datetime.datetime(2021, 6, 13, 0)

# Tempo restante
tempo_para_aniv = aniversario - data_hoje

print(type(tempo_para_aniv))
print(repr(tempo_para_aniv))
print(f'Faltam {tempo_para_aniv.days} dias e {tempo_para_aniv.seconds//60//60} horas para o meu aniversário')

# Exemplo boleto
data_da_compra = datetime.datetime.now()
print(data_da_compra)

validade_boleto = datetime.timedelta(days=3)
print(validade_boleto)

vencimento_boleto = data_da_compra + validade_boleto
print(vencimento_boleto)
