# Crie uma função chamada maiorMenor que recebe uma lista  de inteiros e seu tamanho como parâmetros e retorna o maior e o menor valor no lista.

from random import randint

def maiorMenor(inteiros, tamanho):
    for i in range(tamanho):
        inteiros.append(randint(1, 100000))
    return (f'{inteiros},\nMaior: {max(inteiros)}\nMenor: {min(inteiros)}')

print(maiorMenor(inteiros=[], tamanho=5))
