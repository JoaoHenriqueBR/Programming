'''
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]

soma_par = soma_ter_col = maior = 0

for x in range(3):
  for y in range(3):
    matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

print('-'*30)
print(f" {'MATRIZ':^30}")
print('-'*30)

# Minha Versão
for l, x in enumerate(matriz):
  print(f'[ {x[0]:^5} ]  [ {x[1]:^5} ]  [ {x[2]:^5} ]') 
  soma_ter_col += matriz[l][2]
  for c, y in enumerate(x):
    if y % 2 == 0:
      soma_par += y
    if l == 1 and y > maior:
      maior = y
      
# Versão do Guanabara
# for l in range(0,3):
#   soma_ter_col += matriz[l][2]
#   for c in range(0,3):
#     print(f'[{matriz[l][c]:^5}}]', end='')
#     if matriz[l][c] % 2  == 0:
#       soma_par += matriz[l][c]
#
# for c in range(0,3):
#   if c == 0:
#     maior = matriz[1][c]
#   elif matriz[1][c] > maior:
#     maior = matriz[1][c]

print(f'Soma dos pares: {soma_par}.')
print(f'Soma da 3ª Coluna: {soma_ter_col}.')
print(f'Maior valor da 2ª Linha: {maior}.')