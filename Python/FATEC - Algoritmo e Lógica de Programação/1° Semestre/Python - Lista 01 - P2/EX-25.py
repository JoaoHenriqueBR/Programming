'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo
'''

from os import system

n = 0
XXIV = 0
L = 0
LXXIV = 0
C = 0
while n >= 0:
    try:
        n = int(input('Digite um número: '))
    except:
        system('clear')
        print('Número inválido! Tente novamente')
        continue
    if n < 0:
        break
    elif n <= 25:
        XXIV += 1 
    elif n <= 50:
        L += 1
    elif n <= 75:
        LXXIV += 1
    elif n <= 100:
        C += 1

print(f'[0-25]: {XXIV} números.')
print(f'[26-50]: {L} números.')
print(f'[51-75]: {LXXIV} números.')
print(f'[76-100]: {C} números.')
