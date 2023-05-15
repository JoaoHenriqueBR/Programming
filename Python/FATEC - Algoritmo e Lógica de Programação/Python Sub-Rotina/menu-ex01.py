from time import sleep

cont = 0
saldo = 0
media = 0
c = 's'

while c == 's':
    inv = 0
    try:
        x = float(input('digite um valor: '))
    except:
        print('Valor invalido! O valor precisa ser númerico. ')
        x = 0
        inv += 1
    if inv >= 1:
        print('NÃO REGISTRADO! ')
    else:
        print('REGISTRADO! ')
    cont += 1 - inv
    saldo += x
    try:
        media = saldo/cont
    except ZeroDivisionError:
        media = 0
    c = ' '
    while c not in 'sn':
        c = str(input('Deseja digitar outro valor? (s/n): ')).lower()

print('Processando... ')
sleep(1.5)
nome = input('Por último, informe seu nome: ')
print('\nObrigado {}\n! '.format(nome))
print('Foi registrado {} valores.'.format(cont))
print('Saldo: {}'.format(saldo))
print('Média: {}'.format(media))
