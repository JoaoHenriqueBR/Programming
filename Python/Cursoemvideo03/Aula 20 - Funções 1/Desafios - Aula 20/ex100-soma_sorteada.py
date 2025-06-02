'''
Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar().
    - A primeira função vai sortear 5 números e vai colocá-los dentro da lista;
    - A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint
from time import sleep

números = list()

def sorteia(num):
    
    print('Sorteando números: ', end='')

    for c in range(0,5):
        n = randint(0,10)
        num.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print()


def somaPar(num):
    soma = 0
    
    for n in num:
        if n % 2 == 0:
           soma += n

    print(f'Soma dos pares de {num}: {soma}')

sorteia(números)
somaPar(números)
