'''
Testes Automatizados!

        Aplicação Web
-------------------------------
|                             |
|      frontend e backend     |
|                             |
-------------------------------
|    testes automatizados     |
-------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos
    - Testes garantem que bugs que foram corrigidos anteriormente continuem corrigidos
    - Testes garantem que a refatoração que costumamos fazer não traga novos bugs.

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)
Com o TDD são utilizado estágios de desenvolvimento:
    - Você escreve o seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo.

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor.
'''

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
