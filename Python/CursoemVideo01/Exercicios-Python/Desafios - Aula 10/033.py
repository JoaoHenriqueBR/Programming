# Faça um programa que leia 3 números e mostre qual o maior e qual o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o ultimo número: '))

maior = n2
menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
    menor = n2 if n3 > n2 else n3
if n3 > n2 and n3 > n1:
    maior = n3
    menor = n1 if n2 > n1 else n2

print('Dentre {}, {} e {}, o maior número é {}! '.format(n1, n2, n3, maior))
print('Já o menor número é {}! '.format(menor))
