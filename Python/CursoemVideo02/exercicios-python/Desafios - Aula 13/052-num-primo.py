# Faça um programa que leia um núemro inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))

tot = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')

print('\033[m')
print('O número {} foi divisivel {} vezes.'.format(n,tot))

if tot == 2:
    print('Portanto, ele é primo!')
else:
    print('Portanto, não é primo!')
