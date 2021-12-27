"""
Atributos -> Representam as características do objeto, seus estados.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos.

# Atributos de instância: São atributos declarados dentro do método construtor.
OBS: Método construtor: É um método especial utilizado para a construção do objeto.

- Exemplo de classe em Java:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}
OBS: Podemos ver que em Java existem atributos com diferentes níveis de segurança

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo undescore no início de seu nome
Isso é conhecido também como Name Mangling.

"""

# CLASSES EM PYTHON:
# Classes com Atributos de Instância Públicos
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classe com Atributos Privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

# Exemplo
user = Acesso('user@gmail.com', '12345')

print(user.email)
# print(user.__senha)  # AttributeError
print('dir: ', dir(user))
print(user._Acesso__senha) # MangLing
user.mostra_senha()
print()

# O que significa atributos de instância?
# Significa que qo criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@hotmail.com', '987654')

user1.mostra_senha()
user2.mostra_senha()
print()


# ATRIBUTOS DE CLASSE

# Atributos de classe são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já
# inicializados com um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de
# cada instância da classe ter seus próprios valores, como é o caso dos atributos de instância, com os atributos de
# classe todas as instâncias terão o mesmo valor para este atributo.


# Refatorando a classe Produto

class Produto:
    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador += 1


p1 = Produto('Playstation 5', 'Video Game', 2300)
p2 = Produto('Xbox Series X', 'Video Game', 4500)

print(f'{p1.nome} vale {p1.valor} com um imposto de {p1.imposto}')
print(f'{p2.nome} vale {p2.valor} com um imposto de {p2.imposto}')
print(p1.id)
print(p2.id)
print()


# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto)  # Acesso correto de um atributo de classe
print()
# OBS: Em linguages como o Java, esse 'atributos de classe' são conhecidos como 'atributos estáticos'


# ATRIBUTOS DINÂMICOS -> Um atributo de instância que pode ser criado em tempo de execução

# OBS: Um atributo dinâmico será exclusivo da instância que o criou

p1 = Produto('Playstation 5', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução
p2.peso = '5kg'  # Note que na classe Produto não existe o atributo 'peso'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Preço: {p2.valor}, Peso: {p2.peso}')
print()

# DELETANDO ATRIBUTOS
# Podemos remover atributos de uma classe sendo eles dinâmicos ou mesmo de instância
print(p1.__dict__)
print(p2.__dict__)
# print(Produto.__dict__)

del p2.peso  # Deleta o atributo dinâmico 'peso'
del p2.valor  # Deleta o atributo de instância 'valor'
print(p2.__dict__)
