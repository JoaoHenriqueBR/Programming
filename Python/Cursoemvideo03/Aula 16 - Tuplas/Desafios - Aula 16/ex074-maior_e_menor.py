'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.
'''

from random import randint


tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Foram sorteados: ', end='')
for n in tupla:
    print(f'{n} ', end='')

print('')
print(f'Maior: {max(tupla)}')
print(f'Menor: {min(tupla)}')
