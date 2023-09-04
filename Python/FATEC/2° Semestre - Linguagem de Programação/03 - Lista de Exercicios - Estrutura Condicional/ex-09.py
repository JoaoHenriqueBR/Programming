'''
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos apagar. 
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar. 
'''

print('='*32)
print('SIMULADOR DE EMPRÉSTIMO BANCÁRIO')
print('='*32)

valor = float(input('Valor da casa a comprar: '))
salario = float(input('Salário: '))
anos = int(input('Quantidade de anos para pagar: '))

mensal = (valor / anos) / 12

if mensal <= (salario / 10)*3:
    print('EMPRÉSTIMO pode ser CONCEDIDO!')
else:
    print('EMPRÈSTIMO NEGADO!')
    print('Prestação com o valor muito alto! NEGADO devido a risco de quebra de contrato!')

print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(valor, anos), end='') 
print(' o valor da prestação será de R$ {:.2f}/Mês.'.format(mensal))
