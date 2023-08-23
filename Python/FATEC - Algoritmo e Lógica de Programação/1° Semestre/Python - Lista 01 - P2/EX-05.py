# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro

lista = []

for c in range(20):
    print(c+1)
    lista.append(c+1)

print(lista)
