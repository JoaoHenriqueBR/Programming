'''
Escreva um programa que leia um numero e verifique se é ou não um numero primo. Para fazer essa verificação,  calcule  o  resto  da  divisão  do  numero  por  2  e  depois  por  todos  os  números  impares até  o numero lido. Se o resto de uma dessas divisões for igual a zero, o numero não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
'''

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
