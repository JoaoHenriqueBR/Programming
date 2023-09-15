# Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período. 

print('='*10)
print('POUPANÇA')
print('='*10)

ini = float(input('\nDepósito inicial: R$ '))
tax = float(input('Taxa de Juros: '))

ganho = 0
total = ini

for c in range(24):
    ganho +=  (total * (tax/100))
    total = ini + ganho
    print(f'Total: R$ {total:.2f} -> Ganho: R$ {ganho:.2f}')


