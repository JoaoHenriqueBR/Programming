'''
Crie um programa que simule o funcionamento de um caixa eletrônico.

No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('-'*30)
print(f' {"CAIXA ELETRÕNICO":^30}')
print('-'*30)


print('Notas disponíveis: R$ 50, R$ 20, R$ 10 e R$ 1.')
saque = int(input('Valor do saque: R$ '))
print('')

total = saque

ced = 50 # Variável ced, contendo o valor da cédula de maior valor
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('')
print('-'*35)
print('Obrigado por usar nossos serviços, \nVolte sempre!')
