# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120

# Método Convencional (While)

n = int(input('Digite um número: '))
c = n
fat = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print(fat)

# Método prático (Biblioteca Math)

from math import factorial

print('')
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'O fatorial de {n} é {fat}.')
