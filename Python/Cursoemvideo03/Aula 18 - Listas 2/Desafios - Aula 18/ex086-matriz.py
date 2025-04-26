'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]

for x in range(3):
  for y in range(3):
    matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

print('-'*30)
print(f" {'MATRIZ':^30}")
print('-'*30)

# No video do exercicio, o Guanabara usou 2 comandos for para mostrar a matriz.
# Nesse caso eu optei por usar apenas 1.

# Minha Versão
for x in matriz:
  print(f'[ {x[0]:^5} ]  [ {x[1]:^5} ]  [ {x[2]:^5} ]')

# Versão do Guanabara:
# for l in range(0,3):
#   for c in range(0,3):
#     print(f'[{matriz[l][c]:^5}}]', end='')

print()