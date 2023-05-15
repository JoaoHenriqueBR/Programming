a = str(input('Digite algo (será considerado uma string): '))
b = str(input('Digite algo (será considerado outra string): '))

s = a+b
t = len(s)

print('{} - Tamanho: {} caracteres.'.format(s, t))

if len(a) > len(b):
    print('Primeira string é a maior! ')
elif len(b) > len(a):
    print('Segunda string é a maior!')
else:
    print('Ambas strings possuem o mesmo tamanho! ')
    if a == b:
        print('Possuindo o mesmo conteúdo. ')
    else:
        print('Com conteúdos diferentes.')
