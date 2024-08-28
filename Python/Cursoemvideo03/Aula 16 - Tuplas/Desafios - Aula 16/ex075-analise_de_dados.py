'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

tupla = (int(input("Digite um número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")), int(input("Digite o ṹltimo: ")))

print("")
print(f"Você digitou: {tupla}")
print(f"O 9 apareceu {tupla.count(9)} vezes.")

if 3 in tupla:
    print(f"O 3 apareceu na {tupla.index(3)+1}º posição.")
else:
    print("O valor 3 não foi digitado.")

print("São valores pares: ", end="")
for n in tupla:
    if n % 2 == 0:
       print(n, end=' ')

print("")
