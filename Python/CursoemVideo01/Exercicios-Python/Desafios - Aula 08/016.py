# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#
# Ex: Digite 6.127 (O Número 6.127 tem a parte inteira 6).

'''from math import trunc

nr = float(input('Digite um número real: '))                                  # Importado do 'Math'

print('O número {} tem {} como sua parte inteira! '.format(nr, trunc(nr)))'''

# Nativo do Python (Sem importar nada)

num = float(input('Digite um valor real: '))

print('O número {} tem {} como sua parte inteira! '.format(num, int(num)))
