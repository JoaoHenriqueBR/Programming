# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem:
#   R$ 0,50 por Km para viagens de até 200Km
#   R$ 0,45 para viagens mais longas

distancia = int(input('Informe a distância da sua viagem (Em Km): '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('A viagem custará R$ {:.2f}.'.format(preco))
