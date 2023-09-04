# Escreve  um  programa  que  pergunte  o  salário  do  funcionário  e  calcule  o  valor  do  aumento.  
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.  

salario = float(input('Salário do funcionário: '))

if salario > 1250:
    aumento = salario / 10
else:
    aumento = (salario / 100)*15

print(f'Novo salário: R$ {salario+aumento:.2f} - Aumento: R$ {aumento:.2f}')
