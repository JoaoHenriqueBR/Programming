# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
# Maioridade = 21 anos

from datetime import date

maior = menor = 0


for p in range(10):
    n = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - n
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas atingiram a maioridade.')
print(f'{menor} pessoas não a atingiram.')
