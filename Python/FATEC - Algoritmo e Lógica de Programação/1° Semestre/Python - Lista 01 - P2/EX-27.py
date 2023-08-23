'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

a. 1 , 2, 3, 4 - Votos para os respectivos candidatos

b. (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)

c. 5 - Voto Nulo

d. 6 - Voto em Branco

Faça um programa que calcule e mostre:

e. O total de votos para cada candidato;

f. O total de votos nulos;

g. O total de votos em branco;

h. A percentagem de votos nulos sobre o total de votos;

i. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

from os import system
import math

candidatos = {1:'Jose',
              2:'João',
              3:'Jorge',
              4:'Jasmim',
              5:'Nulo',
              6:'Branco'}

print('{} CANDIDATOS {}'.format('='*30, '='*30))
print(candidatos)

v = -1
total = 0

jose = 0
joao = 0
jorge = 0
jasmim = 0
branco = 0
nulo = 0

while v != 0:
    try:
        v = int(input('Informe o seu voto (0 - Encerra a votação): '))
    except:
        v = -1
    if v == 0:
        break
    elif v < 0 or v > 6:
        system('clear')
        print('Voto inválido! Tente novamente.')
    else:
        print(f'Voto registrado! Você votou em {candidatos[v]}.')
        total += 1
        if v == 1:
            jose += 1
        elif v == 2:
            joao += 1
        elif v == 3:
            jorge += 1
        elif v == 4:
            jasmim += 1
        elif v == 6:
            branco += 1
        else:
            nulo += 1

print(f'Jose: {jose} votos.')
print(f'João: {joao} votos.')
print(f'Jorge: {jorge} votos.')
print(f'Jasmim: {jasmim} votos.')
print('')
print(f'{nulo} votos nulos. ({100*nulo/total}%)')
print(f'{branco} votos brancos. ({100*branco/total}%)')
