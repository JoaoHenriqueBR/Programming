# Escreva  um  programa  que  calcule  o  resto  da  divisão  inteira  entre  dois  números.  
# Utilize  apenas  as operações de soma e subtração para calcular o resultado. 

a = int(input('Digite um número: '))
b = int(input('Digite o número divisor: '))

x = quo = 0

while x <= a - b:
    x += b
    quo += 1

resto = a - x

print(f'Resultado: {quo}')
print(f'Resto: {resto}')
