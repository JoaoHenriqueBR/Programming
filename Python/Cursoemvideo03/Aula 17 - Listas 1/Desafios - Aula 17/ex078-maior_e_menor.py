
# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0

for cont in range(0, 5):
    valores.append(int(input(f"Digite um número para a posição {cont}: ")))
    if cont == 0:
        maior = menor = valores[cont]
        pos_maior = pos_menor = cont
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f"Maior valor: {maior} na(s) posição(ões) -> ", end='')
for cont, val in enumerate(valores):
    if val == maior:
        print(f"{cont}...", end='')
print()
print(f"Menor valor: {menor} na(s) posição(ôes) -> ", end='')
for cont, val in enumerate(valores):
    if val == menor:
        print(f"{cont}...", end='')
print()
