# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida. 

from time import sleep

op = ''
bool = True
while bool == True:
  print(f'''
{'='*18}
TABUADA AUTOMÁTICA
{'='*18}

1 - Adição;
2 - Subtração;
3 - Divisão;
4 - Multiplicação;
5 - Sair

{'='*18}
''')
  r = int(input('Sua escolha: '))
  if r >= 0 and r < 5:
    n = int(input('Número que deseja saber a tabuada: '))
    print('')
    match r:
      case 1:
        op = '+'
        for c in range(1, 11):
          print('{} {} {} = {}'.format(n, op, c, n+c))
      case 2:
        op = '-'
        for c in range(1,11):
          print('{} {} {} = {}'.format(n, op, c, n-c))
      case 3:
        op = '/'
        for c in range(1,11):
          print('{} {} {} = {}'.format(n, op, c, n/c))
      case 4:
          op = 'x'
          for c in range(1,11):
            print('{} {} {} = {}'.format(n, op, c, n*c))
  elif r == 5:
    print('Obrigado por usar o programa! ')
    break
  else:
    print('\nValor Inválido! Tente novamente.')
    sleep(1)
