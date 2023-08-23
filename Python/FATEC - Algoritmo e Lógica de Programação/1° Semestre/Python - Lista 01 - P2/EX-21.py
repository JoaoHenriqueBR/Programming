'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

from datetime import date

salario = 0
while salario < 1:
    try:
        salario = float(input('Digite o salário inicial: '))
    except:
        pass
    if salario >= 1:
        break 
    print('Valor Inválido! Tente novamente.')

aumento = (salario * 1.5)/100
salario = salario + aumento
print('1996: R$ {:.2f}\n'.format(salario))

ano = 1997
while ano <= date.today().year:
    aumento *= 2 
    salario = salario + aumento
    print('{}: R$ {:.2f}'.format(ano, salario))
    ano += 1

