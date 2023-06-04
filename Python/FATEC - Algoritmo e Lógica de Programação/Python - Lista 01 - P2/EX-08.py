# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

from os import system # importa o system('clear')

print('{} Fatorial de um número! {}'.format('='*10, '='*10)) # titulo

c = 1
while c == 1: # loop em caso de erro
    c = 0
    try: # tenta ler um valor
        n = int(input('Digite um número: '))
    except: # se erro
        system('clear')
        c = 1
        print('Inválido! Precisa ser um número inteiro. ')

fat = n
for c in range(n-1, 1, -1): # calcula o fatorial
    fat = fat * c

print(f'Fatorial de {n}! é igual a: {fat}')
