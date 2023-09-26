# Crie uma função chamada imprime_dicionario que aceite um dicionário como parâmetro e imprima todas as chaves e valores do dicionário.

dicionario = {}
def imprime_dicionario(dicionario):
    for item in dicionario:
        print(f'{item} -> {dicionario[item]}')

while (1):
    print('Construindo o dicionário...')
    a = input('Categoria do conteúdo: ')
    b = input('Conteúdo: ')
    dicionario[a] = b
    if input('Deseja continuar? (0 para parar): ') == '0':
        break

imprime_dicionario(dicionario)
