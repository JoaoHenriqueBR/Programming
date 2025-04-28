'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

alunos = list()

while True:
  nome = str(input('Nome: '))
  n1 = float(input('Nota 1: '))
  n2 = float(input('Nota 2: '))
  media = (n1+n2)/2
  alunos.append([nome, [n1, n2], media])
  r = str(input('Deseja continuar? (s/n): ')).strip().lower()
  if r == 'n':
    break

print('-='*15)

print(f'{"Nº":<4} | {"Nome":<10} | {"Média":>8}')
print('-'*30)
for c, a in enumerate(alunos):
  print(f'{c:<4} | {a[0]:<10} | {a[2]:>8.1f}')

while True:
  r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if r == 999:
    print('FINALIZANDO...')
    break
  if r <= len(alunos) - 1:
    print(f'As notas de {alunos[r][0]} são: {alunos[r][1]}')
print('<<< VOLTE SEMPRE! >>>')
