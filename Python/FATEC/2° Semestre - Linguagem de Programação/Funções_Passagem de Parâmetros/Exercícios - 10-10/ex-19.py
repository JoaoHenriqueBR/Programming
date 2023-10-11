#  Crie uma função chamada calculaMediaPonderada que recebe dois listas (um de notas e outro de pesos)
#  e o número de elementos como parâmetros e retorna a média ponderada das notas. 


def calculaMediaPonderada(notas, pesos, n):
    if len(notas) != n or len(pesos) != n:
        return "As listas de notas e pesos devem ter o mesmo tamanho."
    else:
        soma = 0
        soma_pesos = 0
        for i in range(n):
            soma += notas[i] * pesos[i]
            soma_pesos += pesos[i]
        return soma / soma_pesos

print(calculaMediaPonderada(notas=[5, 10], pesos=[20, 30], n=2))
