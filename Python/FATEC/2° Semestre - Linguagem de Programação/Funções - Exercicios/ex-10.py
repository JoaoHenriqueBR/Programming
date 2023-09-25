# Crie uma função chamada conta_palavras que aceite uma string como parâmetro e retorne o número de palavras na string

def conta_palavras():
    frase = input('Digite uma frase: ').strip()
    palavras = frase.split()
    print(f'Número de palavras: {len(palavras)}')

conta_palavras()
