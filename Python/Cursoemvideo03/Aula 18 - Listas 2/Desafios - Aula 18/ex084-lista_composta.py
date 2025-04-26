'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
dados = list()
pessoas = list() # Lista de pessoas para agilizar: [['João', 90.0], ['Jorge', 85.0], ['Cléber', 95.0], ['Mateus', 70.0], ['Pedro', 65.0], ['Ronaldo', 120.0], ['Rodrigo', 135.0]]

mai = men = 0

while True:
  dados.append(str(input('Nome: ')))
  dados.append(float(input('Peso (KG): ')))
  
  if len(pessoas) == 0:
    mai = men = dados[1]
  else:
    if dados[1] > mai:
      mai = dados[1]
    if dados[1] < men:
      men = dados[1]
  
  pessoas.append(dados[:])
  dados.clear()
  
  r = input('Deseja continuar? (s/n): ').lower().strip()
  if r == 'n':
    break


print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai} KG. Peso de ', end='')
for p in pessoas:
  if p[1] == mai:
    print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi de {men} KG. Peso de ', end='')
for p in pessoas:
  if p[1] == men:
    print(f'[{p[0]}] ', end='')

print()