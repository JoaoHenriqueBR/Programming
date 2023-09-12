# Escreva um programa que exiba a tabuada do número digitado de 0 a 10.

n = int(input('Número que deseja saber a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
