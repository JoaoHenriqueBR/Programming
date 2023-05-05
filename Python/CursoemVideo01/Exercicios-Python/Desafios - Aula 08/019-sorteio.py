# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele. lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('Dentre esses alunos, o aluno escolhido foi {}!'.format(escolhido))
