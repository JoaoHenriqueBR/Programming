def lin():
    print('-='*30)

def soma(a,b):
    # Os valores são passados pelos parâmetros A e B, limitando a função aos parâmetros definidos.
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma A + B = {s}')

# Para mais valores serem acrescentados indefinidamente:
def contador(*num):
    # Os valores passados pelos parâmetros são empacotados e salvos em uma tupla.
    '''
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    '''

    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

def dobra(lst):
    # Os valores também podem ser passados como uma lista (variável composta).
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        

# Programa Principal
soma(4, 5)
lin()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
lin()

valores = [6, 3, 9, 1, 0, 2]

dobra(valores)
print(valores)
