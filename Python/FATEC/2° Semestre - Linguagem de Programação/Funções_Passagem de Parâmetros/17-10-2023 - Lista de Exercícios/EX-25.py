# Crie uma função chamada verificaPalindromo que recebe uma string como parâmetro 
# e retorna 1 se a string for um palíndromo (ou seja, lê-se da mesma forma da esquerda para a direita e da direita para a esquerda) e 0 caso contrário

def verificaPalindromo(string):
    inverso = string[::-1]
    if inverso == string:
        return 1
    else:
        return 0

palindromo = verificaPalindromo(string='aposasopa')
normal = verificaPalindromo(string='pão')


print(palindromo, normal)
