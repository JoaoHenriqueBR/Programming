# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor.

from math import inf

maior = 0
menor = inf
for p in range(5):
    peso = float(input('Digite o peso(KG) da {}° pessoa: '.format(p+1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso foi: {maior} KG')
print(f'O menor foi: {menor} KG')
