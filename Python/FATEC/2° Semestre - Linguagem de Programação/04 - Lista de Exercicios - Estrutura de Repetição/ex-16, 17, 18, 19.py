#  EX 16
#
#  Escreva um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. 
# Para simplificar utilize números inteiros e com cédulas de R$50, R$20, R$10, R$4 e R$1. 
# Após concluído, testes com os seguintes valores: 50, 745, 384, 2, 7 e 1. 

from decimal import Decimal

cinquenta = vinte = dez = qua = cem = um = moeda_cinquenta = moeda_dez = moeda_cinco = moeda_dois = moeda_um = 0

val = float(input('Informe o valor: R$ ')) 

if val >= 100: # EX 18 - Modifique o programa da questão 16 para trabalhar com nota de R$ 100,00 
    cem = val // 100
    val = Decimal(f'{val}') % 100
if val >= 50 and val < 100:
    cinquenta = val // 50
    val = Decimal(f'{val}') % 50
if val >= 20 and val < 50:
    vinte = val // 20
    val = Decimal(f'{val}') % 20
if val >= 10 and val < 20:
    dez = val // 10
    val = Decimal(f'{val}') % 10
if val >= 4 and val < 10:
    qua = val // 4
    val = Decimal(f'{val}') % 4
if val >= 1 and val < 4:
    um = val // 1
    val = Decimal(f'{val}') % 1

# EX 19 - Modifique o programa da questão 16 para aceitar valores decimais, ou seja, também contar moedas de R$0.01, R$0.02, R$0.05, R$0.10, e R$0.50.

if val >= 0.50:
    moeda_cinquenta = Decimal(f'{val}') // Decimal('0.5')
    val = Decimal(f'{val}') % Decimal('0.5')
if val >= 0.1:
    moeda_dez = Decimal(f'{val}') // Decimal('0.1')
    val = Decimal(f'{val}') % Decimal('0.1')
if val >= 0.05:
    moeda_cinco = Decimal(f'{val}') // Decimal('0.05')
    val = Decimal(f'{val}') % Decimal('0.05')
if val >= 0.02:
    moeda_dois = Decimal(f'{val}') // Decimal('0.02')
    val = Decimal(f'{val}') % Decimal('0.02')


if val < 0.02:
    moeda_um = Decimal(f'{val}') // Decimal('0.01')


print('Para pagar esse valor, será necessário: ')
print(f'{cem} nota(s) de R$ 100.\n')
print(f'{cinquenta} nota(s) de R$ 50.')
print(f'{vinte} nota(s) de R$ 20.')
print(f'{dez} nota(s) de R$ 10.')
print(f'{qua} nota(s) (2 de 2) de R$ 4.')
print(f'{um} moeda(s) de R$ 1.')
print('')
print(f'{moeda_cinquenta} moeda(s)de R$ 0.50.')
print(f'{moeda_dez} moeda(s) de R$ 0.10.')
print(f'{moeda_cinco} moeda(s) de R$ 0.05.')
print(f'{moeda_dois} moeda(s) de R$ 0.02.')
print(f'{moeda_um} moeda(s) de R$ 0.01.')

# EX 17
'''
- No programa anterior, o que acontece se for digitado 0 (zero) no valor a pagar? 

>
Informe o valor: R$ 0
Para pagar esse valor, será necessário: 
0 nota(s) de R$ 50.
0 nota(s) de R$ 20.
0 nota(s) de R$ 10.
0 nota(s) (2 de 2) de R$ 4.
0 moeda(s) de R$ 1.

'''