"""
- Métodos (funções) -> Representam o comportamento do objeto. Ou seja, as ações que
este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em dois grupos, Métodos de instância e Métodos de classe.

O método dunder init __init__ é um método especial chamado de construtor e sua função é
construir o objeto à partir da classe

OBS: Os métodos dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilisando dunder, isso não é aconselhado.
O Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo, de preferência nunca o faça
"""

# MÉTODOS DE INSTÂNCIA
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema.')

    @staticmethod
    def definicao():
        return 'Método estático'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário {self.__gera_usuario()} criado com sucesso!')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Exemplo 1
p1 = Produto('PS5', 'Video Game', 5000)
print(f'O produto PS5 vale R${p1.desconto(10)} com um desconto de 10%')
print()

# Exemplo 2
user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
print(user1.nome_completo())
print(Usuario.nome_completo(user1))
print(user1.checa_senha('12345'))
print()

'''# Exemplo 3
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirmaSenha = input('Confirme a senha: ')

if senha == confirmaSenha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criando com sucesso')
else:
    print('As senhas não conferem')
    exit()

while True:
    entrar = input('Deseja entrar na sua conta? [S/N]')
    if entrar in 'Nn':
        break
    else:
        senha = input('Informe a sua senha: ')
        if user.checa_senha(senha):
            print('Acesso permitido!')
            break
        else:
            print('Acesso negado! Senha não confere.')
'''

# MÉTODOS DE CLASSE
# OBS: Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens
user = Usuario('Brad', 'Pitt', 'bradpitt@gmail.com', '229966')

Usuario.conta_usuarios()
user.conta_usuarios()  # Forma incorreta
print()

# MÉTODOS PRIVADOS
user2 = Usuario('Terry', 'Crews', 'terry@gmail.com', '753159')
print()

# MÉTODOS ESTÁTICOS
print(Usuario.definicao())
