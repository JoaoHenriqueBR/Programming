# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

from os import system

print('{} Calculo de valor da coleção de CDs {}'.format('='*10, '='*10))

cd = 0
while cd < 1:
    try:
        cd = int(input('Digite a quantidade de CDs: '))
    except:
        pass
    if cd > 0:
        break
    print('Número inválido! Tente novamente.')

val = 0
for c in range(cd):
    print('{} CD {} {}'.format('-'*5, c+1, '-'*5))
    try:
        val += float(input('Valor do CD: R$ '))
    except:
        system('clear')
        print('Valor Inválido! Será desconsiderado.')
        cd -= 1
        continue
    system('clear')

print('Valor total da coleção: R$ {:.2f}'.format(val))
print('Valor médio por CD: R$ {:.2f}'.format(val/cd))
