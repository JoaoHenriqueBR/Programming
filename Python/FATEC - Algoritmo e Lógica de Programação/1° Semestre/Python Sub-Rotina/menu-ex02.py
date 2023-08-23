print('{:=^40}'.format(' LOJAS JH '))

c = 0

while c < 1:
    try:
        valor = float(input('Informe o valor da prestação (use . para centavos): R$ '))
        dias = int(input('Dias em atraso: '))
        break
    except:
        print('Valor Inválido! Tente novamente. \n')

txmulta = (valor/100)*2
meses = dias / 30
txjuros = (valor/100)*meses


juros = txjuros* (1/30) * dias * valor
vlpagar = valor + txmulta + juros

print('\nValor original: {:.2f}'.format(valor))
print('DIAS de atraso: {}'.format(dias))
print('Multa: {:.2f}'.format(txmulta))
print('Juros: {:.2f}'.format(juros))
print('Valor final -> {:.2f}'.format(vlpagar))
