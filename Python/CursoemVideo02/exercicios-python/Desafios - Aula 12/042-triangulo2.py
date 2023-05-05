# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado:
# - Equilátero: Todos os lados são iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados são diferentes

print('~≃~' * 10)
print('ANALISADOR DE TRIÂNGULOS 2.0! ')
print('~≃~' * 10)

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Por causa do comprimento de uma das retas, não é possivel fazer um triângulo!')
else:
    if a == b == c:
        print('Triângulo Equilátero, todos os lados são iguais!')
    elif a != b != c != a:
        print('Triângulo Escaleno, todos os lados são diferentes!')
    else:
        print('Triângulo Isósceles, dois lados são iguais!')
