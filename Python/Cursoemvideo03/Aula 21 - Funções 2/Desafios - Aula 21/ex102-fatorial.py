'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:

- O primeiro que indique o número a calcular
- O outro chamado show, que será um valor lógico(opcional)
    - Indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
# Incluir um guia de como usar a função para o help() da função;

def fatorial(n=int, show=False):
    """
    -> Calcula a fatorial.
    :param n: Número a calcular
    :param show: (Opcional) Indica se será mostrado ou não na tela o processo de cálculo do fatorial.
    :return: Resultado da Fatorial
    """
    fat = 1

    for c in range(n, 0, -1):
        if show == True:
            print(f'{c} ', end='')
            if c > 1:
                print(f'x ', end='')
            else:
                print(f'= ', end='')
        fat *= c

    return fat


# Programa Principal
print('-'*30)
print(f'{"Fatorial":^30}')
print('-'*30)

print(fatorial(int(input('Número a ser calculado: ')), show=True))


r = input('\nDeseja ver como funciona o programa? (s/n): ')

if r != 'n':
    help(fatorial)

print('\nObrigado por usar o programa! :)')
