# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] Soma;
# [2] Multiplicação;
# [3] Maior;
# [4] Novos números;
# [5] Sair do programa.
#
# Seu programa deverá realizar a operação solicitada em cada caso.
#

a = int(input('Digite um número: '))
b = int(input('Digite outro: '))


r = 0
n = [a, b]
while r != 'n':
    print('''
[1] Soma;
[2] Multiplicação;
[3] Maior;
[4] Novos números;
[5] Sair do programa.
''')

    x = 0
    r = int(input('O que deseja fazer?: '))
    match r:
        case 1:
            for c in n:
                x += c
            print(f'Soma: {x}')
        case 2:
            x = 1
            for c in n:
                x *= c
            print(f'Multiplicação: {x}')
        case 3:
            x = max(n)
            print(f'Maior: {x}')
        case 4:
            x = int(input('Digite o número: '))
            n.append(x)
        case 5:
            print('Obrigado por usar!')
            break
        case _:
            print('Valor errado, tente novamente!')
    while r <= 3:
        r = str(input('Deseja fazer outra operação? (s/n): ')).lower().strip()
        if r == 'n':
            print('Obrigado por usar!')
            break
        elif r == 's':
            break
        else:
            print('Valor inválido! Tente novamente (s ou n).')
            r = 0
