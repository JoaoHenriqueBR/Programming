# Crie uma função chamada fatorial que recebe um número inteiro como parâmetro e retorna o fatorial desse número

def fatorial(n):
    fat = n
    for c in range(n-1, 1, -1): # calcula o fatorial
        fat = fat * c
    return fat

print('Fatorial: {}'.format(fatorial(n=int(input('Digite um número: ')))))
