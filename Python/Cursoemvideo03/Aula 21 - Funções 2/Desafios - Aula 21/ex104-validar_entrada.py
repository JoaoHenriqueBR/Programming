'''
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = leiaint('Digite um n')
'''

def leiaint(msg):
    n = ''
    
    while n.isnumeric() == False:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou {n}.')
