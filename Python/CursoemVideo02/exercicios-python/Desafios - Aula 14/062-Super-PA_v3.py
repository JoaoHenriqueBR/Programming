# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar alguns termos.
# O programa encerra quando ele dizer que quer mostrar 0 termos.

print('='*15)
print('10 TERMOS DA PA')
print('='*15)

a1 = int(input('O primeiro termo da PA: '))
r = int(input('A razão da PA: '))
quant = int(input('Quantidade de termos: '))

f = a1 + (quant-1)*r
c = a1

while c <= f:
    print('{} '.format(c), end='-> ')
    c += r
print('ACABOU! ')
