# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag).

total = []
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    total.append(n)
    soma = sum(total)

print('Números: {}'.format(total))
print('Soma: {}'.format(soma))
