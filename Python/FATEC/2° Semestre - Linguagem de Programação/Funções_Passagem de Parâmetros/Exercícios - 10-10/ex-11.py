#  Crie uma função chamada verificaPrimo que recebe um número inteiro como parâmetro e retorna 1 se o número for primo e 0 caso contrário. 

def verificaPrimo(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1
    if tot == 2:
        return 1
    else:
        return 0

print(verificaPrimo(n=4)) # Chama a função e declara o número que será verificado
