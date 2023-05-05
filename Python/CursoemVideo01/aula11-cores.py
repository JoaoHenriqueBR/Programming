# print('\033[7;37mOlá, Mundo!\033[m ')

nome = str(input('Qual é o seu nome? '))

cores = {'limpa':'\033[m',
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;37m'}

print('Prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
