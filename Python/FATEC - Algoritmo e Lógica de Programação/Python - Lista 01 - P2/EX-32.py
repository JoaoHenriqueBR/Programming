'''
Faça um programa que mostre os n termos da Série a seguir:

a. S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

Imprima no final a soma da série.
'''

from os import system

n = 0
while n <= 0:
    try:
        n = int(input('Número de termos da série: '))
    except:
        n = -1
    if n > 0:
        break
    system('clear')
    print('Número Inválido! Precisa ser inteiro e positivo.')

soma = 0
for c in range(n):
    serie = c*2+1
    print(f'S = {c+1}/{serie}')
    soma += serie 

print(f'Soma: {soma}')
