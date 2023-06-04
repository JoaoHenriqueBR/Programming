# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

from os import system

c = 1
while c == 1: # loop em caso de erro
    c = 0
    try: # tenta ler um valor
        n = int(input('Digite um número inteiro: '))
    except: # se erro
        system('clear')
        c = 1
        print('Inválido! Precisa ser um número inteiro. ')

if n % 2 != 0 and n % 3 != 0:
    print('Ele é primo!')
elif n == 2 or n == 3:
    print('Ele é primo!')
else:
    print('Pode ser divisivel por outros números')
    print('Não é primo!')
