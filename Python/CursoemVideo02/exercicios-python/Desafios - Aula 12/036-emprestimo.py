# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o:
# - Valor da Casa;
# - Salário do comprador;
# - Em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
 
print('=~'*20)
print('EMPRÉSTIMO BANCÁRIO - BANCO JH')
print('=~'*20)

valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Informe o seu salário: R$ '))
duracao = int(input('Em quantos anos irá pagar: '))

mensal = (valor / duracao) / 12

if mensal <= (salario / 10)*3:
    print('EMPRÉSTIMO pode ser CONCEDIDO!')
else:
    print('EMPRÈSTIMO NEGADO!')
    print('Prestação com o valor muito alto! NEGADO devido a risco de quebra de contrato!')

print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(valor, duracao), end='') 
print(' o valor da prestação será de R$ {:.2f}/Mês.'.format(mensal))
