# Faça um programa que leia 5 números e informe o maior número.

from os import system # usado system('clear') para limpar a tela

print('{} Maior número entre 5 {}'.format('='*10, '='*10)) # titulo
c = 0
while c == 0:
    c = 1
    try: # tenta ler um valor
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        c = float(input('Digite o terceiro número: '))
        d = float(input('Digite o quarto número: '))
        e = float(input('Digite o último número: '))
    except: # se erro:
        c = 0
        system('clear')
        print('Valor inválido! Tente novamente.\n')

lista = [a, b, c, d, e]

print('')
print(f'O Maior número entre esses valores é {max(lista)}.')

