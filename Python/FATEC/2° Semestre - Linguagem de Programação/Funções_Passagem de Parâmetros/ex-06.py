# Crie uma função chamada somaMatriz que recebe uma matriz de inteiros e suas dimensões como parâmetros e retorna a soma de todos os elementos da matriz.

import numpy as np

tamanho = int(input('Qual a dimensão (tamanho) da matriz: '))

matriz = np.zeros((tamanho, tamanho), dtype=np.int64)

def somaMatriz(matriz, tamanho):
    soma = 0
    for x in range(0, tamanho):
        for y in range(0,tamanho):
            matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))
    print('--------- MATRIZ ---------')
    for x in range(0, tamanho):
        for y in range(0, tamanho):
            print(f'[{matriz[x][y]}]', end='')
            soma += matriz[x][y]
        print()
    print('-'*26)
    print(f'Soma: {soma}')

somaMatriz(matriz, tamanho)
