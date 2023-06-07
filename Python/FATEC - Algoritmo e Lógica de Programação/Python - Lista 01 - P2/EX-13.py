# Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

from os import system
from time import sleep

print('{} Pesquisa - Idade da Turma {}'.format('='*10, '='*10)) # titulo

n = -1
while n < 0: # loop em caso de erro
    try: # tenta ler um valor
        n = int(input('Nº de participantes da pesquisa: '))
    except: # se erro
        system('clear')
    if n > 0:
        total = 0
        for c in range(n):
            print('{} {}º Pessoa {}'.format('-'*10, c+1, '-'*10)) # titulo
            try:
                i = int(input('Quantos anos você tem: '))
            except:
                system('clear')
                print('Inválido! Precisa ser um número inteiro positivo. ')
                i = 0
                n = n - 1
                print('Valor será desconsiderado! ')  
            total += i
            print('\nObrigado pela contribuição! Aguarde...')
            sleep(3)
            system('clear')
        break    
    print('Inválido! Precisa ser um número inteiro positivo. ')

media = total / n
print(f'Média de idade: {media} anos.')

if media < 26:
    print('Turma jovem!')
elif media >= 26 and media <= 60:
    print('Turma adulta!')
else:
    print('Turma velha')