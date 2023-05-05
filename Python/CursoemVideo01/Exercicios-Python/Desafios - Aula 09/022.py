# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# - O nome com todas as letras maiúsculas;
# - O nome com todas as letras minúsculas;
# - Quantas letras ao todo (Sem considerar espaços);
# - Quantas letras tem o primeiro nome.
#

nome = str(input('Digite um nome completo: ')).strip()
dividido = nome.split()
count = len(nome) - nome.count(' ')

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Ao todo ele tem {} letras! \n'.format(count))
print('Seu primeiro nome é {} e tem {} letras!'.format(dividido[0], len(dividido[0])))
