# Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. 
# Pergunte também o valor mensal que será pago. Imprima o úmero de meses para que a divida seja paga, o total pago e o total de juros pago. 

from time import sleep

print('='*17)
print('CALCULO DE DIVIDA')
print('='*17)

ini = float(input('Valor inicial: R$ '))
tax = float(input('Juros mensal: R$ '))

pag = float(input('Valor mensal a ser pago: R$ '))

m = tot_pag = 0
tot = ini

while m >= 0:
    tot_pag += pag
    m += 1
    tot -= pag
    if tot < pag:
        print(f'Após {m} meses ', end='')
        print(f'Serão pagos R$ {tot_pag:.2f}.')
        print(f'Valor dos juros: R$ {(tot_pag + tot)-ini:.2f}')
        if tot != 0:
            print(f'Para quitar, restará uma {m+1}ª parcela de R$ {tot:.2f}')
        break
    tot += (tot * (tax / 100))
