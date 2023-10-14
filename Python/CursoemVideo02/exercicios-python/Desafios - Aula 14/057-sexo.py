# Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'False'
while sexo not in 'MF':
    sexo = input('Seu sexo (M/F): ')
    