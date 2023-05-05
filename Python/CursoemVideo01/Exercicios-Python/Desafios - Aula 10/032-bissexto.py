from datetime import date

ano = int(input('Veja se um ano é bissexto ou não (0 para o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))
