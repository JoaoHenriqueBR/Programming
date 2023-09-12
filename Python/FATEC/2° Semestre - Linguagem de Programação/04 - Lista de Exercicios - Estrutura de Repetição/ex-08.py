'''
Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como a soma sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. 
'''

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))

total = 0
soma = []

print(f'{a} x {b} = ', end='')
for n in range(b+1):
  soma.append(a)
  total += a

print(f'{soma} = {total}'.replace(',', ' +').replace('[', '').replace(']', ''))
