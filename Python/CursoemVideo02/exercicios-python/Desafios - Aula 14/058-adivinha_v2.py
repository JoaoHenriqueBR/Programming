# Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar.
# Mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('='*25)
print('ADVINHE O NÚMERO (0 A 10!)')
print('='*25)

print('O computador pensou em um número...')

cpu = randint(0, 10)
acertou = False
palpites = 0


while not acertou:
    usuario = int(input('Adivinhe o número: '))
    palpites += 1
    if cpu == usuario:
        acertou = True
    else:
        print('\nPuts! Parece que errou, tente', end=' ')
        if usuario < cpu:
            print('um número maior!')
        else:
            print('um número menor!')

print('\033[32mVOCÊ VENCEU!\033[m')
print(f'Foram {palpites} tentativa(s), parabéns!')
