'''
Faça um programa que tenha uma função chamada maior(),
    que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e definir qual deles é o maior.
'''

from time import sleep

def maior(*num):
    maior = 0

    print('Analisando...')
    sleep(1)

    print('Valores: ', end='')
    for c, n in enumerate(num):
        print(n, end=' ', flush=True)
        sleep(0.5)
        if c == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print()
    print(f'Quantidade: {len(num)}')
    print(f'Maior valor: {maior}')

def lin():
    print('-='*20)


# Programa Principal
lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()
lin()
maior(-2, -5, -1, -7) # Teste pessoal

