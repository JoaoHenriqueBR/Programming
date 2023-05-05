# Escreva um programa que pergunte:
#
# - Quantidade de Km percorridos por um carro alugado;
# - Quantidade de dias pelos quais ele foi alugado.
# 
# E calcule o preço a pagar, sabendo que o carro:
#
# - Custa R$60/Dia;
# - R$ 0,15 por Km rodado.

km = float(input('Distância percorrida pelo carro (Em Km): '))
d = int(input('Tempo de uso do carro (Em dias): '))

p = (d * 60) + (km * 0.15)

print('O preço pelo aluguel do carro será de R${:.2f}!'.format(p))
