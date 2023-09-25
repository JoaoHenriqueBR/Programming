# Crie uma função chamada maior_valor que aceite uma lista de números como parâmetro e retorne o maior valor da lista. 

numeros = []

def maior_valor(numeros):
    maior = 0
    for n in numeros:
        if n > maior:
            maior = n
    return maior

while (1):
    x = int(input('Acrescente um número (0 para parar): '))
    if x == 0:
        break
    numeros.append(x)

print(f'Números: {numeros}')
print(f'Maior: {maior_valor(numeros)}')
