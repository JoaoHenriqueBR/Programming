# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))

cores = {'limpa':'\033[m'}

print('O número antecessor de \033[34m{}{} é \033[31m{}{}, enquanto seu sucessor é \033[32m{}{}.'.format(n, cores['limpa'], (n-1), cores['limpa'], (n+1), cores['limpa']))

