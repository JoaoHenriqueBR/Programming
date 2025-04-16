# Cria uma lista teste e adiciona seus dados
teste = list()
teste.append('Gustavo')
teste.append(40)

# Cria uma nova lista galera e adiciona uma cópia da outra lista
galera = list()
galera.append(teste[:])

# Altera os dados da lista e adiciona outra cópia a lista.
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
#Obs: Para que a lista seja uma cópia e não uma ligação, se usa o [:].


print(galera)
