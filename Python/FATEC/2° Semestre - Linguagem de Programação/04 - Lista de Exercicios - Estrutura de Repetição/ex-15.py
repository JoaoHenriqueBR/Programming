'''
Escreva  um  programa  para  controlar  uma  pequena  maquina  registradora.  
Você  solicita  o  usuário que digite o código do produto e a quantidade comprada. 
Utilize a tabela de códigoa seguir para obter o preço de cada produtor. 
•Código 1 – Preço R$ 0,50 
•Código 2 – Preço R$ 1,00 
•Código 4 – Preço R$ 4,00
•Código 5 – Preço R$ 7,00 
•Código 9 – Preço R$ 8,00 
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Quaisquer outros códigos devem gerar a mensagem de erro “Código Invalido”.
'''
bool = True
preco = tot = 0
while bool == True:
    while preco == 0:
        cod = int(input('Informe o código do produto: '))
        match cod:
            case 0:
                bool = False
                break
            case 1:
                preco = 0.5
            case 2:
                preco = 1
            case 4:
                preco = 4
            case 5:
                preco = 7
            case 9:
                preco = 8
            case _:
                print('Código Inválido!')
    if cod != 0:
        qtd = int(input('Quantidade: '))
        tot += preco * qtd
        print('Registrado...')
        preco = 0

print('')
print(f'Valor total da Compra: R$ {tot:.2f}')
