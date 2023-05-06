# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: apos a sopa

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
tam = len(frase)
palindromo = 0


for c in range(tam):
    if ('{}'.format(frase[c])) == ('{}'.format(frase[tam-(c+1)])):
        palindromo = palindromo + 1

if tam == palindromo:
    print('É um palindromo! ')
else:
    print('NÃO é um palindromo! ')




