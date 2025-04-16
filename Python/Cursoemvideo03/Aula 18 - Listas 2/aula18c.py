# Declarão de variáveis (2 listas, 2 int)

galera = list()
dado = list()
totmai = totmen = 0

# Os dados da pessoa são extraidos através de um loop, onde:
#   - São adicionados a uma lista dado.
#   - Uma cópia da lista dado é adicionada a lista galera.
#   - A lista dado é limpa para uma próxima consulta.
for c in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('idade: ')))
  galera.append(dado[:])
  dado.clear()

# Análise dos dados (Verificação de Maioridade)
for p in galera:
  if p[1] >= 18:
    print(f'{p[0]} é maior de idade.')
    totmai += 1
  else:
    print(f'{p[0]} é menor de idade.')
    totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
  