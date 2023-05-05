# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27

r = float(input('Quantos reais deseja converter? R$'))
d = r / 3.27
h1 = str(' COTAÇÃO DO DÓLAR (EX.)')
h2 = str('US$1,00 = R$3,27')

print('='*40)
print('{} \n {}'.format(h1, h2))
print('='*40)
print('\n R$ {:.2f} valem US$ {:.2f}!'.format(r, d))
