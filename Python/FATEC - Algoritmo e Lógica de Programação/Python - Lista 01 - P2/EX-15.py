# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.

from os import system

print('{} ALUNOS POR TURMA {}'.format('='*10, '='*10)) # titulo

turmas = 0
while turmas < 1:
    try:
        turmas = int(input('Digite o número de turmas: '))
    except:
        pass
    if turmas > 0:
        break
    print('Número inválido! Tente novamente.')

n = 0
for c in range(turmas):
    print('{} Turma {} {}'.format('-'*5, c+1, '-'*5))
    try:
        n += int(input('Número de alunos: '))
    except:
        system('clear')
        print('Valor Inválido! Será desconsiderado.')
        turmas -= 1
        continue
    system('clear')

print(f'Média por turma: {n/turmas} alunos.')
