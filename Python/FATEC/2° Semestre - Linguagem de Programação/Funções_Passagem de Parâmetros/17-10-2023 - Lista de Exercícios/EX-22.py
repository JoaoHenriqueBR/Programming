# Crie uma função chamada inverteMatriz que recebe uma matriz de inteiros 
# e suas dimensões como parâmetros 
# e inverte a ordem das linhas da matriz.

dim = 2
matriz = []

def inverteMatriz(matriz, dim):
    for x in range(0, dim):
        linha = []
        for y in range(0, dim):
            linha.append(int(input(f'Digite um valor para [{x}, {y}]: ')))
        matriz.append(linha) 
    for i in range(0, dim):
        matriz[i].reverse()
    return matriz

print(inverteMatriz(matriz, dim))


