# Crie uma função chamada calculaMediaMatriz que recebe uma matriz de inteiros e suas dimensões como parâmetros e retorna a média de todos os elementos da matriz. 

import numpy as np

tamanho = int(input('Qual a dimensão (tamanho) da matriz: '))
matriz = np.zeros((tamanho, tamanho), dtype=np.int64)

def calculaMediaMatriz(matriz, tamanho):
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
    return soma / (tamanho**2)

print(f'Média: {calculaMediaMatriz(matriz, tamanho)}')
