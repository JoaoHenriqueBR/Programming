'''
Escreva  um  programa  que  calcular  a  categoria  de  um  produto  e  determine  o  preço  pela  tabela: 
Categoria 1 valor de R$ 10,00; 
Categoria 2 valor de R$ 15,00; 
Categoria 3 valor de R$ 19,00; 
Categoria 4 valor de R$ 23,00 e 
Categoria 5 valor de R$ 27,00. 
'''

c = 0

print('='*30)
print('Consulta de Preço / Categoria')
print('='*30)

while c == 0:
    c = int(input('Categoria do Produto: '))
    if c <= 5 and c >= 1:
        break
    else:
        print('Valor Inválido, Tente novamente.')
        c = 0

tabela = ['R$ 10.00', 'R$ 15.00', 'R$ 19.00', 'R$ 23.00', 'R$ 27.00']

print(f'Preço do produto: {tabela[c-1]}')
