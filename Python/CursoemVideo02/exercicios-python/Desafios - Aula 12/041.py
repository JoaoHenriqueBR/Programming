# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
id = atual - nasc

print('Você tem {} anos!'.format(id))
if id <= 9:
    print('Na natação, sua categoria é MIRIM!')
elif id <= 14:
    print('Na natação, sua categoria é INFANTIL!')
elif id <= 19:
    print('Na natação, sua categoria é JUNIOR!')
elif id <= 20:
    print('Na natação, sua categoria é SÊNIOR!')
else:
    print('Na natação, sua categoria é MASTER!')
