'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços,
na sequência.

No final, mostre uma listagem de preços, 
organizando os dados em forma tabular
'''

tabela = ("Pão", 1.8, "Hamburguer", 5, "Coxinha", 4, "Pão de Queijo", 3)

print('-'*43)
print(f'{"TABELA DE PREÇOS DO JH":^43}')
print('-'*43)

for i in range(0, len(tabela), 2):
    print(f"{tabela[i]:.<30} | R$ {tabela[1+i]:>7.2f}")

print('-'*43)
