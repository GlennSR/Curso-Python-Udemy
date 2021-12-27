"""
Decoradores (Decorators)

O que são?
- Decoradores são funções;
- Decoradores envolvem outras funções e aprimoram seus comportamentos;
- Decoradores também são exemplos de Higher Order Functions;
- Decoradores tem uma sintaxe própria, usando '@' (Syntatic Sugar / Açúcar sintático)

|-------------------------------------------|
|           Function Decorator              |
|-------------------------------------------|


|-------------------------------------------|
| |---------------------------------------| |
| |           Função decorada             | |
| |---------------------------------------| |
| |---------------------------------------| |
"""

# Decorators como funções (Sintaxe não recomendada / Sem Syntatic Sugar)
# Decorator Function
def seja_educado(funcao):
    def sendo():
        print('Foi um pazer te conhecer!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


# Decorator
def saudacao():
    print('Meu chamo Glênio')


teste = seja_educado(saudacao)
teste()
print()

# Decorators com Syntatic Sugar
def seja_educado2(funcao):
    def sendo2():
        print('Foi um pazer te conhecer!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo2


@seja_educado2
def apresentando():
    print('Meu nome é Pedro')


# Teste 1
apresentando()
print()

# Teste 2
@seja_educado2
def mariana():
    print('Meu nome é Mariana')


mariana()

# OBS: Não confundir Decorator com Decorator Function