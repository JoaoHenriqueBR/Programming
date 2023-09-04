'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
'''

from math import inf

c = 0
altura = 0
peso = 0
menor = inf
magro = inf
alto = 0
fat = 0
codmenor = 0
codalto = 0
codfat = 0
codmagro = 0
while c >= 0:
    try:
        cod = int(input('Digite o código do Cliente (0 Para finalizar): '))
    except:
        print('Código Inválido! Tente novamente.')
        continue
    if cod == 0:
        break
    else:
        c += 1
        try:
            alt = float(input('Informe sua altura: (M) '))
            pes = float(input('Informe seu peso (KG): '))
        except:
            print('Valor Inválido! Tente novamente.')
            continue
        altura += alt
        peso += pes
        if alt > alto:
            alto = alt
            codalto = cod
        if alt < menor:
            menor = alt
            codmenor = cod
        if pes > fat:
            fat = pes
            codfat = cod
        if pes < magro:
            magro = pes
            codmagro = cod

print(f'Mais alto: (COD: {codalto}) - {alto}M')
print(f'Mais baixo: (COD: {codmenor}) - {menor}M')
print(f'Mais gordo: (COD: {codfat}) - {fat}KG')
print(f'Mais magro: (COD: {codmagro}) - {magro}KG')
print('')
print('Média de altura da Academia: {:.2f}M'.format(altura/c))
print('Média de peso da Academia: {:.1f}KG'.format(peso/c))
