'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deve perguntar se o usuário quer ou não continuar.
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres com menos de 20 anos.
'''

maior = garota = homem = 0
while True:
    print('-'*30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-'*30)
    idade = int(input('IDADE: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    if sexo == 'M':
        homem += 1
    if idade >= 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        garota += 1
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print(f'{maior} pessoas acima de 18.')
print(f'{homem} homens.')
print(f'{garota} mulheres com menos de 20.')
