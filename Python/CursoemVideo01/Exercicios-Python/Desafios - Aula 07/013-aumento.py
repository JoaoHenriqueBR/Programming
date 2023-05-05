# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento,

s = int(input('Qual era seu salário? '))
a = (s / 100)*15

print('Seu novo salário será de R$ {:.2f}! '.format(s+a))
