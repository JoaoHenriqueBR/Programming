'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

c = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    soma += n

print(f'Qtd. de Números digitados: {c}')
print(f'Soma: {soma}')
