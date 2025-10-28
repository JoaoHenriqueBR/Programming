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
