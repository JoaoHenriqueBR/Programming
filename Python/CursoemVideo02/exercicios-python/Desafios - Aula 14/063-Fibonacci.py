# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

quant = int(input('Quantos termos quer mostrar?: ')) 
cont = t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
while cont != quant - 2:
    f = t1+t2
    t1 = t2
    t2 = f
    print(f'{f} -> ', end='')
    cont +=1
print('FIM!')  
