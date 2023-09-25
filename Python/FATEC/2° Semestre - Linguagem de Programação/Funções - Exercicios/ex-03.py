# Crie uma função chamada media que aceite uma lista de números como parâmetro e retorne a média deles.

numeros = []

def media(numeros):
    soma = sum(numeros)
    med = soma / len(numeros)
    return med


while (1):
    x = int(input('Acrescente um número (0 para parar): '))
    if x == 0:
        break
    numeros.append(x)

print(f'Números: {numeros}')
print(f'Média: {media(numeros)}')
