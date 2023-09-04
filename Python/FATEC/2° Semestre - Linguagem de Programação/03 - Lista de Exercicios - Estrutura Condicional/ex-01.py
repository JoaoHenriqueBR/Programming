# –Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. Caso ambos os números forem iguais, imprima na tela “números iguais”. 

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print(f'O número {a} é o maior!')
elif b > a:
    print(f'O número {b} é o maior!')
else:
    print('Números iguais.')

