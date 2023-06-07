# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

from os import system
from time import sleep

print('{} Pesquisa de eleitores {}'.format('='*10, '='*10)) # titulo

n = -1
while n < 1:
    try:
        n = int(input('Número de eleitores: '))
    except:
        pass
    if n >= 1:
        break
    system('clear')
    print('Valor inválido! Tente novamente.')

a = 0
b = 0
c = 0
null = 0

for x in range(n):
    print(f'------ Eleitor {x+1} ------')
    print('[1] para Candidato A \n[2] para Candidato B \n[3] para Candidato C \n[Outro] Anula o voto ')
    try:
        v = int(input('Seu voto:'))
    except:
        v = 0
        pass
    if v == 1:
        a = a + 1
    elif v == 2:
        b = b + 1
    elif v == 3:
        c = c + 1
    else:
        system('clear')
        print('Voto anulado! Aguarde...')
        sleep(2)
        system('clear')
        null += 1    

print(f'Candidato A: {a} votos!')
print(f'Candidato B: {b} votos!')
print(f'Candidato C: {c} votos!')
print(f'Foram anulados {null} votos.')
