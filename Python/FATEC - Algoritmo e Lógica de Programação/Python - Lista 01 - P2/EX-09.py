# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

from os import system # importa o system('clear')

print('{} Fatorial de um número (0-16)! {}'.format('='*10, '='*10)) # titulo

r = 's'
while r == 's': # inicia o programa
    try: # tenta ler um valor
        n = int(input('Digite um número: '))
    except: # se erro
        n = -1 # invalida o número
    if n > 0 and n <= 16: # se válido
        fat = n
        for c in range(n-1, 1, -1): # calcula o fatorial
            fat = fat * c
        print(f'Fatorial de {n}! é igual a: {fat}')
        r = input('Deseja saber a fatorial de outro número? digite (s) caso sim: ').lower().strip()
        system('clear')
    else: # se inválido
        system('clear')
        print('Inválido! Precisa ser um número inteiro entre 0 e 16. ')
else: # se finalizado
    print('PROGRAMA FINALIZADO! Obrigado por usár-lo!')
