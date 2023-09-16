# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no inicio de cada mês, e você deve considera-lo para o calculo de juros do mês seguinte. 

print('='*10)
print('POUPANÇA')
print('='*10)

ini = float(input('\nDepósito inicial: R$ '))
tax = float(input('Taxa de Juros: '))
mes = float(input('Depósito mensal: R$ '))

ganho = 0
total = ini

for c in range(24):
    ganho +=  (total * (tax/100)) + mes
    total = ini + ganho
    print(f'Mês {c+1} -> Total: R$ {total:.2f} -> Ganho: R$ {ganho:.2f}')


