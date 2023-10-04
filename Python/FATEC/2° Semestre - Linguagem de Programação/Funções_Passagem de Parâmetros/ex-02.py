# Crie uma função chamada trocar que recebe dois inteiros como parâmetros e troca seus valores.

def trocar(a, b):
    x = a
    a = b
    b = x
    print(f'A virou {a} e B virou {b}.')

trocar(a=int(input('A - Digite um número: ')), b=int(input('B - Digite outro: ')))
