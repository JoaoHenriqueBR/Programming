# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três
# e que se encontram no intervalo de 1 até 500.

i = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        i = i + c
        cont += 1
print('SOMA dos {} valores: {}'.format(cont, i))
