'''

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

a. Os juros e a quantidade de parcelas seguem a tabela abaixo:

b. Quantidade de Parcelas % de Juros sobre o valor inicial da dívida

c. 1 0

d. 3 10

e. 6 15

f. 9 20

12 25
'''

from os import system
import math

status = 'erro'
while status == 'erro':
    try: 
        valor = float(input('Informe o valor da divida: R$ '))
    except:
        valor = -1
    system('clear')
    if valor >= 0:
        break
    print('Valor Inválido! Tente novamente.\n')

print('Valor da divida: R% {:.2f}\n'.format(valor))

n = 1
print('{} TABELA DE PARCELAS/JUROS {}'.format('='*10, '='*10))
print('1x - 0% - R$ {:.2f}'.format(valor))
for c in range(3, 13, 3):
    n += 1
    juros = 5 * n
    total = valor + ((valor / 100)*juros)
    print('{}x - {}% - R$ {:.2f} '.format(c, juros, total/c))
