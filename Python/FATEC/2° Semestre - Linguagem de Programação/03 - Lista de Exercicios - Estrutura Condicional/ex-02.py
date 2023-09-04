# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exibauma mensagem dizendo que o usuário foi multado. 
# Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h. 

vel = int(input('Velocidade do carro: '))

if vel > 80:
    print('MULTADO! ')
    multa = (vel - 80)*5
    print(f'Valor: R$ {multa:.2f}')
else:
    print('Velocidade Segura! Boa viagem :)')
