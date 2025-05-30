'''
Faça um programa que tenha uma função chamada área(),
    que receba as dimensões de um terreno (largura e comprimento) e
    mostre a área do terreno.
'''

def area(larg, comp):
    print(f"Área do terreno {larg}x{comp}: {larg*comp}m².")


# Programa Principal
print('-'*20)
print(f'{"Controle de Terrenos":^20}')
print('-'*20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
