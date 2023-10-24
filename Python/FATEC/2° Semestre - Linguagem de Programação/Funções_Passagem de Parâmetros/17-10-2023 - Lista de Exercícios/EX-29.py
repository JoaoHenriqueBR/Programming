# Crie um programa que determine se uma frase é um palíndromo 
# (ou seja, pode ser lida da mesma forma de trás para frente, desconsiderando espaços e diferenciação entre maiúsculas e minúsculas).

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
tam = len(frase)
inverso = frase[::-1]

print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
    print('Portanto, é um palindromo! ')
else:
    print('Portanto, NÃO é um palindromo! ')
