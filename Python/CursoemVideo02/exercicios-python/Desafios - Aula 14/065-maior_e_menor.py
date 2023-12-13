# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = total = c = 0
r = 's'
while r == 's':
    r = 'a'
    n = int(input('Digite um número: '))
    total += n
    c += 1
    if n > maior:
        maior = n
    if n < menor or c == 1:
        menor = n
    while r not in 'sn': # Impede o usuário de terminar o programa "sem querer".
        r = input('Deseja continuar? (s/n): ').lower().strip()

print('Média: {}'.format(total/c))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
