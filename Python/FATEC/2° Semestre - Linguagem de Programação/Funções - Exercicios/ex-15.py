# Crie uma função chamada eh_primo que aceite um número como parâmetro e retorne True se o número for primo ou False caso contrário. 


def eh_primo(n):
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1
    if tot == 2:
        return True
    else:
        return False

print(eh_primo(n=int(input('Digite um número inteiro: '))))
