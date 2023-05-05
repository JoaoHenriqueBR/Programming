# Desenvolva um programa que leia o comprimento de três retas
# Diga ao usuário se elas podem ou não formar um triângulo.

print('~≃~' * 10)
print('ANALISADOR DE TRIÂNGULOS! ')
print('~≃~' * 10)

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a >= b + c or b >= a + c or c >= a + b:
    print('Por causa do comprimento de uma das retas, não é possivel fazer um triângulo!')
else:
    print('É possivel fazer um triângulo! ')
