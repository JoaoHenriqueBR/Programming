'''
O cardápio de uma lanchonete é o seguinte:

a. Especificação Código Preço

b. Cachorro Quente 100 R$ 1,20

c. Bauru Simples 101 R$ 1,30

d. Bauru com ovo 102 R$ 1,50

e. Hambúrguer 103 R$ 1,20

f. Cheeseburguer 104 R$ 1,30

g. Refrigerante 105 R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

from os import system

c = 0
total = 0

cardapio = {100:'Cachorro Quente - R$ 1.20',
            101:'Bauru Simples - R$ 1.30',
            102:'Bauru com ovo - R$ 1.50',
            103:'Hamburguer - R$ 1.20',
            104:'Cheeseburguer - R$ 1.30',
            105:'Refrigerante - R$ 1.00'}
preco = {100:1.20,
         101:1.30,
         102:1.50,
         103:1.20,
         104:1.30,
         105:1}

print('{} CARDÁPIO {}'.format('-'*90, '-'*90))            
print(cardapio)

while c >= 0:
    qtd = 0
    try:
        c = int(input('Informe o código (0 - Encerra o pedido): '))
    except:
        c = -1
    if c == 0:
        break
    elif c < 100 and c > 105:
        system('clear')
        print('Código inválido! Tente novamente.')
    else:
        while qtd <= 0:
            print(f'Pedido: {cardapio[c]}')
            try:
                qtd = int(input('Quantidade: '))
            except:
                qtd = -1
            if qtd == 0:
                break
            elif qtd < 0:
                system('clear')
                print('Inválido! Tente novamente.')
        pagar = preco[c] * qtd
        print('Valor: R${:.2f}'.format(pagar))
        total += pagar

print('Pedido Finalizado! Total: R$ {:.2f}'.format(total))
