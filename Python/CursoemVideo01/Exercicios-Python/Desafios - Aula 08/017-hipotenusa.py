# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostra o comprimento de sua hipotenusa.

from math import hypot

a = float(input('Digite o comprimento do cateto adjacente: '))
b = float(input('Digite o comprimento do cateto oposto: '))

h = hypot(b, a)

print('O comprimento da hipotenusa será de {:.2f}!'.format(h))
