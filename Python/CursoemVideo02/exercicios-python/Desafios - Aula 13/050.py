# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem:
# Pares, se for impar, desconsidere-o.

s = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print('Soma dos números pares: {}'.format(s))
