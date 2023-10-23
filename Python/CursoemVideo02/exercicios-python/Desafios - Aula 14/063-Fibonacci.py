# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Digite um número: '))
lista = [0, 1] 
cont = x = 0
y = 1
while cont != n - 2:
    f = x+y
    x = y
    y = f
    lista.append(f)
    cont +=1
print(lista)  
