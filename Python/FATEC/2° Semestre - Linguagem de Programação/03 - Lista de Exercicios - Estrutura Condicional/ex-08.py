# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você  deve  poder  calcular  soma  (+),  subtração  (-),  multiplicação  (*)  e  divisão  (/).  
# Exiba  o  resultado  da operação solicitada. 

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))

print('''
+ -> Soma
- -> Subtração
* -> Multiplicação
/ -> Divisão
''')

res = 0

while res == 0:
    op = input('Qual operação deseja realizar: ').strip()
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a / b
    else:
        print('Valor inválido! Tente novamente.')

print(f'Resultado: {a} {op} {b} = {res}.')
