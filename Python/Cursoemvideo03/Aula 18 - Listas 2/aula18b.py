# Cria uma lista com várias listas dentro
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)

# Mostra cada dado de cada lista através de um laço for.
for p in galera:
  print(f'{p[0]} tem {p[1]} anos de idade.')
  # A variável p mostra as listas, no [] especifica o dado que precisa de cada lista.