# Crie uma função chamada calcula_fatorial que aceite um número inteiro como parâmetro e retorne o fatorial desse número.

def calcula_fatorial():
    fat = n
    for c in range(n-1, 1, -1): # calcula o fatorial
        fat = fat * c
    return fat

n = int(input('Digite um número: '))

print(f'Fatorial de {n}!: {calcula_fatorial()}')
