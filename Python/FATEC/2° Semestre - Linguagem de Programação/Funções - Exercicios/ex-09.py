# Crie uma função chamada soma_intervalo que aceite dois números como parâmetros e retorne a soma de todos os números inteiros no intervalo entre eles.

def soma_intervalo(a, b):
    soma = 0
    if a < b:
        for c in range(a+1, b):
            soma = soma + c
    else:
        for c in range(b+1, a):
            soma = soma + c
    return soma

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))

print(f'Soma do intervalo entre {a} e {b}: {soma_intervalo(a, b)}')
