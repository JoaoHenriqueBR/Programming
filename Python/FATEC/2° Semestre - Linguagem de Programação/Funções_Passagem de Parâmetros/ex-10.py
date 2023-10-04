# Crie uma função chamada contaVogais que recebe uma string como parâmetro e retorna o número de vogais na string.

def contaVogais(frase):
    vogal = 0
    for letra in frase:
        if letra in 'aáãeéêioóôuAÁÃEÉÊIOÓÔUÚÜ':
            vogal += 1
    return vogal

print('{} Vogais.'.format(contaVogais(frase=input('Digite algo: '))))
