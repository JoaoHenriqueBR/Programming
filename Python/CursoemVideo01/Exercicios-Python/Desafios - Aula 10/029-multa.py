# Escreva um programa que leia a velocidade de um carro.
#
# Se ele ultrapassar 80 KM/h, mostre uma mensagem dizendo que ele foi multado.
# 
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input('Informe a velocidade do veiculo: '))
diferença = velocidade - 80
multa = diferença * 7


if velocidade > 80:
    print('MULTADO! Excedeu por {} KM/h o limite! Deve pagar o valor de R$ {:.2f}!'.format(diferença, multa))
else:
    print('Não ultrapassou o limite de 80 KM/h, tudo certo com o veiculo! ')
