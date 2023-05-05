# Faça um programa que leia um núemro inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))

if n % 2 != 0 and n % 3 != 0:
    print('Ele é primo!')
elif n == 2 or n == 3:
    print('Ele é primo!')
else:
    print('Pode ser divisivel por outros números')
    print('Não é primo!')
