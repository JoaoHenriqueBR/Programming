# Elabore um programa que calcule o valor a ser pago por um produto;
# Considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais: 20% de juros

print('{:=^40}'.format(' LOJAS JH '))

valor = float(input('Qual o valor do produto? R$ '))
condicao = float(input('''Qual será a forma de pagamento?
[ 1 ] para à vista (dinheiro/cheque) - 10% de desconto
[ 2 ] para à vista no cartão - 5% de desconto
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais - 20% de juros
Digite sua escolha: '''))

if condicao == 1:
    desc = valor / 10
    preco = valor - desc
    print('Pagando à vista no dinheiro/cheque, o produto ficará por R$ {:.2f}!'.format(preco))
    print('O Desconto será de R$ {:.2f}!'.format(desc))
elif condicao == 2:
    desc = (valor * 5)/100
    preco = valor - desc
    print('Pagando à vista no cartão, o produto ficará por R$ {:.2f}!'.format(preco))
    print('O Desconto será de R$ {:.2f}!'.format(desc))
elif condicao == 3:
    print('Em 2x, serão duas parcelas de R$ {:.2f}.'.format(valor / 2))
    print('Totalizando R$ {:.2f}!'.format(valor))
elif condicao == 4:
    parcelas = int(input('Em quantas vezes deseja parcelar: '))
    if parcelas >= 3:
        juros = (valor * 20)/100
    else:
        juros = 0
    preco = valor + juros
    print('Em {}x, serão {} parcelas de R$ {:.2f}.'.format(parcelas, parcelas, preco / parcelas))
    print('Totalizando R$ {:.2f}!'.format(preco))
else:
    print('OPÇÃO INVALIDA! Tente novamente!')

