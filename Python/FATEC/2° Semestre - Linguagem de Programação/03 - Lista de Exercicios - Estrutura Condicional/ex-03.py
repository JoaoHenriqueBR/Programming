# Escreva um programa que leia três números e que imprima o maior e o menor. 

maior = menor = 0

for c in range(3):
    n = int(input(f'Digite o {c+1}º número: '))
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print(f'Maior: {maior}.')
print(f'Menor: {menor}.')
