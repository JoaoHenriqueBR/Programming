# Faça um programa que leia 5 números e informe a soma e a média dos números.

from os import system # usado system('clear') para limpar a tela

print('{} Soma e média entre 5 números! {}'.format('='*10, '='*10)) # titulo

c = 0
while c == 0:
    c = 1
    try: # tenta ler os valores
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        c = float(input('Digite o terceiro número: '))
        d = float(input('Digite o quarto número: '))
        e = float(input('Digite o último número: '))
    except: # se erro:
        c = 0
        system('clear')
        print('Valor inválido! Tente novamente.\n')

soma = a + b + c + d + e

print('')
print(f'SOMA: {soma}')
print(f'Média: {soma/5}')
