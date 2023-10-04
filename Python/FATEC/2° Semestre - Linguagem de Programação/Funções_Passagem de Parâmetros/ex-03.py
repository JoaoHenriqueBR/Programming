# Crie uma função chamada media que recebe uma lista de números inteiros e seu tamanho como parâmetros e retorna a média dos valores em uma lista.

numeros = []

def media(numeros, tamanho):
    soma = sum(numeros)
    med = soma / tamanho
    return med

while True:
    x = int(input('Acrescente um número (0 para parar): '))
    if x == 0:
        break
    numeros.append(x)

print(f'Números: {numeros}')
print(f'Média: {media(numeros, tamanho=len(numeros))}')
