# Crie uma função chamada contador_caracteres que aceite uma string e um caractere como parâmetros e retorne o número de vezes que o caractere aparece na string. 

def contador_caracteres(string, caractere):
    c = 0
    for letra in string:
        if letra == caractere:
            c += 1
    print(f'{c} caracteres.')

contador_caracteres(string=input('Digite uma frase: '), caractere=input('Digite um caractere: '))
