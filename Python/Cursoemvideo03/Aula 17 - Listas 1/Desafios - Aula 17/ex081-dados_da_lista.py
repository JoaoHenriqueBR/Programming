'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    r = input("Deseja continuar? (s/n): ").lower().strip()
    if r in "n":
        break

print(f"Lista: {lista}\n")
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números.")
print(f"Ordem decrescente: {lista}\n")

if 5 in lista:
    print(f"O número 5 foi digitado {lista.count(5)} vez(es).")
else:
    print("O valor 5 não foi encontrado na lista.")
    