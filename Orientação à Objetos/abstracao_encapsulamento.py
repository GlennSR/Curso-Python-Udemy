"""
Abstração e Encapsulamento

O grande objetivo da POO é encapsular o código dentro de um grupo lógico e hierárquico utilisando
classes.

Encapsular -> Cápsula

            Classe
_______________________________
|                             |
|     atributos e métodos     |
|_____________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe, mas Python não bloqueia este acesso fora da
classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos
privados, conforme:

_Classe__elemento

Exemplo:

instancia._Pessoa__nome
instancia._Pessoa__falar()

# Abstração

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe e abstrair dados irrelevantes, escondendo
atributos e métodos privados de usuário
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando

conta1 = Conta('Glênio', 150.00, 1500)
print(conta1.__dict__)

# Como os dados são todos público, não há encapsulamento, então temos o problema de segurança, o que nos deixa fazer as
# seguintes operações
conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 9999999
conta1.limite = 9999999999
print(conta1.__dict__)

# Corrigindo

class ContaSegura:

    contador = 400

    # Encapsulando os atributos
    def __init__(self, titular, saldo, limite):
        self.__numero = ContaSegura.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ContaSegura.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisar ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor + 5  # Taxa de transferência de R$5,00

        # 2 - Adicionar valor na conta destino
        conta_destino.__saldo += valor


# Testando

print()
conta1 = ContaSegura('Glênio', 150.00, 1500)
print(conta1.__dict__)

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 9999999
conta1.limite = 9999999999
print(conta1.__dict__)

conta1.sacar(300)

conta2 = ContaSegura('Italo', 300.00, 1500)
conta2.transferir(100, conta1)
print(conta1.extrato())
print(conta2.extrato())
