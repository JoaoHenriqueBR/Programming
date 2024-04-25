'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

from time import sleep

c = preco = caros = soma = 0
r = 's'
while r == 's':
    c += 1
    print('-'*30)
    nome = f'Produto {c}'
    print(f' {nome:^30}')
    print('-'*30)
    nome = input('Nome do produto: ')
    preco = float(input('Preço de produto: R$ '))
    print('Produto registrado...')
    soma += preco
    if preco > 1000:
        caros += 1
    if c == 1:
        nome_barato = nome
        barato = preco
    elif preco < barato:
        nome_barato = nome
        barato = preco
    sleep(1)
    while r != 'n':
        r = input('Deseja registrar outro? (s/n): ').lower()
        if r == 's':
            break

print('')
print(f'TOTAL GASTO: R$ {soma:.2f}')
print(f'Produtos acima de R$ 1000: {caros}')
print(f'Produto mais barato: {nome_barato}, R$ {barato:.2f}')

