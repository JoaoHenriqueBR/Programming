# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('Para {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.3f}.'.format(n, (n*2), (n*3), (n**(1/2))))
