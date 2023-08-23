# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de Idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres tem menos de 20 anos.

velho = jovem_mulher = total = 0
nome_velho = ''

for p in range(1, 5):
    print('-----{}° PESSOA-----'.format(p))
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Sua idade: '))
    sexo = input('Seu sexo (m ou f): ').strip()
    total += idade
    if idade > velho and sexo in 'mM':
        velho = idade
        nome_velho = nome
    if idade < 20 and sexo in 'fF':
        jovem_mulher += 1

print('Média de idade: {} anos'.format(total/4))
print('Homem mais velho: {} - {} anos'.format(nome_velho, velho))
print('Mulheres com menos de 20 anos: {} mulheres'.format(jovem_mulher))
