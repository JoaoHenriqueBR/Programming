a = int(input('Ano do nascimento (/aaaa/):'))
m = int(input('Mês do nascimento (/mm/): '))
d = int(input('Dia do nascimento (/dd/): '))
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto',
        'setembro', 'outubro', 'novembro', 'dezembro']

if m > 12 or d > 31 or a <= 0:
    print('DATA INVÁLIDA! Tente novamente!')
else:
    print('Data de nascimento: {}/{}/{} Você nasceu em {} de {} de {}!'.format(d, m, a, d, mes[m-1], a))
