# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um número: '))
c = 0
fat = n

while c < (n-1):
    c += 1
    fat = fat * (n-c)

print(f'Fatorial de {n}! = {fat}')
