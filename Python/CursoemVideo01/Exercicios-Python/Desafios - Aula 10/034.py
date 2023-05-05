# Escreva um programa que calcule o salário de um funcionário e calcule o valor do seu aumento.
#
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário atual: '))

if salario > 1250:
    aumento = (salario / 100)*10
else:
    aumento = (salario / 100)*15

print('Seu novo salário será de: R$ {:.2f}!'.format(salario + aumento))
print('Com um aumento de R$ {:.2f}!'.format(aumento))
