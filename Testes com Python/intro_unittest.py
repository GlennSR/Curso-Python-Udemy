'''
Introdução ao módulo Unittest

OBS: Abrir arquivos "atividades.py" e "testes.py"

Unittest -> Testes unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos ...

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então ganhamos os 'assertions'
presentes no módulo.

Para rodar os testes utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Documentação com todos os tipos de assertions: https://docs.python.org/3/library/unittest.html

Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_

# Para executar os testes com unittest
python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose (com mais detalhes)
python nome_do_modulo.py -v

# Docstrings nos testes
Podemos acrescentar (e é recomendado) docstrings nos testes.
'''