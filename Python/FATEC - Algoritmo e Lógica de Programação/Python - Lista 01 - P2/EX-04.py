# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

from time import sleep
from math import trunc
from os import system

print('{} PROGRAMA DE COMPARAÇÃO DE CRESCIMENTO DE CIDADES {}'.format('='*10, '='*10))
a = 0
b = 0
ta = 0
tb = 0

while a == 0:
    try:
        a = int(input('Número de habitantes da primeira cidade: '))
    except:
        system('clear')
        print('Valor inválido! Precisa ser um número inteiro.\n')
        a = 0

while ta == 0:
    print('\nAVISO! A taxa de crescimento será mantida em relação ao número de habitantes.')
    try:
        ta = float(input('Taxa de crescimento (%): '))
    except:
        system('clear')
        print('Valor Inválido! Tente novamente! (Lembre-se: Números decimais precisam ser escritos com . invés de ,)')
        ta = 0
system('clear')

while b == 0:
    try:
        b = int(input('Número de habitantes da segunda cidade: '))
    except:
        system('clear')
        print('Valor inválido! Precisa ser um número inteiro.\n')
        b = 0

while tb == 0:
    print('\nAVISO! A taxa de crescimento será mantida em relação ao número de habitantes.')
    try:
        tb = float(input('Taxa de crescimento (%): '))
    except:
        system('clear')
        print('Valor Inválido! Tente novamente! (Lembre-se: Números decimais precisam ser escritos com . invés de ,)')
system('clear')

c = 0

if a < b:
    while a <= b:
        t1 = ta*(a / 100)
        a = a + t1

        t2 = tb*(b / 100)
        b = b + t2
        
        c += 1
    else:
        print(f'Com a cidade A tendo uma população de {trunc(a)} habitantes;\nCom a cidade B tendo {trunc(b)} habitantes; \nForam necessário {c} anos')
elif a > b:
    while b >= a:
        t1 = ta*(a / 100)
        a = a + t1

        t2 = tb*(b / 100)
        b = b + t2
        
        c += 1
    else:
        print(f'Com a cidade A tendo uma população de {trunc(a)} habitantes;\nCom a cidade B tendo {trunc(b)} habitantes; \nForam necessário {c} anos')
else:
    print('Ambos já possuem a mesma quantidade de habitantes! ')
