'''
Uso do ELIF – Entre com um número de 1 a 7 e exiba o dia correspondente da semana.
Se o número digitado for 1 imprima domingo, Caso o número digitado for 2 imprima
segunda feira, 3 terça feira, 4 quarta feira, 5 quinta feira, 6 sexta feira e 7 sábado.
Quaisquer outros números digitados, emita mensagem de erro. 
'''

n = int(input('Digite um número (1-7): '))

if n == 1:
    print('domingo')
elif n == 2:
    print('segunda')
elif n == 3:
    print('terça')
elif n == 4:
    print('quarta')
elif n == 5:
    print('quinta')
elif n == 6:
    print('sexta')
elif n == 7:
    print('sábado')
else:
    print('ERRO! Tente novamente!')