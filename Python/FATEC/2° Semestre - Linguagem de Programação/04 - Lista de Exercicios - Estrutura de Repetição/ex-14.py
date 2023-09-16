# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética

n = 1
c = soma = 0
while n != 0:
    n = int(input('Digite um número (0 para parar): '))
    if n == 0:
        break
    c += 1
    soma += n

media = soma / c

print(f'Números digitados: {c}.')
print(f'Soma: {soma}.')
print(f'Média: {media}.')
