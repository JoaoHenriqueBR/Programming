# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem:
# - O primeiro valor é maior;
# - O segundo valor é maior;
# - Os dois são iguais.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro: '))

if n1 > n2:
    print('{} é maior que {}!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}!'.format(n2, n1))
else:
    print("Ambos são iguais!")
