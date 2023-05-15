# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

from getpass import getpass

print('{:=^40}'.format(' LOGIN '))
user = input('Nome do usuário: ')
senha = getpass('SENHA: ')

while senha == user:
    print('Senha deve ser diferente do Nome do usuário! Tente novamente! ')
    senha = getpass('Digite novamente a senha: ')
else:
    print('\nLogado com Sucesso! Bem vindo de volta {}!'.format(user))
