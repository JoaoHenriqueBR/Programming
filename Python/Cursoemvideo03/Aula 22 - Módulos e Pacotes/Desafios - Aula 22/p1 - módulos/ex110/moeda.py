def aumentar(n = 0, taxa = 0, formatar=False):
    res = n + (n * taxa/100)
    return res if formatar is False else moeda(res)

def diminuir(n = 0, taxa = 0, formatar=False):
    res = n - (n * taxa/100)
    return res if formatar is False else moeda(res)

def dobro(n = 0, formatar=False):
    return n * 2 if formatar is False else moeda(n*2)

def metade(n = 0, formatar=False):
    return n / 2 if formatar is False else moeda(n/2)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:>.2f}'.replace('.',',')

def resumo(preco, aumento = 0, reduzir = 0):
    print('-'*30)
    print(f'{'CALCULADORA DE PREÇOS':^30}')
    print('-'*30)

    print(f'Preço calculado: \t{moeda(preco)}')
    print('-'*30)

    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Aumentando {aumento}%: \t{aumentar(preco, aumento, True)}')
    print(f'Diminuindo {reduzir}%: \t{diminuir(preco, reduzir, True)}')
    print('-'*30)


