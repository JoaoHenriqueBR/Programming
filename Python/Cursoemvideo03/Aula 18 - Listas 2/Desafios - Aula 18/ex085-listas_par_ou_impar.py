'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

num = [[], []]

for c in range(7):
  n = int(input(f'Digite o {c+1}º número: '))
  if n % 2 == 0:
    num[0].append(n)
  else:
    num[1].append(n)

print('-'*30)
num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'Impares: {num[1]}')
