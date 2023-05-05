# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print('~≃~' * 10)
print('O computador irá escolher um número de 0 a 5!')
print('~≃~' * 10)

usuario = int(input('Tente adivinhar: ')) 
computador = randint(0, 5)

if computador == usuario:
    print('\033[32mVOCÊ VENCEU!\033[m')
else:
    print('\033[31mVOCÊ PERDEU!\033[m ')
    print('\033[33mO computador escolheu \033[34m{}!\033[m'.format(computador))
