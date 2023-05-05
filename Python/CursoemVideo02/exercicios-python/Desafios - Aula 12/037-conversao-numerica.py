# Escreva um programa que leia um número inteiro e peça para o usuário escolher a base de conversão:
# - 1 para binário;
# - 2 para octal;
# - 3 para hexadecimal.

# CORES
cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'verde':'\033[32m',
       'vermelho':'\033[31m'}

numero = int(input('Informe um número: '))
print('=~'*20)
print('CONVERSÂO DE NÙMEROS')
print('=~'*20)
print('{}1{} para {}binário{};'.format(cor['verde'], cor['limpa'], cor['verde'], cor['limpa']))
print('{}2{} para {}octal{};'.format(cor['azul'], cor['limpa'], cor['azul'], cor['limpa']))
print('{}3{} para {}hexadecimal{}.'.format(cor['amarelo'], cor['limpa'], cor['amarelo'], cor['limpa']))
base = int(input('Qual base deseja converter: '))

if base == 1:
       print('{} convertido para binário é igual a {}!'.format(numero, bin(numero)[2:]))
elif base == 2:
       print('{} convertido para octal é igual a {}!'.format(numero, oct(numero)[2:]))
elif base == 3:
       print('{} convertido para hexadecimal é igual a {}!'.format(numero, hex(numero)[2:]))
else:
       print('{}OPÇÃO INVALIDA!{} Tente Novamente.'.format(cor['vermelho'], cor['limpa']))
