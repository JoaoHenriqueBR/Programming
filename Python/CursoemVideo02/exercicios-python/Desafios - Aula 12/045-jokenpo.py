# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('~=~'*10)
print('JOKÊNPO contra o Computador! ')
print('~=~'*10)

vc = int(input('''[ 1 ] para PEDRA
[ 2 ] para TESOURA
[ 3 ] para PAPEL
Escolha um: '''))

cpu = randint(1, 3)
jokenpo = {1:'PEDRA',
           2:'TESOURA',
           3:'PAPEL'}

if vc >= 4 or vc == 0:
    print('OPÇÂO INVÁLIDA! Tente novamente!')
else:
    print('JO')
    sleep(1)
    print('KÊN')
    sleep(1)
    print('PO!!!')
    print('~='*14)
    print('Você jogou {}!'.format(jokenpo[vc]))
    print('O computador jogou {}!'.format(jokenpo[cpu]))
    print('~='*14)
    if cpu == 1 and vc == 3 or cpu == 2 and vc == 1 or cpu == 3 and vc == 2:
        print('PARABÉNS! Vocẽ ganhou!')
    elif cpu == vc:
        print('EMPATE! Sem ganhadores!')
    else:
        print('VOCÊ PERDEU! ')
