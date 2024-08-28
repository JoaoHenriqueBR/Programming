'''
Crie um programa que tenha uma tupla
com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais.
'''

palavras = ("pao", "Ronaldo", "Brasil", "Garrincha", "aprender", "programar")

for p in palavras:
    print(f"\nVogais de {p.upper()} = ", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('')
