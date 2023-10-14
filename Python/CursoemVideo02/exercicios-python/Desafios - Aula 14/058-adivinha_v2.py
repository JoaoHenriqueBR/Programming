# Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar.
# Mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('='*25)
print('ADVINHE O NÚMERO (0 A 10!)')
print('='*25)

cpu = randint(0, 10)
usuario = cpu + 1

while cpu != usuario:
    usuario = int(input('Adivinhe o número: '))
    if cpu == usuario:
        print('\033[32mVOCÊ VENCEU!\033[m')
        break
    else:
        print('\nPuts! Parece que errou, tente novamente!')
