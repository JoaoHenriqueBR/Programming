'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

from math import inf

alto = 0
baixo = inf

for c in range(10):
    print('{} {}º ALUNO {}'.format('-'*5, c+1, '-'*5))
    try:
        n = int(input('Digite o número do aluno: '))
        alt = int(input('Digite sua altura (CM): '))
    except:
        print('Valor inválido! \n')
        continue
    if alt > alto:
        n_alto = n
        alto = alt
    if alt < baixo:
        n_baixo = n
        baixo = alt

print(f'Mais alto: (N.{n_alto}) - {alto}cm')
print(f'Mais baixo: (N.{n_baixo}) - {baixo}cm')
