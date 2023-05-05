# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou da hora de se alistar.
# Também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))

ano = date.today().year
id = ano - nasc

print('Você tem {} anos!'.format(id))
if 18 - id >= 2:
    print('Ainda faltam {} anos para se alistar!'.format(18-id))
    print('Seu alistamento será em {}!'.format(ano + (18-id)))
elif 18 - id == 1:
    print('Ainda falta um ano para se alistar!')
    print('Seu alistamento será em {}!'.format(ano + (18-id)))
elif id == 18:
    print('Está na hora de se alistar!')
elif id - 18 == 1:
    print('Já passou um ano do prazo para se alistar.')
    print('Seu alistamento foi em {}!'.format(ano - (id - 18)))
else:
    print('Já passaram {} anos do prazo para se alistar.'.format(id-18))
    print('Seu alistamento foi em {}!'.format(ano - (id - 18)))
