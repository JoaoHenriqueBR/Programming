print('~='*15)
print('  BEM-VINDO AO CAIXA DO JÃO')
print('~='*15)
r = str(input('Deseja fazer um saque? (s/n): '))

if r == 's' or r == 'S':
    print('\nVALOR MÍNIMO: R$10')
    print('VALOR MÁXIMO: R$600')
    v = float(input('Qual o valor: '))
    print('\nDISPONIVEL: notas de 1, 5, 10, 20, 50 e 100 reais. ')
    print('Em seguida, você irá escolher o número de notas e seu valor')
    d = 0
    while d < v:
        print('\nTOTAL = R${}, ainda faltam R${} para sacar'.format(v, v - d))
        q = int(input('Qual o valor da nota: '))
        n = int(input('Quantidade de notas: '))
        if q != 1 and (q%5 == 0) or q > 100:
            print('Foi solicitado {} notas de R${:.2f}'.format(n, q))
            d = d + (q * n)
    print('\nSAQUE CONCLUÍDO COM SUCESSO!')
    print('Obrigado por usar nossos serviços!')
elif r == 'n' or r == 'N':
    print('Não será realizado o saque, atendimento finalizado')
else:
    print('OPÇÂO INVAlIDA! Digite > s < ou > n < !')

