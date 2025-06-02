'''
Faça um programa que tenha uma função chamada contador(),
    que recebe três parâmetros: inicio, fim e passo e
    realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
    a) De 1 até 10, de 1 em 1
    b) De 10 até 0, de 2 em 2
    c) Uma contagem personaliza.
'''

from time import sleep

def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)

    if inicio > fim:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    

# Programa Principal
contagem(1, 10, 1)
contagem(10,0,2)
print('-='*20)
print('Crie sua contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
