# Crie uma função chamada calculaDesvioPadrao que recebe uma lista  de números reais e seu tamanho como parâmetros e retorna o desvio padrão dos valores no lista. 

from math import sqrt


reais = [290.33, 12.2, 17.5, 99.9] 
tam = len(reais)


def calculaDesvioPadrao(reais, tam):
    soma = varian = 0
    for x in reais:
        soma += x
    media = soma / tam
    for x in reais:
        varian += (x - media)**2
    return sqrt(varian / tam)


print(calculaDesvioPadrao(reais, tam))
