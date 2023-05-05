nome = str(input('Qual é o seu nome? '))

if nome == 'João':
    print('Que nome Bonito! ')
elif nome == 'Gustavo':                                 #elif = Pode ser usada quantas vezes quiser!
    print('Obrigado pelo curso! ')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}!'.format(nome))
