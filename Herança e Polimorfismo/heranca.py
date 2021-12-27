"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código e também extender as classes

OBS: Com a herança, à partir de uma classe existente nós extendemos outra classe que passa a herdar atributos e métodos
da classe herdada

Exemplo: Nós temos duas classes com diversos parâmetros iguais

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

"""

# FORMA ANTIGA: Sem herança

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Testando
cliente1 = Cliente('Glênio', 'Simião', '123.456.789-00', 5000)
funcionario1 = Funcionario('Ítalo', 'Lucas', '987.654.321-11', 12340)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# FORMA NOVA: Usando herança
'''
OBS: Quando uma classe herda de outra, ela herda TODOS os atributos e métodos da classe herdada

Quanto à nomenclatura, a classe herdada é conhecida por:
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica
    
A classe que herda uma outra é conhecida por:
    - Sub Classe
    - Classe Filha
    - Classe Específica
'''


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Client herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


# Testando
print()
cliente1 = Cliente('Glênio', 'Simião', '123.456.789-00', 5000)
funcionario1 = Funcionario('Ítalo', 'Lucas', '987.654.321-11', 12340)
print(cliente1.nome_completo())
print(funcionario1.nome_completo())


# SOBRESCRITA DE METODOS (Overriding)
# Ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Client herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return  f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


print()
cliente1 = Cliente('Glênio', 'Simião', '123.456.789-00', 5000)
funcionario1 = Funcionario('Ítalo', 'Lucas', '987.654.321-11', 12340)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
