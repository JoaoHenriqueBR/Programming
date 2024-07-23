'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extensão,
de zero até vinte,

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze', 
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(extenso[n])
        r = input('deseja continuar? (s/n): ').lower().strip()
        if r == 'n':
            print('\nPrograma Finalizado! Obrigado por usar-lo.')
            break
    else:
        print('Valor errado! Tente novamente.')
