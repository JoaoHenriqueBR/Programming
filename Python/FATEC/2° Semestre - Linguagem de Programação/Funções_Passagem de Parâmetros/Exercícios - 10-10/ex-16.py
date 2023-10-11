# Crie uma função chamada contaCaracteres que recebe uma string e um caractere como parâmetros e retorna o número de vezes que o caractere aparece na string. 

def contaCaracteres(string, caractere):
    quant = 0
    for c in string:
        if c == caractere:
            quant += 1
    return quant

print(contaCaracteres(string='Pão de Batata', caractere='t'))
