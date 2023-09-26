# Crie uma função chamada remove_elemento que aceite uma lista e um elemento como parâmetros e remova todas as ocorrências desse elemento da lista. 

def remove_elemento(lista, n):
    try:
        while True:
            lista.remove(n)
    except ValueError:
        pass
    print(lista)

remove_elemento(lista=[1, 2, 8, 3, 4, 8, 5, 8, 6 ], n=int(input('Que elemento deseja remover: ')))
