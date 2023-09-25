# Crie uma função chamada eh_palindromo que aceite uma string como parâmetro e retorne True se a string for um palíndromo (pode ser lida igual de trás para frente) ou False caso contrário. 


def eh_palindromo(frase):
    tam = len(frase)
    inverso = frase[::-1]
    if inverso == frase:
        return True
    else:
        return False

print(eh_palindromo(frase=str(input('Digite uma frase: ')).strip().lower().replace(' ', '')))
