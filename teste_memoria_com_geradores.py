"""
Teste de memória com Generators

# Exemplo: Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13 ...
"""

# Função usando listas
def fibonacci(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função usando Generator
def fibonacci_gen(max):
    a, b = 0, 1
    count = 0
    while count < max:
        yield b
        a, b = b, a + b
        count += 1


# Teste
for n in fibonacci(10):
    print(n, end=', ')
print()

print(list(fibonacci_gen(100)))
