# Faça um programa que leia um ângulo qualquer e mostre na sua tela o valor do seno, cosseno e tangente.

import math

a = int(input('Digite o valor de um ângulo: '))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

if t > 1:
    print('O angulo de {}º tem como: \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: Indefinido.'. format(a, s, c))
else:
    print('O ângulo de {}º tem como: \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(a, s, c, t))
