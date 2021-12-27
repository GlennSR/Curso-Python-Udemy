"""
Decorators com diferentes assinaturas
"""
# Relembrando


def gritar(funcao):
    def capslock(nome):
        return funcao(nome).upper()
    return capslock


@gritar
def saudacao(nome):
    return f'Olá, meu nome é {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Teste
print(saudacao('Angelina'))

# print(ordenar('Picanha', 'Batata Frita'))
# Dá erro porque gritar() só recebe um parâmetro

# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

# -> Refatorando com a Decorator Pattern


def gritar2(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar2
def saudacao2(nome):
    return f'Olá, meu nome é {nome}'


@gritar2
def ordenar2(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


print(saudacao2('Glênio'))
print(ordenar2('Picanha', 'Batata Frita'))
print()

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma(num1, num2):
    return num1 + num2


print(soma(10, 12))  # 22
print(soma(1, 21))  # Erro

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduíche', 'pizza'))
