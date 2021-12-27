"""
Forçando tipo de dados com decoradores
"""


def força_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@força_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)
        print(type(msg))


repete_msg(0, '3')
print()


@força_tipo(float, float)
def dividir(a, b):
    print(a / b)


dividir('1', 5)
