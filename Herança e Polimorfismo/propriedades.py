"""
POO - Propriedades

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos a criar métodos
públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde os getters retornam
o valor do atributos e os setters alteram o valor do mesmo.
"""

class Conta:

    contador = 400

    # Encapsulando os atributos
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

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
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Glênio', 3000.00, 1500)
conta2 = Conta('Italo', 2000.00, 1500)

conta1.extrato()
conta2.extrato()

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma dos saldos das duas contas é: {soma}')

print(conta1.__dict__)
conta1.set_limite(9999999)
print(conta1.__dict__)


# Forma Python
# No Python, usa-se os chamados propriedades, decoradores @property, para criar getters e setters

class Conta2:

    contador = 400

    # Encapsulando os atributos
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta2.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta2.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    # Getter
    @property
    def limite(self):
        return self.__limite

    # Setter
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

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
        self.__saldo -= valor
        conta_destino.__saldo += valor


conta1 = Conta2('Glênio', 3000.00, 1500)
conta2 = Conta2('Italo', 2000.00, 1500)

print()
soma = conta1.saldo + conta2.saldo
print(f'A soma dos saldos das duas contas é: {soma}')

print(conta1.__dict__)
conta1.limite = 9546
print(conta1.limite)
