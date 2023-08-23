# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

from getpass import getpass

print('{:=^40}'.format(' LOGIN '))

user = input('Nome do usuário: ')
senha = getpass('SENHA: ') # Aprendi sobre o uso do Getpass como forma de perguntar ao usuário alguma informação sem a revelar

while user == senha:
    print('SENHA INVÁLIDA! A senha deve ser diferente do nome do usuário! ')
    senha = getpass('Digite a senha novamente: ')

print('Bem vindo de volta {}!'.format(user))
