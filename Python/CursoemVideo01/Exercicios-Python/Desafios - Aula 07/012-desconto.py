# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do seu produto? R$'))
d = (p / 100)*5

print('Com um desconto de 5%, você irá conseguir este produto por R$ {:.2f}!'.format(p-d))
