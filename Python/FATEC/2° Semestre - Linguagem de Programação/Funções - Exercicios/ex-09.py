# Crie uma função chamada soma_intervalo que aceite dois números como parâmetros e retorne a soma de todos os números inteiros no intervalo entre eles.

def soma_intervalo(a, b):
    soma = a - b
    for c in range((a-b)-1, 1, -1):
        soma = soma * c
    return soma

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))

print(f'Soma do intervalo entre {a} e {b}: {soma_intervalo(a, b)}')
