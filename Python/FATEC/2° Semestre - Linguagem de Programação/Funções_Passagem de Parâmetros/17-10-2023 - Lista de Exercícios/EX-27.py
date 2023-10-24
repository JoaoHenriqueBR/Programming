# Crie uma função chamada contaCaracteresUnicos que recebe uma string como parâmetro e retorna o número de caracteres únicos na string.

def contaCaracteresUnicos(string):
    unico = []
    n = 0
    for i in string:
        if i not in unico:
            unico.append(i)
            n += 1
    return unico, n

string = 'Pão de Batata'
unico, n = contaCaracteresUnicos(string)


print(f'Caracteres únicos: {unico}')
print(f'Qtde.: {n}')
