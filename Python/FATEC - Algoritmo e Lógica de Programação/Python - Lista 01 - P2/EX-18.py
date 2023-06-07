'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, 
a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

1. Preço do pão: R$ 0.18

2. Panificadora Pão de Ontem - Tabela de preços

3. 1 - R$ 0.18

4. 2 - R$ 0.36

5. ...

6. 50 - R$ 9.00
'''

from os import system

print('{} Panificadora Pão de Ontem - Tabela de preços {}'.format('='*10, '='*10))

pao = 0
while pao < 0.01:
    print('Exemplo -> Preço do pão: R$ 0.18')
    try:
        pao = float(input('Informe o preço do pão: R$ '))
    except:
        pass
    if pao > 0:
        break
    system('clear')
    print('Valor inválido! Tente novamente.')

for p in range(50):
    print('{}. R$ {:.2f}'.format(p+1, pao * (p+1)))
