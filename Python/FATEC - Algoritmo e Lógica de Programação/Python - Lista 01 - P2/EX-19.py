'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

1. Lojas Tabajara

2. Produto 1: R$ 2.20

3. Produto 2: R$ 5.80

4. Produto 3: R$ 0

5. Total: R$ 9.00

6. Dinheiro: R$ 20.00

7. Troco: R$ 11.00

8. ...
'''

from os import system

print('{} Lojas Tabajara {}'.format('='*10, '='*10))

c = 1
valor = total = 0
while c > 0:
    try:
        valor = float(input(f'Produto {c}: R$ '))
    except:
        print('Valor Inválido! Tente novamente.')
        continue
    c += 1
    total += valor
    if valor == 0:
        print('Total: R$ {:.2f}'.format(total))
        try:
            pago = float(input('Dinheiro: R$ '))
        except:
            print('Valor Inválido! Tente novamente.')
            continue
        print('Troco: R$ {:.2f}'.format(pago - total))
        try:
            c = int(input('Deseja continuar? Pressione 0 para finalizar: '))
        except:
            pass
        valor = total = 0

print('Caixa finalizado! Obrigado por usar o programa!')
