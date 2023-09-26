# Crie uma função chamada mesma_quantidade que aceite duas listas como parâmetros e retorne True se ambas tiverem o mesmo número de elementos ou False caso contrário.



def mesma_quantidade():
    a = []
    b = []
    while (1):
        x = (input('Acrescente algo na lista A (0 para parar): '))
        if x == '0':
            print('LISTA A COMPLETA!\n')
            while (2):
                x = (input('Acrescente algo na lista B (0 para parar): '))
                if x == '0':
                    print('LISTA B COMPLETA!\n')
                    break
                b.append(x)
            break
        a.append(x)
    print('Estas listas possuem o mesmo numero de elementos: ', end='')    
    if len(a) == len(b):
        return True
    else:
        return False

print(mesma_quantidade())
