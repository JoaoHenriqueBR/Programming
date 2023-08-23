num = int(input('Digite um número (<800): '))
n = str(num)
if num < 800:
    print('Centena: {}'.format(n[0]))
    print('Dezena: {}'.format(n[1]))
    print('Unidade: {}'.format(n[2]))
else:
    print('Numero tem que ser menor que 800!')
