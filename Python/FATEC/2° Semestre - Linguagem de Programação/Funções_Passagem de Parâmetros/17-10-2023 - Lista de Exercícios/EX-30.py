# Elabore um programa que simule um jogo de adivinhação, onde o computador escolhe um número aleatório entre 1 e 100 e o jogador tenta adivinhar o número.

from random import randint

print('='*25)
print('ADVINHE O NÚMERO (1 A 100!)')
print('='*25)

cpu = randint(1, 100)
usuario = cpu + 1

while cpu != usuario:
    usuario = int(input('Adivinhe o número: '))
    if cpu == usuario:
        print('\033[32mVOCÊ VENCEU!\033[m')
        break
    else:
        print('\nPuts! Parece que errou, tente novamente!')
        if cpu > usuario:
            print('Tente um número maior!')
        else:
            print('Tente um número menor!')

