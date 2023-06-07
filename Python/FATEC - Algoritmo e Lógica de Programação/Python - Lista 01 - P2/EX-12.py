# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

from os import system

print('{} NÚMEROS PRIMOS DENTRO DE UMA SEQUÊNCIA {}'.format('='*10, '='*10)) # titulo

n = -1
while n < 0: # loop em caso de erro
    try: # tenta ler um valor
        n = int(input('Digite um número inteiro: '))
    except: # se erro
        system('clear')
    if n > 0:
        break    
    print('Inválido! Precisa ser um número inteiro positivo. ')

divs = 0
primo = [1, 2, 3] # Lista de números primos com características diferentes dos demais (Pode ser dividido por 2 ou 3)
del primo[n:3] # Se o usuário digitar 1, 2, 3, valores que são maiores serão apagados da lista

for c in range(5, n+1, 2):
    divs += 2 # Conta o número de divisões
    if c % 2 != 0 and c % 3 != 0: # realiza duas divisões para ver se o número é primo
        primo.append(c) # Se for primo, ele é adicionado a lista de primos


print(f'Números primos: {primo}')
print(f'Divisões executadas: {divs}')
