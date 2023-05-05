# Desenvolva uma lógica que leia o peso e a altura de uma pessoa;
# Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

kg = float(input('Digite seu peso (KG): '))
alt = float(input('Digite sua altura (m): '))

imc = kg / (alt ** 2)

print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso! ')
elif imc < 25:
    print('Peso ideal! ')
elif imc < 30:
    print('Sobrepeso! ')
elif imc < 40:
    print('Obesidade! ')
else:
    print('Obesidade mórbida! ')
