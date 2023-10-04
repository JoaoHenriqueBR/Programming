# Crie uma função chamada maximo que recebe uma lista de números inteiros e seu tamanho como parâmetros e retorna o valor máximo na lista.

numeros = []

def maximo(numeros):
    maior = max(numeros)
    return maior

while True:
    x = int(input('Acrescente um número (0 para parar): '))
    if x == 0:
        break
    numeros.append(x)

print(maximo(numeros))
