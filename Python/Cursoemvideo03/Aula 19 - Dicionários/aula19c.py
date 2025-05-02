estado = dict()
brasil = list()
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  
  # Diferente de lista, os dicionários não aceitam o fatiamento [:]
  # No lugar, se usa o método .copy()
  brasil.append(estado.copy())

# Para os itens na lista brasil
for e in brasil:
  # Para os itens no dicionário estado
  for k, v in e.items():
    print(f'{k}: {v}.')
  print()

for e in brasil:
  # Apenas os valores no dicionário
  for v in e.values():
    print(v, end=' ')
  print()
