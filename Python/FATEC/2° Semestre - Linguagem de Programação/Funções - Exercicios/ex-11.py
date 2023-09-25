# Crie uma função chamada acha_menor que aceite uma lista de números como parâmetro e retorne o menor número da lista. 


numeros = []
def acha_menor(numeros):
    menor = min(numeros)
    return menor

while (1):
    x = int(input('Acrescente um número (0 para parar): '))
    if x == 0:
        break
    numeros.append(x)

print(f'Lista:{numeros}.\nMenor: {acha_menor(numeros)}')
