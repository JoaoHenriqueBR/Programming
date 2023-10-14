# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*15)
print('10 TERMOS DA PA')
print('='*15)

a1 = int(input('O primeiro termo da PA: '))
r = int(input('A razão da PA: '))

f = a1 + (10-1)*r
c = a1

while c <= f:
    print('{} '.format(c), end='-> ')
    c += r
print('ACABOU! ')
