# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
#
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ùltimo: Souza
#

nome = input('Digite o nome completo de alguém: ').strip()
dividido = nome.split()
ultimo = len(dividido) - 1

print('Seu primeiro nome é: {}'.format(dividido[0]))
print('Já o seu último é: {}'.format(dividido[ultimo]))
