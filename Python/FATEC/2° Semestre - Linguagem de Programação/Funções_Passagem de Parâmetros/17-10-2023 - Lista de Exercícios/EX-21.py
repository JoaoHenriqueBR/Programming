'''
Crie uma função chamada calculaSomaMedia que recebe uma lista  de inteiros 
e seu tamanho como parâmetros e calcula a soma e a média dos valores no lista, 
retornando ambos os resultados.
'''


def calculaSomaMedia(inteiros, tam):
    soma = sum(inteiros)
    media = soma / tam
    return soma, media

inteiros = [2, 2, 2, 2, 2]
tam = len(inteiros)

x, y = calculaSomaMedia(inteiros, tam)

print(f'Soma: {x}')
print(f'Média: {y}')
