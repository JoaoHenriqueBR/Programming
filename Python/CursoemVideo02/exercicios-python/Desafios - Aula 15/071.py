'''
Crie um programa que simule o funcionamento de um caixa eletrônico.

No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('-'*30)
print(f' {'CAIXA ELETRÕNICO':^30}')
print('-'*30)


print('Notas disponíveis: R$ 50, R$ 20, R$ 10 e R$ 1.')
saque = int(input('Valor do saque: R$ '))

while saque > 0:
    if saque >= 50:
        cinquenta = saque // 50
        saque -= 50*cinquenta
    if saque >= 20:
        vinte = saque // 20
        saque -= 20*vinte
    if saque >= 10:
        dez = saque // 10
        saque -= 10*dez
    if saque >= 1:
        um = saque
        saque = 0

print('')
print('Serão sacados: ')
print(f'{cinquenta} notas de R$ 50.')
print(f'{vinte} notas de R$ 20.')
print(f'{dez} notas de R$ 10.')
print(f'{um} moedas de R$ 1.')
