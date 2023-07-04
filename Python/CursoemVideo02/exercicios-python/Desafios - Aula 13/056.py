# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de Idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres tem menos de 20 anos.

velho = jovem_mulher = velho_homem = total = 0
nome_velho = ''

for p in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Sua idade: '))
    sexo = input('Seu sexo (m ou f): ')
    total += idade
    if idade > velho:
        velho = idade
        if sexo == 'm':
            nome_velho = nome
            velho_homem = idade
    if idade < 20 and sexo == 'f':
        jovem_mulher += 1

print('Média de idade: {} anos'.format(total/4))
print('Homem mais velho: {} - {} anos'.format(nome_velho, velho_homem))
print('Mulheres com menos de 20 anos: {} mulheres'.format(jovem_mulher))
