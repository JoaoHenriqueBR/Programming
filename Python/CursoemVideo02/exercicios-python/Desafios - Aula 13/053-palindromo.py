# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: apos a sopa

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
tam = len(frase)
inverso = frase[::-1]

print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Portanto, é um palindromo! ')
else:
    print('Portanto, NÃO é um palindromo! ')

