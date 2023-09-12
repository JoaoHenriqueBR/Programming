# Escreva um programa que exiba a tabuada do número digitado, onde o usuário possa escolher o inicio e o fim da tabuada.

n = int(input('Número que deseja saber a tabuada: '))

i = int(input('Inicio da tabuada: '))
f = int(input('Final da tabuada: '))

for c in range(i, f+1):
    print('{} x {} = {}'.format(n, c, n*c))
