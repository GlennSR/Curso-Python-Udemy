"""
- Geradores (Generators) são Iteradores (Iterators)

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras.

Diferenças entre Funções e Função Geradora (Generator Functions)

--------------------------------------------------------------------------------------------
| Funções                                           | Função Geradora                       |
--------------------------------------------------------------------------------------------
| utilizam return                                   | utilizam yield                        |
--------------------------------------------------------------------------------------------
| retorna uma vez                                   | podem utilizar yield múltiplas vezes  |
--------------------------------------------------------------------------------------------
| quando executada, retorna um valor                | quando executada, retorna um generator|

"""

# Exemplo de Generator Function


def conta_ate(valor_max):
    cont = 1
    while cont <= valor_max:
        yield cont
        cont += 1


# OBS: Uma Generator Function não é um Generator, ela gera um Generator
gen = conta_ate(5)
# print(list(gen))
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for num in gen:
    print(num, end=' ')
