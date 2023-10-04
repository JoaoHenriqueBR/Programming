# Crie uma função chamada copiaString que recebe duas strings como parâmetros e copia o conteúdo da primeira para a segunda.

def copiaString(a, b):
    b = b + a
    return b

print('B = {}'.format(copiaString(a=input('Digite a primeira string (A): '), b=input('Digite a segunda (B): '))))
