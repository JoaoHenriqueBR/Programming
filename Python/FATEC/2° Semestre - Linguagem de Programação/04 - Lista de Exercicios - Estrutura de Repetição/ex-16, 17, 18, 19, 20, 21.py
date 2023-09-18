#  EX 16
#
#  Escreva um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor. 
# Para simplificar utilize números inteiros e com cédulas de R$50, R$20, R$10, R$4 e R$1. 
# Após concluído, testes com os seguintes valores: 50, 745, 384, 2, 7 e 1. 

from decimal import Decimal

bool = True
while bool == True: # EX 21 - Reescreva o programa da questão 16 de forma a continuarexecutando até que o valor digitado seja 0. Utilize repetições aninhadas
  val = float(input('Informe o valor (0 Para finalizar): R$ '))
  if val == 0:
    print('Obrigado por usar o programa :)')
    break
  else:
    # EX 18 - Modifique o programa da questão 16 para trabalhar com nota de R$ 100,00 
    cem = val // 100
    val = Decimal(f'{val}') % 100
    
    cinquenta = val // 50
    val = Decimal(f'{val}') % 50
    vinte = val // 20
    val = Decimal(f'{val}') % 20
    dez = val // 10
    val = Decimal(f'{val}') % 10
    qua = val // 4
    val = Decimal(f'{val}') % 4
    um = val // 1
    val = Decimal(f'{val}') % 1
    
    # EX 19 - Modifique o programa da questão 16 para aceitar valores decimais, ou seja, também contar moedas de R$0.01, R$0.02, R$0.05, R$0.10, e R$0.50.  
    moeda_cinquenta = Decimal(f'{val}') // Decimal('0.5')
    val = Decimal(f'{val}') % Decimal('0.5')
    moeda_dez = Decimal(f'{val}') // Decimal('0.1')
    val = Decimal(f'{val}') % Decimal('0.1')
    moeda_cinco = Decimal(f'{val}') // Decimal('0.05')
    val = Decimal(f'{val}') % Decimal('0.05')
    moeda_dois = Decimal(f'{val}') // Decimal('0.02')
    val = Decimal(f'{val}') % Decimal('0.02')
    moeda_um = Decimal(f'{val}') // Decimal('0.01')
    
    print('Para pagar esse valor, será necessário: ')
    print(f'{cem} nota(s) de R$ 100.\n')
    print(f'{cinquenta} nota(s) de R$ 50.')
    print(f'{vinte} nota(s) de R$ 20.')
    print(f'{dez} nota(s) de R$ 10.')
    print(f'{qua} nota(s) (2 de 2) de R$ 4.')
    print(f'{um} moeda(s) de R$ 1.')
    print('')
    print(f'{moeda_cinquenta} moeda(s)de R$ 0.50.')
    print(f'{moeda_dez} moeda(s) de R$ 0.10.')
    print(f'{moeda_cinco} moeda(s) de R$ 0.05.')
    print(f'{moeda_dois} moeda(s) de R$ 0.02.')
    print(f'{moeda_um} moeda(s) de R$ 0.01.')
    print('')
  


# EX 17
'''
- No programa anterior, o que acontece se for digitado 0 (zero) no valor a pagar? 

>
Informe o valor: R$ 0
Para pagar esse valor, será necessário: 
0 nota(s) de R$ 50.
0 nota(s) de R$ 20.
0 nota(s) de R$ 10.
0 nota(s) (2 de 2) de R$ 4.
0 moeda(s) de R$ 1.

'''

# EX 20

'''
- No programa da questão 19, o que acontece se digitarmos 0.001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir esse problema. 

Informe o valor (0 Para finalizar): R$ 0.001
Para pagar esse valor, será necessário: 
0 nota(s) de R$ 100.

0 nota(s) de R$ 50.
0 nota(s) de R$ 20.
0 nota(s) de R$ 10.
0 nota(s) (2 de 2) de R$ 4.
0 moeda(s) de R$ 1.

0 moeda(s)de R$ 0.50.
0 moeda(s) de R$ 0.10.
0 moeda(s) de R$ 0.05.
0 moeda(s) de R$ 0.02.
0 moeda(s) de R$ 0.01.
'''
