# Crie uma função chamada contador_vogais que aceite uma string como parâmetro e retorne o número de vogais na string.

def contador_vogais(frase):
    vogal = 0
    for letra in frase:
        if letra in 'aáãeéêioóôuAÁÃEÉÊIOÓÔU':
            vogal += 1
    return vogal


frase = input('Digite uma frase: ')

print(f'Na frase {frase}, tem {contador_vogais(frase)} vogais.')
