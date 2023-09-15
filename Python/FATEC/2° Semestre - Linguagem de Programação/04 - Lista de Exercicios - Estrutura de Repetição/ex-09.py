'''
Escreva um programa que leia dois números. 
Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. 
Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
'''

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))

x = quo = 0

while x <= a - b:
    x += b
    quo += 1

resto = a - x

print(f'O quociente da divisão é {quo}.')
print(f'O resto da divisão é {resto}.')
