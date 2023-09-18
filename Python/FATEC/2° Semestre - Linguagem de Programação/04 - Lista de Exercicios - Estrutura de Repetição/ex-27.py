# Escreva um programa que verifique se um numero é palíndromo. Um número palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501. 

while (1):
    n = str(input('Digite um número: ')).strip().replace(' ', '')
    if n.isdigit() == True:
        break
    else:
        print('Valor inválido! ')

inverso = n[::-1]

print('O inverso de {} é {}'.format(n, inverso))
if inverso == n:
    print('Portanto, é um palindromo! ')
else:
    print('Portanto, NÃO é um palindromo! ')

