'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas
    os valores pares
    os valores impares
digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

num = []
pares = num[:]
impares = num[:]

while True:
    n = int(input("Digite um número: "))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
    r = input("Deseja continuar (s/n): ").strip().lower()
    if r != "s":
        break

print(f"\nDigitado: {num}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
