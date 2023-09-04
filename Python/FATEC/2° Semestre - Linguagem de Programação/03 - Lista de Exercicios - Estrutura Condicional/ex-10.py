'''
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: 
R para residencial, 
I para industrial e 
C para comércios. 

Calcule o preço a pagar de acordo com a tabela a seguir: 
•Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.  
•Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.  
•Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.  
'''

print('='*39)
print('CÁLCULO DE VALOR POR CONSUMO DE ENERGIA')
print('='*39)

print('''
========= TIPO DE INSTALAÇÃO =========

R para residencial, 
I para industrial e 
C para comércios.
''')

tipo = ''

while tipo == '':
    tipo = input('Seu tipo de instalação: ').strip().upper()
    if tipo in 'RIC':
        break
    else:
        print('Tipo inválido! Tente Novamente.')
        tipo = ''

print('')
print('============ CONSUMO =============')
print('')

cons = int(input('Quantidade de kWh consumida: '))

match tipo:
    case 'R':
        if cons <= 500:
            preco = 0.4
        else:
            preco = 0.65
    case 'C':
        if cons <= 1000:
            preco = 0.55
        else:
            preco = 0.6
    case 'I':
        if cons <= 5000:
            preco = 0.55
        else:
            preco = 0.6

print(f'Preço por KWh: R$ {preco:.2f}')
print(f'Total a pagar: R$ {cons*preco:.2f}')
