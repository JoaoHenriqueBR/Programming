# Crie uma função chamada calculaMDC que recebe dois números inteiros como parâmetros e retorna o máximo divisor comum (MDC) entre eles. 

from math import gcd

def calculaMDC(a, b):
    return gcd(a, b)

print(calculaMDC(a=20, b=24))
