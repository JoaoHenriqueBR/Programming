# Faça um algoritmo que leia a idade de uma pessoa expressa em anos e meses. 
# Entre com a idade da segunda pessoa da mesma forma 
# Considerar ano com 365 dias e mês com 30 dias. 
# Verificar a pessoa mais velha e o resultado do cálculo.

print('------ Primeira Pessoa ------\n')
a1 = int(input('Quantos anos possui: '))
m1 = int(input('Quantos meses: '))

print('\n------ Segunda Pessoa ------\n')
a2 = int(input('Quantos anos possui: '))
m2 = int(input('Quantos meses: '))

total1 = (a1 * 365) + (m1 * 30)
total2 = (a2 * 365) + (m2 * 30)

if total1 > total2:
    print('A primeira pessoa é mais velha!')
    print('Diferença: {} dias.'.format(total1-total2))
elif total2 > total1:
    print('A segunda pessoa é a mais velha!')
    print('Diferença: {} dias.'.format(total2-total1))
else:
    print('Ambas tem a mesma idade!')
