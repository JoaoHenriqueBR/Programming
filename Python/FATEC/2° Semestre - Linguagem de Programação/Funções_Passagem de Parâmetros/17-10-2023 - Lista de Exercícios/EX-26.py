# Crie uma função chamada copiaMatriz que recebe uma matriz de inteiros e suas dimensões como parâmetros e retorna uma cópia da matriz. 


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dim = 3

def copiaMatriz(matriz, dim):
    copia = []
    for x in range(dim):
        linha = []
        for y in range(dim):
            linha.append(matriz[x][y])
        copia.append(linha)
    return copia

print(copiaMatriz(matriz, dim))
