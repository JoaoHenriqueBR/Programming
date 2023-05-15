a = str(input('Digite algo: ')).lower()

vogais = 0
spaces = a.count(' ')

for a in a:
    if a in 'aeiou':
        vogais += 1

print('Número de espaços: {}'.format(spaces))
print('Número de vogais: {}'.format(vogais))
