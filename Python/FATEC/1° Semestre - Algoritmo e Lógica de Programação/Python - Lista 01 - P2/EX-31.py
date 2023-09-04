# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

from os import system

n = 0
while n <= 0:
    try:
        n = int(input('Digite um número: '))
    except:
        n = -1
    if n > 0:
        break
    system('clear')
    print('Número Inválido! Precisa ser inteiro e positivo.')

num = str(n)
invertido = ''
for c in range(len(num), 0, -1):
    invertido += num[c-1]
    
print(invertido)
