'''
Faça um programa que tenha uma função chamada escreva(),
    que recebe um texto qualquer como parâmetro e
    mostre uma mensagem com tamanho adaptável.

Ex:
    escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
'''


def escreva(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(f'{txt:^{tam}}')
    print('~'*tam)


# Programa Principal
escreva('Olá, Mundo!')
escreva('Vamos Brasil!!!')
escreva('JH')
